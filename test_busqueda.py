from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

# Configuración básica del navegador
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Maximiza la ventana

# Inicialización automática de ChromeDriver
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chrome_options
)

try:
  driver.get("https://duckduckgo.com")

  # Buscar campo de texto
  buscador = driver.find_element(By.NAME, "q")
  buscador.send_keys("inmuebles en Bogotá")
  buscador.send_keys(Keys.RETURN)

  # Esperar resultados
  time.sleep(2)

  # Validar que exista algún resultado
  resultados = driver.find_elements(By.CSS_SELECTOR,'[data-testid="result"]')
  assert len(resultados) > 0, "No se encontraron resultados."
  print(" Prueba funcional completada con éxito")

finally:
    driver.quit()