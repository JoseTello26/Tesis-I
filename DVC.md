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