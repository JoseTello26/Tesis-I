# Comparación de Algoritmos de Compresión de Video usando Redes Neuronales

## **INTRODUCCIÓN**

La compresión de datos ha sido un reto desde muchos años antes de tener las computadoras que conocemos actualmente. La transmisión de información sensible por parte de fuerzas enemigas en una guerra implicaba una manera de encriptar y encapsular esos datos, de tal manera que sean fáciles de transportar pero difíciles de descifrar. Sin embargo, el tipo de datos que nos compete son los elaborados después del desarrollo de la Teoría de la Información (Claude E. Shannon) en 1940, que marcaría un antes y un después en la perspectiva que se tenía sobre la transmisión de datos. El problema en ese entonces ya no radicaba en ¿Cómo enviar o recibir cualquier tipo de datos?, pues gracias a Shannon, se estandarizó y se supo que prácticamente cualquier tipo de información podría ser enviada en base a bits. El problema cambió totalmente, y evolucionó a la pregunta ¿Existe una manera de enviar datos con un menor número de bits?, ya que un mayor número de bits resultaba en un mayor tiempo de envío de dicha información, cuando tenemos partes de la misma que pueden ser omitidos sin alterar el mensaje final.

Es así que gran parte de los esfuerzos de matemáticos y científicos afines a la computación centraron sus esfuerzos en elaborar algoritmos que puedan comprimir, de manera significativa y eficiente, tipos de información específica, dependiendo de sus características.

### Descripción del problema

El caso de la compresión de archivos de imágenes y videos llama mucho la atención. Según Cisco, estuvo previsto que para finales de 2021, el tráfico de video en internet representaría el 82% de todos los datos, además de alcanzar los 227.6 Exabytes por mes, por lo que se entiende que la compresión de video es un tópico de uso frecuente más actualmente que en años anteriores. Es por ello que tienen una gran diversidad de formatos y dimensiones, como videos HDR, 4K, 6K, 8K, 3D y videos en 360° [Cisco:2016].

Los codecs de video usados en la actualidad se ven en la necesidad de adaptarse a los formatos de video cambiantes debido a las novedades que aporta la tecnología. Muchos de ellos, sin embargo, presentan inconvenientes a la hora de ponerse en práctica.

- Los formatos de video actuales cada vez están aumentando su resolución, haciendo su compresión mucho más difícil.
- Los formatos de video distintos que cada vez son más demandados requieren funcionar en un ancho de banda limitado, por lo que se tiende a sacrificar la calidad de los mismos en cierta medida.
- Durante una transmisión de un archivo de video, dado un ancho de banda cambiante, pueden ocurrir fluctuaciones en el flujo de datos y, por lo tanto, ocasionar la degradación de la calidad del video mismo con el fin de mantener una transmisión de datos estable.

A la fecha, se han desarrollado múltiples algoritmos en codecs con el fin de comprimir archivos de video. Estos algoritmos pueden clasificarse en algoritmos con pérdida o sin pérdida de datos, pues algunos tienden a eliminar información no relevante para la vista humana.

Algunos ejemplos de codecs con algoritmos de compresión usados actualmente son:

- **H.264 (Advanced Video Coding):** Desarrollado para 2003, es un codec desarrollado por el ITU-T y el ISO. Permite la compresión compatible con Blu-ray, HD DVD y streaming en casi cualquier plataforma. Con más de 10 años de desarrollo, es el codec más aceptado actualmente.
- **H.265 (High Efficiency Video Coding):** Sucesor de H.264, desarrollado en 2013, optimiza la compresión facilitando la transmisión de videos en vivo en HD.
- **H.266 (Versatile Video Coding):** Publicado en 2020, es el sucesor del HEVC. Promete tener una compresión hasta 50% más eficiente que su predecesor. Como características adicionales, soporta archivos de video del tipo HDR y videos 360° y transmisión de datos con resolución adaptiva [EvaluacionH266:2021].

Por lo general, estos algoritmos tienen dos etapas [DeepLearningApproaches:2022], las cuales son:

- **Decorrelación:** Búsqueda de redundancias en el archivo de video, sean temporales (inter codificación, comparación entre fotogramas) o espaciales (intra codificación, comparación dentro de un fotograma), para poder realizar predicciones respecto al resto del contenido.
- **Codificación entrópica:** Representación del archivo de video basado en métodos estadísticos, conociendo de antemano qué elementos de él son los más frecuentes, para representarlos con una cantidad menor de bits.

Es en el paso de Decorrelación que entran las posibles soluciones, al ser un paso que requiere de métodos de predicción, es donde entran las redes neuronales. Una de las soluciones que parece llamar la atención y promete dar buenos resultados es el uso de redes neuronales para facilitar el proceso de predicción en la compresión de video.

### Objetivos

#### Objetivo general

A través de un análisis detallado, este estudio busca proporcionar una visión clara sobre el estado actual de las tecnologías de compresión de video, permitiendo identificar cuáles métodos pueden considerarse como más avanzados y eficaces en la actualidad, con implicaciones significativas para el desarrollo y la adopción de tecnologías de compresión de video en diversos contextos de aplicación. Adicionalmente, se busca no solo determinar cuál método ofrece la mejor calidad de compresión en términos de reducción de ruido y preservación de detalles, sino también identificar los factores determinantes que influyen en su desempeño práctico, especialmente en escenarios de aplicaciones en tiempo real.

#### Objetivos específicos

- Establecer las diferencias técnicas entre los codecs para archivos de video H.264, H.265 y H.265.
- Contrastar los codecs tradicionales de video con los frameworks de compresión DeepCoder y DVC, en términos del ruido producido al finalizar la compresión, usando como referencia una la imagen previa la compresión.
- Validar la superioridad del método DVC por sobre el codec H.266/vVc, en términos de PSNR (Peak Signal to Noise Ratio).
- Establecer qué factores serían los más relevantes e influyentes en la ejecución en tiempo real de dichos algoritmos, para poder verificar si su uso es factible en los casos de uso actuales.

### Hipótesis

A lo largo de este artículo se propone demostrar mediante métodos experimentales que la compresión de un archivo de video usando el framework DVC genera una salida con menor ruido y una predicción más aproximada respecto al archivo original que el codec H.266 (VVC). Esta comparación definiría si finalmente se ha superado completamente a los métodos de compresión con enfoque tradicional hasta el momento, por ello la elección del codec H.266, que es el codec más reciente publicado por la ITU-T.

## MARCO TEÓRICO

### Algoritmos de Compresión

La compresión de video es fundamental en la transmisión, almacenamiento y procesamiento eficiente de datos de video. Los algoritmos de compresión buscan reducir la cantidad de datos necesarios para representar un video, manteniendo una calidad perceptual aceptable.

Para lograr esto, se tienen en cuenta los siguientes principios:

- **Redundancia Espacial:** Aprovecha la correlación entre píxeles cercanos dentro de un fotograma para eliminar la información redundante.
- **Redundancia Temporal:** Aprovecha la similitud entre fotogramas sucesivos en una secuencia de video para eliminar la información temporal redundante.

#### H.264 (Advanced Video Coding)

Es la cuarta generación de la estandarización, publicado en 2003, ha sido desarrollado desde entonces hasta convertirse en el principal estándar de compresión de video usado en internet al año 2020 . Su funcionamiento comprende las siguientes etapas:

**Predicción**

Un fotograma de video está compuesto por píxeles, los cuales a su vez tienen componentes R, G y B. Estos componentes son transformados al espacio de color YUV (Luminancia y Color). Muchos codificadores trabajan en el espacio YUV para identificar mejor los elementos a descartar basados en la recepción de colores del ojo humano.

Se distinguen 3 tipos de fotogramas:

- **I-frame:** Fotograma de referencia, el cual no depende de la predicción de fotogramas anteriores o posteriores.
- **P-frame:** Hacen referencia a I-frames o P-frames anteriores, por lo que su codificación es significativamente menor a los I-frames.
- **B-frame:** Dependen tanto de I-frames y P-frames anteriores y posteriores.

![Frame Types](img/frame-types.png)

Estos fotogramas son divididos en lo que se conocen como Macro-Bloques (MB), los cuales pueden variar de dimensión de 8x8 a 16x16 píxeles. Cada macrobloque luego es procesado por las funciones de intra-predicción e inter-predicción.

- **Intra-predicción:** Cada componente de luminancia y los dos componentes de color son procesados en hasta 9 distintos modos de predicción para bloques 8x8, los cuales son determinados por el sentido en el cual se predecirán los macrobloques. Busca minimizar el error de estimar los píxeles en las 9 direcciones mencionadas dentro de un mismo frame.

  ![Intra-prediction MB](img/h264_intra.png)

- **Inter-predicción:** Cada MB en un frame se utiliza para estimar su movimiento en frames posteriores, realizando una búsqueda en una región de un frame posterior, en donde se calcula un vector de movimiento que es el resultado de trasladar el MB a la sección que reduzca el residual de dicho MB.

  ![Inter-Prediction](img/h264_inter.png)

**Compensación**

Se realiza la predicción de cada uno de los píxeles de los MB respecto a los modos de intra-predicción y respecto a los vectores de movimiento en la inter-predicción.

**Transformación y Cuantización**

El resultado de predecir cada MB es luego comparado respecto al MB original, dando como resultado los residuales de los MB, que serán transformados al dominio de frecuencias mediante la Transformación Coseno Discreta (DCT). La transformación se aplica a un residual de entrada X, del cual se obtiene una transformada W, que a su vez se cuantiza para obtener los nuevos valores buscados. La cuantización consiste en aplicar una división entera, elemento a elemento, la matriz con respecto a una matriz con coeficientes fijos.

**Codificación Entrópica**

Se refiere al proceso de codificar los elementos necesarios (vectores de movimiento, las matrices cuantizadas, etc.) en un stream de bits que será decodificado para reconstruir el archivo. H.264 usa dos métodos de codificación estandarizados: Context Adaptive Variable-Length Coding (CAVALC) y Context-Based Arithmetic Coding (CABAC) .

#### H.265 (High-Efficiency Video Coding)

Es el sucesor del codec H.264. Desarrollado desde 2013, es el estándar de video provisto para reemplazar al H.264, dada la incremental demanda de videos en HD, superando las capacidades del codec previo. El denominado High-Efficiency Video Coder busca reducir el bitrate obtenido con respecto al H.264 en un 50% y aspira a ser el estándar para videos en calidades superiores a 4K.

En términos de aplicación, HEVC busca reducir del 30% al 50% los datos transmitidos por videos en dispositivos móviles, reduciendo así los costos de transmisión de datos a través de la red. Además, busca que los formatos de video en Ultra HD, 4K y 8K sean los estándares en el mercado comercial de streaming .

A pesar de que sigue básicamente la misma estructura que H.264, se diferencia de este principalmente en los siguientes aspectos:

**Coding Tree Units (CTU)**

En H.264, los fotogramas se codifican en macrobloques que pueden variar de tamaño entre 16x16 y 8x8 píxeles. En H.265, la codificación de los fotogramas se realiza mediante una estructura mucho más eficiente, pero más compleja. Los CTU (coding tree units) son árboles de datos creados a partir de bloques de hasta 64x64 píxeles, y a su vez son particionados en 4 sub-particiones de manera recursiva.

![Coding Tree Unit](img/h265_ctu.png)

**Intrapredicción**

HEVC presenta hasta 35 distintas direcciones en las cuales se pueden predecir las estructuras CTU dentro de un mismo frame. Esto aumenta el rango de predicción de los píxeles rodeando a un MB, pero también duplica el número de operaciones que se realizan en comparación con H.264.

![H.264 vs H.265 Intra-Prediction Modes](img/h264_vs_h265.png)

**Procesamiento paralelo**

Tomando en cuenta el aumento de la complejidad en las operaciones, HEVC busca aprovechar el procesamiento en paralelo de los datos de entrada mediante tres estrategias:

- Dividir cada frame en regiones rectangulares sobre las cuales se aplica la codificación y decodificación.
- Aplicar filtros en los bordes de cada MB predecido, uniformizando la imagen total para evitar cambios drásticos entre cada MB.
- El Wavefront Parallel Processing (WPP) permite que cada región de un frame pueda ser dividida en CTU, y para decodificar cada nivel del árbol generado se requiere del nivel anterior.

#### H.266 (Versatile Video Coding)

El Versatile Video Coding fue publicado en 2021. Superando a sus predecesores no solo en cuanto a reducción de bitrate, sino también aumentando la eficiencia y compatibilidad con un mayor número de formatos:

- Videos de resoluciones mayores a 8K y con profundidad de bits de hasta 10 bits.
- Puede adaptarse al procesamiento de contenido generado por computadora como al compartir una pantalla remota.
- Soporta el procesamiento de videos en formato 360°.

**Codificación de MB**

Se deja de lado la codificación en árboles de 4 particiones para pasar a CTU de particiones múltiples, partiendo desde un MB de hasta 128x128 píxeles, que se particiona inicialmente en 4, para posteriormente particionar cada nodo obtenido en múltiples particiones de manera vertical u horizontal adecuándose a las características de los píxeles. Cada nodo del árbol obtenido es denominado Coding Unit (CU).

**Intra-Predicción**

Se cuenta con predicción definida por ángulos. Cada bloque tiene hasta 65 distintas direcciones en las cuales puede predecir los píxeles dentro de un fotograma. El número de ángulos depende del tamaño del bloque y puede variar desde 45° hasta 135°. Se cuenta con distintos métodos de predicción para los componentes lumínicos y cromáticos.

**Inter-Predicción**

Al igual que en AVC y HEVC, se usan vectores de movimiento (MV) para poder estimar el movimiento de un bloque en un conjunto de frames de referencia. Sin embargo, VVC puede tener dos listas de MV referenciando frames distintos que posteriormente promedian las predicciones para formar una sola.

### Redes Neuronales

Las redes neuronales son un modelo computacional inspirado en el funcionamiento del cerebro humano, diseñado para aprender representaciones de datos complejos mediante capas de procesamiento interconectadas. Las redes neuronales convolucionales (CNN) son un tipo específico de red neuronal que se ha destacado en el procesamiento de datos estructurados, especialmente en aplicaciones de visión por computadora.

#### Redes Neuronales Convolucionales

Las redes neuronales convolucionales son una variante especializada de redes neuronales diseñadas para procesar datos estructurados en mallas, como imágenes. Características clave de las CNN incluyen:

- **Convoluciones:** Operación fundamental donde se aplica un filtro (kernel) a regiones solapadas de la entrada, extrayendo características locales.
- **Capas Convolucionales:** Combinan capas convolucionales con capas de activación (como ReLU) para aprender representaciones jerárquicas de características.
- **Pooling:** Operación utilizada para reducir el tamaño espacial de las características y controlar la complejidad del modelo.
- **Aprendizaje Jerárquico de Características:** Las primeras capas aprenden características simples (como bordes y texturas), mientras que las capas posteriores combinan estas características para aprender representaciones más abstractas.

### Métricas

#### Peak Signal to Noise Ratio (PSNR)

Este algoritmo procesa dos señales, una señal "limpia" y otra "distorsionada", y lo que hace es compara las diferencias entre ellas respecto al valor máximo de la señal original. En el contexto de los videos, se entiende como la comparación entre el valor de cada pixel de cada fotograma, obteniendose así un valor de PSNR por cada fotograma, los cuales finalmente se promediarán.

Siendo $I(i,j)$ y  $K(i,j)$ el pixel $(i,j)$ video original y el video comprimido respectivamente, se tiene el error cuadrático medio como:
$$
MSE = \frac{1}{MN}\displaystyle\sum^{M-1}_{i=0}\sum^{N-1}_{j=0}\| I(i,j) - K(i,j)\|^2
$$
Así, el PSNR queda definido como:
$$
PSNR = 10\log_{10}{\left(\frac{MAX_I^2}{MSE}\right)}
$$
La medida tendrá unidades de decibeles, y a medida que se tenga una medida mayor, será un indicador de cuán buena es la compresión

#### Structural Similarity Index (SSIM)

Ejecuta una comparación entre dos imágenes basándose en la capacidad del ojo humano de percibir y diferenciar estructuras de información. Da como resultado un índice entre -1 y 1, el cual mientras mas próximo sea a 1, indica que hay mayor similitud entre las imágenes comparadas.

Esta métrica usa 3 componentes dentro de la imagen: 

- Luminancia: $\mu_x = \frac{1}{N}\displaystyle\sum^N_{i=1}{x_i} $
- Contraste: $\sigma_x= \left(\frac{1}{N-1}\displaystyle\sum^N_{i=1}(x_i-\mu_x)^2\right)$ 
- Estructura: $(x-\mu_x)/\sigma_x$

Dadas dos imágenes $x$ e $y$:

- Comparación de luminancia: 
  $$
  l(x,y) = \frac{2\mu_X\mu_y + C_1}{\mu_x^2+\mu_y^2 + C_1}
  $$

- Comparación de contraste:
  $$
  c(x,y) = \frac{2\sigma_x\sigma_y + C2}{\sigma_x^2 + \sigma_y^2 + C_2}
  $$

- Comparación de estructura:
  $$
  s(x,y) = \frac{\sigma_{xy}+C_3}{\sigma_x\sigma_y + C_3}
  $$
  Donde:
  $$
  \sigma_{xy} = \frac{1}{N-1}\displaystyle\sum^{N}_{i=1}{(x_i - \mu_x)(y_i - \mu_y)}
  $$

Finalmente, se calcula el SSIM como:
$$
SSIM(x,y) = [l(x,y)]^{\alpha}[c(x,y)]^{\beta}[s(x,y)]^{\gamma}
$$
Donde $\alpha>0, \beta>0, \gamma>0$



El conjunto de codecs H.26X son una serie de codecs estandarizados realizados en conjunto por el ITU-T, Video Coding Experts Group (VCEG) y el ISO Moving Pictures Experts Group (MPEG). Cada generación busca desde 1998 adaptarse a distintos tipos de archivos con resoluciones y bitrates cada vez mayores y busca reemplazar al estándar de la generación previa reduciendo aproximadamente en 50% el bitrate requerido para una resolución fija. Son desarrollados con el objetivo de ofrecer una mayor calidad de video a un bitrate menor. []

## ESTADO DEL ARTE

### **DeepCoder**

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

### **DVC**

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

### AV1

El codificador AOMedia Video 1 (AV1) es un algoritmo de compresión de código abierto diseñado por la AOM (Alliance for Open Media) en 2019 como sucesor del codec VP9 de Google.  AV1 sigue la misma estructura básica de un algoritmo de compresión, dividiendo los frames en bloques de píxeles y realizando inter o intra-predicciones entre ellos para finalmente codificar los residuos de realizar las predicciones de cada frame. 

Sin embargo, AV1 ofrece hasta 10 maneras de particionar un macrobloque de hasta 128x128 píxeles (superbloque) de manera recursiva hasta un mínimo de bloques 4x4. Se introducen además las denominadas "baldosas", definidas como un grupo de macrobloques cuyas referencias de intrapredicción están dentro de la baldosa, es decir, agrupa todos los macrobloques cuyas predicciones sean dependientes entre si. Utilizando las baldozas se obtiene que se agrupan los macrobloques con particiones mas reducidas y que por lo tanto determinan una mayor complejidad computacional. El objetivo de las baldosas es identificar estas regiones con particiones reducidas para poder distribuir el trabajo de manera mas equitativa entre los threads en tiempo de ejecución.







---

---

---

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

