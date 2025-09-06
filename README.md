# CommII_A1_G4 
# Laboratorio 3 - De Radiofrecuencia a la Envolvente Compleja (GNU Radio)

Este laboratorio tuvo como objetivo comprender el proceso de conversión de señales de radiofrecuencia (RF) a su representación en envolvente compleja (EC) utilizando la plataforma GNU Radio. Se trabajó con diferentes esquemas de modulación digital como OOK, BPSK y FSK, observando su comportamiento tanto en RF como en EC.

La EC permite una visualización y análisis simplificado de señales moduladas, al centrarlas en el origen del espectro de frecuencia y representar su información en el plano complejo mediante componentes I (in-phase) y Q (quadrature). Este tipo de representación es muy útil en comunicaciones modernas, radar y procesamiento digital de señales.

---

## Objetivos

- Afianzar el concepto de la envolvente compleja (EC) a partir de señales de radiofrecuencia (RF).
- Comprender el funcionamiento interno de bloques como e_RF_VCO_ff y e_EC_VCO_fc.
- Implementar y analizar modulaciones OOK, BPSK y FSK en versiones RF y EC.
- Evaluar el comportamiento de estas modulaciones en los dominios del tiempo, frecuencia y constelación.

---

## Actividades principales

- Se adaptaron flujogramas base para observar la señal OOK en RF y EC.
- Se reconfiguraron los flujogramas para implementar la modulación BPSK, analizando su comportamiento en el dominio del tiempo y en el diagrama de constelación.
- Se diseñó e implementó una versión FSK, ajustando la frecuencia portadora y la desviación de frecuencia, y se observó la señal resultante en sus diferentes dominios.
- Se estudiaron los efectos del número de muestras por símbolo (SPS) en la calidad de representación de la señal.
- Se respondieron preguntas de control sobre diseño de VCOs, ubicación de bloques, y validación de parámetros.

---

## Herramientas utilizadas

- GNU Radio para simulación y visualización (Time Sink, Frequency Sink, Constellation Sink).
- Python para edición y análisis de bloques personalizados (e_RF_VCO_ff, e_EC_VCO_fc).
- Git y GitHub para trabajo colaborativo y control de versiones.
- Ubuntu Linux como entorno operativo.

---

## Conclusiones

- La envolvente compleja resulta una herramienta fundamental para simplificar el análisis de señales moduladas, facilitando la interpretación de la información transmitida.
- Las modulaciones OOK, BPSK y FSK presentan características distintivas que pueden ser evaluadas más eficientemente en EC que en RF.
- El uso adecuado de parámetros como SPS, desviación de frecuencia y ubicación de bloques como Interpolating FIR Filter es clave para garantizar una simulación precisa.
- El diagrama de constelación permitió visualizar con claridad los símbolos digitales representados por cada técnica de modulación, haciendo más intuitivo su análisis.
