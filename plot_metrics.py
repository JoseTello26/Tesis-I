import json
import matplotlib.pyplot as plt

# Cargar el archivo JSON
with open('test_metrics.json', 'r') as f:
    data = json.load(f)

with open('dvc.json', 'r') as f:
    dvc = json.load(f)

vid_sizes = [1920*1080, 1920*1080, 352*288, 1280*720, 352*288, 352*288, 352*288]
framerates = [120, 120, 25, 60, 25, 30, 25]

# Colores para los diferentes codecs
colors = {
    'dvc': 'k',
    'vvenc': 'r',
    'x265': 'b',
    'x264': 'g'
}

lines = {
    'dvc': '-',
    'vvenc': '-.',
    'x265': '--',
    'x264': ':'
}
opacity = {
    'dvc': 1,
    'vvenc': 1,
    'x265': 0.7,
    'x264': 0.5
}

# Iterar sobre cada test en el JSON
FROM_TESTS=3
NUM_TESTS=4

test_names = list(data.keys())
selected_tests = test_names[FROM_TESTS-1:NUM_TESTS]
selected_vid_sizes = vid_sizes[FROM_TESTS-1:NUM_TESTS]
selected_framerates = framerates[FROM_TESTS-1:NUM_TESTS]

fig, axs = plt.subplots(2, NUM_TESTS-FROM_TESTS+1, figsize=(10, 5))
for i, test_name in enumerate(selected_tests):
    test_data = data[test_name]
    test_dvc = dvc[test_name]
    #print(test_dvc)
    bpp = []
    bpp_dvc={"psnr":[], "ssim": []}
    psnr_values = {'dvc': [],'vvenc': [], 'x264': [], 'x265': []}
    ssim_values = {'dvc': [],'vvenc': [], 'x264': [], 'x265': []}
    
    # Obtener bpp y métricas
    for j,(bitrate, metrics) in enumerate(test_data.items()):
        bpp.append(int(bitrate[:-1])*1000/(selected_vid_sizes[i]*selected_framerates[i]))  # Remover 'k' y convertir a entero
        bpp_dvc['psnr'].append(test_dvc['psnr_bpp'][j])
        bpp_dvc['ssim'].append(test_dvc['ssim_bpp'][j])
        #print(bpp_dvc)

        for codec, values in metrics.items():
            psnr_values[codec].append(values['psnr'])
            ssim_values[codec].append(values['ssim'])
        psnr_values['dvc'].append(test_dvc['psnr'][j])
        ssim_values['dvc'].append(test_dvc['ssim'][j])
    
    # Ordenar bpp y métricas

    
    print(bpp_dvc)
    sorted_bpp = sorted(bpp)
    
    for codec in ['dvc', 'vvenc', 'x264', 'x265']:
        psnr_sorted = [x for _, x in sorted(zip(bpp, psnr_values[codec]))]
        ssim_sorted = [x for _, x in sorted(zip(bpp, ssim_values[codec]))]
        
        # Crear una figura con dos subplots para cada test
        
        if codec=='dvc':
            axs[0][i].plot(bpp_dvc['psnr'], psnr_values['dvc'], label=f'{codec}', color=colors[codec], ls=lines[codec], marker='o', alpha=opacity[codec])
            axs[1][i].plot(bpp_dvc['ssim'], ssim_values['dvc'], label=f'{codec}', color=colors[codec], ls=lines[codec], marker='o', alpha=opacity[codec])
            continue


        # Plotear PSNR
        axs[0][i].plot(sorted_bpp, psnr_sorted, label=f'{codec}', color=colors[codec], ls=lines[codec], marker='o', alpha=opacity[codec])
        
        # Plotear SSIM
        axs[1][i].plot(sorted_bpp, ssim_sorted, label=f'{codec}', color=colors[codec], ls=lines[codec], marker='o', alpha=opacity[codec])
    
    axs[0][i].set_title(f' {test_name}')
    # Configurar los subplots
    axs[0][i].set_ylabel('PSNR (dB)')
    
    axs[0][i].legend(loc='lower right')
    axs[0][i].grid(True)

    axs[1][i].set_xlabel('bpp')
    axs[1][i].set_ylabel('SSIM')
    axs[1][i].legend(loc='lower right')
    axs[1][i].grid(True)

fig.suptitle("PSNR and SSIM vs bpp")
# Mostrar el plot para cada test
plt.tight_layout()
plt.savefig(f"metrics-{FROM_TESTS}-{NUM_TESTS}.png")
plt.show()
