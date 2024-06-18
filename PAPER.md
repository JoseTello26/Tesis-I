# Comparación de Algoritmos de Compresión de Video usando Redes Neuronales

## Introducción

La compresión de datos ha sido un reto desde muchos años antes de tener las computadoras que conocemos actualmente. La transmisión de información sensible por parte de fuerzas enemigas en una guerra implicaba una manera de encriptar y encapsular esos datos, de tal manera que sean fáciles de transportar pero difíciles de descifrar. Sin embargo, el tipo de datos que nos compete son los elaborados después del desarrollo de la Teoría de la Información (Claude E. Shannon) en 1940, que marcaría un antes y un después en la perspectiva que se tenía sobre la transmisión de datos. El problema en ese entonces ya no radicaba en ¿Cómo enviar o recibir cualquier tipo de datos?, pues gracias a Shannon, se estandarizó y se supo que prácticamente cualquier tipo de información podría ser enviada en base a bits. El problema cambió totalmente, y evolucionó a la pregunta ¿Existe una manera de enviar datos con un menor número de bits?, ya que un mayor número de bits resultaba en un mayor tiempo de envío de dicha información, cuando tenemos partes de la misma que pueden ser omitidos sin alterar el mensaje final.

Es así que gran parte de los esfuerzos de matemáticos y científicos afines a la computación centraron sus esfuerzos en elaborar algoritmos que puedan comprimir, de manera significativa y eficiente, tipos de información específica, dependiendo de sus características. 

El caso de la compresión de archivos de imágenes y videos llama mucho la atención. Según Cisco, estuvo previsto que para finales de 2021, el tráfico de video en internet representaría el 82% de todos los datos, además de alcanzar los 227.6 Exabytes por mes, por lo que se entiende que la compresión de video es un tópico de uso frecuente mas actualmente que en años anteriores. Es por ello que tienen una gran diversidad de formatos y dimensiones, como videos HDR, 4K, 6K, 8K, 3D y videos en 360°. 

Los codecs de video usados en al actualidad se ven en la necesidad de adaptarse a los formatos de video cambiantes debido a las novedades que aporta la tecnología. Muchos de ellos sin embargo, presentan inconvenientes a la hora de ponerse en práctica.

- Los formatos de video actuales cada vez están aumentando su resolución, haciendo su compresión mucho mas difícil.
- Los formatos de video distintos que cada vez son mas demandados, requieren funcionar en un ancho de banda limitado, por lo que se tiende a sacrificar la calidad de los mismos en cierta medida.
- Durante una transmisión de un archivo de video, dado un ancho de banda cambiante, pueden ocurrir fluctuaciones en el flujo de datos y por lo tanto, ocasionar la degradación de la calidad del video mismo con el fin de mantener una transmisión de datos estable.

**Revisión del estado actual**

A la fecha, se han desarrollado múltiples algoritmos en codecs con el fin de comprimir archivos de video. Estos algoritmos pueden clasificarse en algoritmos con pérdida o sin pérdida de datos, pues algunos tienden a eliminar información no relevante para la vista humana.

Algunos ejemplos de codecs con algoritmos de compresión usados actualmente son:

- H.264 (Advanced Video Coding): Desarrollado para 2003, es un codec desarrollado por el ITU-T y el ISO. Permite la compresión compatible con Blue-ray, HD DVD y streaming en casi cualquier plataforma. Con mas de 10 años de desarrollo, es el codec mas aceptado actualmente.
- H.265 (High Efficiency Video Coding): Sucesor de H.264, desarrollado en 2013, optimiza la compresión facilitando la transmisión de videos en vivo en HD.
- H.266 (Versatile Video Coding): Publicado en 2020, es el sucesor del HEVC. Promete tener una compresión hasta 50% mas eficiente que su predecesor. Como características adicionales, soporta archivos de video del tipo HDR y videos 360° y transmisión de datos con resolución adaptiva.

Por lo general estos algoritmos, tienen dos etapas, las cuales son:

- Decorrelación: Búsqueda de redundancias en el archivo de video, sean temporales (inter codificación, comparación entre fotogramas) o espaciales (intra codificación, comparación dentro de un fotograma), para poder realizar predicciones respecto al resto del contenido.
- Codificación entrópica: Representación del archivo de video basado en métodos estadísticos, conociendo de antemano qué elementos del son los mas frecuentes, para representarlos con una cantidad menor de bits.

Es en el paso de Decorrelación que entran las posibles soluciones, al ser un paso que requiere de métodos de predicción, es donde entran las redes neuronales. Una de las soluciones que parece llamar la atención y promete dar buenos resultados es el uso de redes neuronales para facilitar el proceso de predicción en la compresión de video. 

**Soluciones Propuestas**

Existen muchas razones para que esta solución sea viable, como que los algoritmos elaborados para deep learning tienen la propiedad de que se ajustan al tipo de dato que tienen y aprenden de ello. Otra razón es que los algoritmos tradicionales de compresión requieren de parámetros previamente establecidos para realizar una compresión, sin embargo, las redes neuronales por definición cambian sus parámetros para poder adaptarse al problema al que se enfrentan, y podrían ser muy útiles a la hora de facilitar los parámetros para codecs dependiendo del tipo de video que se intente comprimir. Esto último también nos lleva a mencionar que las redes neuronales aceptan una gran variedad de datos, en cuanto a dimensiones y tamaños se refiere.

La aplicación de redes neuronales en sus diversas formas se deriva principalmente en las dos etapas principales de los algoritmos de compresión convencionales, las cuales son las que mas han variado a lo largo de los años: la intra-predicción y la inter-predicción

Intrapredicción usando Redes Neuronales

Uno de los métodos planteados en [] se centra en implementar redes convolucionales de manera híbrida con codecs como H.265 empleando un enfoque basado en el aprendizaje residual. Se realiza la intrapredicción de los macrobloques (8x8) de un fotograma con el propio codec, para luego usar esa predicción, junto a una vecindad de tres macrobloques vecinos al predecido (un bloque total de 16x16) como la entrada para la CNN (Convolutional Neural Network) y la salida será la substacción de los bloques originales con los bloques de entrada. A esta red convolucional se le denomina Intra-Prediction CNN (IPCNN).

Finalmente, el macrobloque 8x8 predecido será el macrobloque de entrada restado con la salida del residuo predecido por la IPCNN. 

Este método en particular ha probado ser eficiente al reducir los residuos obtenidos en la predicción de bloques, dado que usa bloques cercanos al objetivo para aportar una entrada con información espacial contextualizada a las CNN.

Otro método planteado en [] aprovecha las CNN y su capacidad de extracción de características de imágenes para de-escalar las estructuras de árbol de macrobloques obtenidas por H.265, y realizando sobre estas las predicciones. La decodificación de las imágenes se realiza con el proceso de decodificación de H.265 y una CNN entrenada para re-escalar los macrobloques decodificados a su resolución original. Los resultados obtenidos de este algoritmo logran reducir el bitrate de un video procesado en un 5.5% respecto a H.265.



Interpredicción usando Redes Neuronales

Este método busca incluir una CNN al codec de video para encargarse de la fase de interpredicción, es decir, el análisis de fotogramas en base a los previamente analizados. Para llevar una buena compresión a cabo, se busca minimizar el MSE (error cuadrático medio) entre la entrada provista a la CNN (predicción de HEVC) )y su señal original

**Selección de una aproximación de hipótesis**

A pesar que los enfoques tradicionales descritos anteriormente suponen mejoras significativas en la compresión en ciertos contextos específicos, se vuelven imprácticos al tratar de mejorarlos. De igual manera con el uso de una red neuronal de lado con un codec de video. Es por eso que el enfoque actual es tratar de usar una serie de distintas redes neuronales que trabajen en conjunto. Asi, tenemos los siguientes avances:

**DeepCoder**

Es un framework de codificación formado a partir de la combinación de distintas CNN. Deepcoder sigue la misma estructura que un algoritmo de compresión de video convencional, variando en la etapa de predicción, en donde utiliza CNNs tanto para codificar como para decodificar las intrapredicciones y los residuales de cada fotograma. 

Cada macrobloque de 32x32 de un fotograma puede ser predecido tanto por intra-predicción como por inter-predicción, pero se elige solo uno mediante una comparación entre ambas predicciones (MSE). 

- En la inter-predicción, se realiza una búsqueda por fuerza bruta en una ventana del frame anterior. Se elige aquel macrobloque con menor MSE respecto al macrobloque original. Adicionalmente se propone usar un parámetro adicional en la codificación: \textbf{SKIP}, el cual denotará que el bloque se mantiene sin cambios si el MSE de un macrobloque con su relacionado en el anterior frame es menor a un valor umbral.

- En la intra-predicción se le aplica una red convolucional de 5 capas, de lo cual se obtiene un mapa de características que posteriormente se decodificará con una red simétrica a la previa.

- Para simplificar la codificación de los residuales, se utiliza la misma CNN usada en la intrapredicción, pero con pesos distintos.

- Tanto la red de predicción como la de residuales se entrenan en base a la función de costo
  $$
  \mathcal{L} = \frac{1}{N} \sum^{N}_{n=1}\| Y_n - X_n\|^2
  $$
  Donde $Y_n$ es la imagen reconstruida y $X_n$ es la imagen original

Como resultado de evaluar el desempeño de esta implementación, se obtuvieron resultados muy similares a H.264 en cuanto a eficiencia pero con menor pérdida.

**DVC**

Este método consta de una serie de CNNs al igual que DeepCoder, pero opta por un procedimiento mas relacionado al tradicional, que se puede resumir en 6 pasos:

1. La estimación de movimiento se da calculando el flujo óptico de los fotogramas, usando vectores de movimiento denotados por $\hat v_t$. Estos son calculados y se pasan a traves de una serie de red de capas convolucionales (\textbf{Red de Codificación/Decodificación de Vectores de Movimiento}) para reducir su tamaño, dando como resultado la cuantización del flujo óptico $\hat m_t$
2. Se define la \textbf{Red de Compensación de Movimiento} se especializa en predecir los fotogramas usando el flujo óptico obtenido en el paso 1. Se obtienen los fotogramas predecidos $\bar x_t$ tomando el fotograma reconstruido previo ($\hat{x}_{t-1}$) distorsionado con el vector de movimiento $v_t$, $\hat{x}_{t-1}$ y $v_t$ se ingresan como parámetros a la red mencionada.
3. Se usa una transformación no linear (\textbf{Red de Codificación de Residuos}) que lleve los residuos (obtenidos de sustraer los fotogramas predecidos de los originales) $r_t$ hacia $y_t$. Luego $y_t$ es llevado a  $\hat y_t$ mediante el proceso de cuantización
4. Se usa  $\hat y_t$ como entrada a la \textbf{Red de Decodificación de Residuos} que obtiene el valor del residual reconstruido, $\hat r_t$
5. Se usa una CNN para obtener la distribución de probabilidad de cada símbolo codificado en $\hat m_t$ y  $\hat y_t$ (entropy coding).
6. Finalmente, se realiza la reconstrucción de los fotogramas haciendo $\hat x_t = \bar x_t + \hat r_t$

Para entrenar la red neuronal se utiliza el entrenamiento basado en la cantidad de bits necesarios para codificar un video, definiendo la función de coste:
$$
\mathcal{L} = \lambda d(x_t, \hat{x}_t) + (H(\hat{m}_t) + H(\hat{y}_t))
$$
Donde $d$ es la función que mide la distorsión entre $x_t$ y $\hat{x}_t$ y $H(x)$ denota la cantidad de bits utilizados para codificar $x$

Según los resultados obtenidos en [], el método empleado logra obtener un mejor resultado que los codecs evaluados hasta el momento, que son H.264 y H.265, lo cual resulta en una nueva estrategia para abordar la compresión de video, además de ser extensible aplicando incluso mejores algoritmos para hallar el flujo óptico.



**Compresión de video**

Sin compresión:

- Videos de alta calidad -> archivos mas grandes, mayor almacenamiento requerido, mayor tiempo de transmisión
- Videos de baja calidad -> archivos mas pequeños, menor almacenamiento y menor tiempo de transferencia

¿Disminuir tamaño de archivos sin afectar la calidad? 

**COMPRESIÓN**

- Busca reducir el tamaño de los archivos de video
- Se realiza en dos pasos: Decorrelación y codificación entrópica
- Decorrelación: Búsqueda de redundancias en el archivo de video, sean temporales o espaciales
- Codificación entrópica: Representación del archivo de video basado en métodos estadísticos, conociendo de antemano qué elementos del archivo son los mas frecuentes, para representarlos con una cantidad menor de bits
- Tipos:
  - Con pérdida
  - Sin pérdida
- Video codec: Compresor y codificador/decodificador de archivos de video
  - H.264 (AVC)
  - H.265 (HEVC)
  - H.266

