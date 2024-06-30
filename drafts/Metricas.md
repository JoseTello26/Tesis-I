# Métricas para la comparación de imágenes y videos comprimidos

Para poder comparar la eficiencia de los algoritmos Deep Video Coder (DVC) y H.266 (Versatile Video Coder) se usarán implementaciones realizadas por los propios divulgadores de los algoritmos, las cuales están subidas en GitHub

DVC: https://github.com/GuoLusjtu/DVC
H.266: https://github.com/fraunhoferhhi/vvenc

Una vez implementados, se probarán con un conjunto de videos de distintas calidades, dimensiones y a distintos bitrates (bps), usando el programa ffmpeg, el cual provee de muchas opciones y filtros para poder llevar a cabo las compresiones y comparaciones.

Posteriormente, se analizarán las salidas de los algoritmos, y sus tiempos de ejecución, para luego proceder a analizar los videos comprimidos respecto a los originales a través de 3 métodos de comparación de video

## Peak Signal to Noise Ratio (PSNR)

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

## Structural Similarity Index (SSIM)

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

### H.264

Es la cuarta generación de la estandarización, publicado en 2003, ha sido desarrollado desde entonces hasta convertirse en el principal estándar de compresión de video usado en internet al año 2020[] Su funcionamiento comprende las siguientes etapas:

**Predicción**

Un fotograma de video está compuesto por píxeles, los cuales a su vez tienen componentes R, G y B. Estos componentes son transformados al espacio de color YUV (Luminancia y Color). Muchos codificadores trabajan en el espacio YUV para identificar mejor los elementos a descartar basados en la recepción de colores del ojo humano.

Se distinguen 3 tipos de fotogramas:

I-frame: Fotograma de referencia, el cual no depende de la predicción de fotogramas anteriores o posteriores

P-frame: Hacen referencia a I-frames o P-frames anteriores, por lo que su codificación es significativamente menor a los I-frames

B-frame: Dependen tanto de I-frames y P-frames anteriores y posteriores.

Estos fotogramas son divididos en lo que se conocen como Macro-Bloques (MB), los cuales pueden variar de dimensión de 8x8 a 16x16 píxeles. Cada macrobloque luego es procesado por las funciones de intra-predicción e inter-predicción

**Intra-predicción**

Cada componente de luminancia y los dos componentes de color son procesados en hasta 9 distintos modos de predicción para bloques 8x8, los cuales son determinados por el sentido en el cual se predecirán los macrobloques. Busca minimizar el error de estimar los píxeles en las 9 direcciones mencionadas dentro de un mismo frame.

**Inter-predicción (estimación de movimiento)**

Cada MB en un frame se utiliza para estimar su movimiento en frames posteriores, realizando una búsqueda en una región de un frame posterior, en donde se calcula un vector de movimiento que es el resultado de trasladar el MB a la sección que reduzca el residual de dicho MB.

Cada macrobloque de 16x16 puede ser divido aún mas en bloques de 8x8, 16x8, 8x16 y adicionalmente los bloques 8x8 pueden ser divididos en bloques de 4x4 a diferencia de las generaciones anteriores de H.26x que hacían predicciones basadas en bloques fijos. Cada frame puede tener hasta 5 frames de referencia para hacer la estimación del movimiento, lo que reduce los residuales pero incrementa los cálculos y el uso de la memoria.

**Compensación**

Se realiza la predicción de cada uno de los píxeles de los MB respecto a los modos de intra-predicción y respecto a los vectores de movimiento en la inter-predicción

**Transformación y Cuantización**

El resultado de predecir cada MB es luego comparado respecto al MB original, dando como resultado los residuales de los MB, que serán transformados al dominio de frecuencias mediante la Transformación Coseno Discreta (DCT). Toma ventaja del conocimiento previo de que el ojo humano es más sensible al detectar cambios en datos de baja frecuencia que en los de alta frecuencia.

La transformación se aplica a un residual de entrada X, del cual se obtiene una transformada W, que a su vez se cuantiza para obtener los nuevos valores buscados. La cuantización consiste en aplicar una división entera, elemento a elemento, la matriz con respecto a una matriz con coeficientes fija, la cual contiene coeficientes menores en el lado superior izquierdo (menores frecuencias) y coeficientes mayores en el inferior derecho (mayores frecuencias). Así, se obtiene una nueva matriz W' con valores reducidos en su mayoría en el lado de las frecuencias altas. Para decodificar W' se aplica la operación inversa a la cuantización y la DCT inversa, dando como resultado una matriz Y similar a X, pero no igual debido a que se están aplicando operaciones que no son reversibles

**Codificación Entrópica**

Se refiere al proceso de codificar los elementos necesarios (vectores de movimiento, las matrices cuantizadas, etc) en un stream de bits que será decodificado para reconstruir el archivo. H.264 usa 2 métodos de codificación estandarizados: Context adaptive variable-length coding (CAVALC) y Context based arithmetic based coding (CABAC).

### H.265

Es el sucesor del codec H.264. Desarrollado desde 2013 es el estándar de video provisto a reemplazar al H.264, dada la incremental demanda de videos en HD, superando las capacidades del codec previo. El denominado High Efficiency Video Coder busca reducir el bitrate obtenido con respecto al H.264 en un 50% y aspira a ser el estándar para videos en calidades superiores a 4K.

En términos de aplicación, HEVC busca reducir al 50% los datos transmitidos por videos en dispositivos móviles, reduciendo así los costos de transmisión de datos a través de la red. Adicionalmente, busca que los formatos de video en Ultra HD, 4K y 8K sean los estándares en el mercado comercial de streaming.

A pesar de que sigue básicamente la misma estructura que H.264, se diferencia de este principalmente en los siguientes aspectos:

Codificación de MB

En H.264, los fotogramas se codifican en macrobloques que pueden variar de tamaño entre 16x16 y 8x8 píxeles. En H.265, la codificación de los fotogramas se realiza mediante una estructura mucho mas eficiente, pero mas compleja. Los CTU (coding tree units) son árboles de datos creados a partir de bloques de hasta 64x64 píxeles, y a su vez son particionados en 4 sub-particiones de manera recursiva. Esta estructura facilita la predicción de datos mas específicos y detallados.

Intrapredicción

HEVC presenta hasta 35 distintas direcciones en las cuales se pueden predecir las estructuras CTU dentro de un mismo frame. Esto aumenta el rango de predicción de los píxeles rodeando a un MB, pero también duplica el número de operaciones que se realizan en comparación con H.264.

Procesamiento paralelo

Tomando en cuenta el aumento de la complejidad en las operaciones, HEVC busca aprovechar el procesamiento en paralelo de los datos de entrada mediante 3 estrategias:

- Dividir cada frame en regiones rectangulares sobre las cuales se aplica la codificación y decodificación.
- Al aplicarse filtros en los bordes de cada MB predecido, se busca uniformizar la imagen total para evitar cambios drásticos entre cada MB. Dichos filtros se aplican de manera vertical y horizontal en paralelo
- El Wavefront Parallel Processing (WPP) permite que cada region de un frame pueda ser dividida en CTU, y para decodifcar cada nivel del árbol generado se requiere del nivel anterior, por lo que se requiere tomar varias decisiones en paralelo para realizarlo.



### H.266

El Versatile Video Coding fue publicado en 2021. Superando a sus predecesores, no solo en cuanto a reducción de bitrate, sino también aumentando la eficiencia y compatibilidad con un mayor número de formatos:

- Videos de resoluciones mayores a 8K y con profundidad de bits de hasta 10 bits
- Puede adaptarse al procesamiento de contenido generado por computadora como al compartir una pantalla remota 
- Soporta el procesamiento de videos en formato 360°

Se diferencia de sus predecesores en los siguientes aspectos:

Codificación de MB

Se deja de lado la codificación en árboles de 4 particiones para pasar a CTU de particiones múltiples, partiendo desde un MB de hasta 128x128 píxeles, que se particiona inicialmente en 4, para posteriormente particionar cada nodo obtenido en múltiples particiones de manera vertical u horizontal adecuandose a las características de los píxeles. Cada nodo del árbol obtenido es denominado Coding Unit (CU). Adicionalmente, se pueden separar los componentes lumínicos y cromáticos (YUV) en CTUs con particiones distintas.

Intra-Predicción

Se cuenta con predicción definida por ángulos. Cada bloque tiene hasta 65 distintas direcciones en las cuales puede predecir los píxeles dentro de un fotograma. El número de ángulos depende del tamaño del bloque y puede variar desde 45° hasta 135°. Se cuenta con distintos métodos de predicción para los componentes lumínicos y cromáticos. 

Intra-Predicción

Al igual que en AVC y HEVC, se usan vectores de movimiento (MV) para poder estimar el movimiento de un bloque en un conjunto de frames de referencia. Sin embargo, VVC puede tener dos listas de MV referenciando frames distintos que posteriormente promedian las predicciones para formar una sola. Además, VVC logró mejorar la predicción de movimiento a nivel de CU, mejoró la compensación de movimiento usando como referencia sub-bloques de cada CU y aparta el método de estimación de movimiento horizontal para videos inmersivos.





