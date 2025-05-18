# CommII_A1_G4 
# **Laboratorio 4 - Modulación M-PSK**

Durante esta práctica se implementaron distintas modulaciones en fase (PSK) usando GNU Radio, específicamente BPSK, QPSK, 8-PSK, 16-PSK y 32-PSK, en un entorno totalmente digital y orientado a SDR (Radio Definida por Software). Se trabajó con fuentes aleatorias y definidas, vectores de constelación personalizados, y se realizaron pruebas tanto en condiciones ideales como con ruido gaussiano agregado.

Se visualizó la envolvente compleja, se midió el ancho de banda usando la regla de -20 dB, y se observó cómo cambian los diagramas de constelación bajo distintas condiciones.

---

## Lo que se logró

- Se comprendió cómo la rata de símbolos afecta directamente la separación de ceros en el espectro de frecuencia.
- Se observó cómo el ruido degrada las constelaciones, especialmente en modulaciones de orden superior.
- Se trabajó con tablas de verdad programadas como vectores para asegurar correspondencia entre símbolos binarios y puntos en la constelación.
- Se analizaron parámetros clave como:
- Ancho de banda (PSD)
- Eficiencia espectral
- Robustez frente al ruido

---

## Herramientas utilizadas

- GNU Radio (bloques QT GUI: Frequency Sink, Constellation Sink, Time Sink)
- Git y GitHub para control de versiones
- Bloques utilizados: `Random Source`, `Vector Source`, `VCO`, `Complex Multiply`, `Interpolating FIR Filter`, etc.

---

## Comparación de modulaciones

| Modulación | Tasa de bits | Ancho de banda | Robustez al ruido |
|------------|--------------|----------------|-------------------|
| BPSK       | Baja         | Bajo           | Alta              |
| QPSK       | Media        | Moderado       | Buena             |
| 8-PSK      | Alta         | Mayor          | Media             |
| 16-PSK     | Más alta     | Alto           | Baja              |
| 32-PSK     | Muy alta     | Muy alto       | Muy baja          |

---

## Conclusiones

- La M-PSK es altamente eficiente para transmisión de datos cuando se controla el ruido del canal.
- Las modulaciones de orden superior(como 16-PSK y 32-PSK) ofrecen mayores tasas de bits pero son más susceptibles a errores.
- La visualización de constelaciones permite evaluar rápidamente la integridad de la señal.
- Se validó que la implementación de modulaciones en GNU Radio es completamente reproducible al usar vectores definidos.
