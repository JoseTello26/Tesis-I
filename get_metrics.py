import os
import json
from ffmpeg_quality_metrics import FfmpegQualityMetrics

metricas={}
framerates = [120, 120, 25, 60, 25, 30, 25]

def get_metrics(num_directories):
    for i in range(1, num_directories + 1):
        test_directory = os.path.join(f"test{i}")
        metricas[f"test{i}"] = {}
        if os.path.isdir(test_directory):
            #print(f"\nArchivos en {test_directory}:")
            for dir in os.listdir(test_directory):
                if 'k' in dir:
                    bitrate_dir = os.path.join(test_directory, dir)
                    metricas[f"test{i}"][dir] = {}
                    for _, _, files in os.walk(bitrate_dir):
                        for file in files:
                            metricas[test_directory][dir][file.split("_")[1]] = {}
                            dist_video = os.path.join(bitrate_dir,file)
                            original_videl = os.path.join(test_directory,"input.y4m")
                            ffqm = FfmpegQualityMetrics(original_videl, dist_video, framerate=framerates[i-1])
                            ffqm_calc = ffqm.calculate(["ssim", "psnr"])
                            print("-------------------------")
                            print(dist_video)
                            print(ffqm.get_global_stats()["psnr"]["psnr_avg"]["average"])
                            print("-------------------------")
                            metricas[test_directory][dir][file.split("_")[1]]["psnr"] = ffqm.get_global_stats()["psnr"]["psnr_avg"]["average"]
                            metricas[test_directory][dir][file.split("_")[1]]["ssim"] = ffqm.get_global_stats()["ssim"]["ssim_avg"]["average"]




                        
        else:
            print(f"Directorio {test_directory} no encontrado.")



# Definir el número de carpetas principales (test1, test2, ..., test7)
num_directories = 7

# Listar archivos en subcarpetas
get_metrics(num_directories)

with open("test_metrics.json", "w") as outfile:
    json.dump(metricas, outfile, indent=2)