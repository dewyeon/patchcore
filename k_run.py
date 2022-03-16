import subprocess
import argparse
parser=argparse.ArgumentParser(description="run")
parser.add_argument("--n", type=int)
args = parser.parse_args()
n = args.n
root = 'results_k'
coreset = 0.01

if args.n == 0:
    for cl in ['bottle', 'cable', 'wood', 'capsule', 'carpet', 'grid', 'hazelnut','zipper', 'leather', 'transistor', 'metal_nut', 'pill', 'screw', 'tile', 'toothbrush']:
        for load in [512]:
            for inp in [224]:
                log_name = cl + str(coreset) + str(inp) + str(load)
                subprocess.call(f"python train.py --phase train --load_size {load} --input_size {inp} --project_root_path {root} --coreset_sampling_ratio {coreset} --category {cl} --gpu {n} > logs/{log_name}.txt", shell=True)

if args.n == 1:
    for cl in ['bottle', 'cable', 'wood', 'capsule', 'carpet', 'grid', 'hazelnut','zipper', 'leather', 'transistor', 'metal_nut', 'pill', 'screw', 'tile', 'toothbrush']:
        for load in [512]:
            for inp in [128]:
                log_name = cl + str(coreset) + str(inp) + str(load)
                subprocess.call(f"python train.py --phase train --load_size {load} --input_size {inp} --project_root_path {root} --coreset_sampling_ratio {coreset} --category {cl} --gpu {n} > logs/{log_name}.txt", shell=True)

if args.n == 2:
    for cl in ['bottle', 'cable', 'wood', 'capsule', 'carpet', 'grid', 'hazelnut','zipper', 'leather', 'transistor', 'metal_nut', 'pill', 'screw', 'tile', 'toothbrush']:
        for load in [256]:
            for inp in [224]:
                log_name = cl + str(coreset) + str(inp) + str(load)
                subprocess.call(f"python train.py --phase train --load_size {load} --input_size {inp} --project_root_path {root} --coreset_sampling_ratio {coreset} --category {cl} --gpu {n} > logs/{log_name}.txt", shell=True)

if args.n == 3:
    for cl in ['bottle', 'cable', 'wood', 'capsule', 'carpet', 'grid', 'hazelnut','zipper', 'leather', 'transistor', 'metal_nut', 'pill', 'screw', 'tile', 'toothbrush']:
        for load in [256]:
            for inp in [128]:
                log_name = cl + str(coreset) + str(inp) + str(load)
                subprocess.call(f"python train.py --phase train --load_size {load} --input_size {inp} --project_root_path {root} --coreset_sampling_ratio {coreset} --category {cl} --gpu {n} > logs/{log_name}.txt", shell=True)

if args.n == 4:
    for cl in ['bottle', 'cable', 'wood', 'capsule', 'carpet', 'grid', 'hazelnut','zipper', 'leather', 'transistor', 'metal_nut', 'pill', 'screw', 'tile', 'toothbrush']:
        for load in [128]:
            for inp in [224]:
                log_name = cl + str(coreset) + str(inp) + str(load)
                subprocess.call(f"python train.py --phase train --load_size {load} --input_size {inp} --project_root_path {root} --coreset_sampling_ratio {coreset} --category {cl} --gpu {n} > logs/{log_name}.txt", shell=True)

if args.n == 5:
    for cl in ['bottle', 'cable', 'wood', 'capsule', 'carpet', 'grid', 'hazelnut','zipper', 'leather', 'transistor', 'metal_nut', 'pill', 'screw', 'tile', 'toothbrush']:
        for load in [128]:
            for inp in [128]:
                log_name = cl + str(coreset) + str(inp) + str(load)
                subprocess.call(f"python train.py --phase train --load_size {load} --input_size {inp} --project_root_path {root} --coreset_sampling_ratio {coreset} --category {cl} --gpu {n} > logs/{log_name}.txt", shell=True)

if args.n == 6:
    for cl in ['bottle', 'cable', 'wood', 'capsule', 'carpet', 'grid', 'hazelnut','zipper', 'leather', 'transistor', 'metal_nut', 'pill', 'screw', 'tile', 'toothbrush']:
        for load in [384]:
            for inp in [128]:
                log_name = cl + str(coreset) + str(inp) + str(load)
                subprocess.call(f"python train.py --phase train --load_size {load} --input_size {inp} --project_root_path {root} --coreset_sampling_ratio {coreset} --category {cl} --gpu {n} > logs/{log_name}.txt", shell=True)

if args.n == 7:
    for cl in ['bottle', 'cable', 'wood', 'capsule', 'carpet', 'grid', 'hazelnut','zipper', 'leather', 'transistor', 'metal_nut', 'pill', 'screw', 'tile', 'toothbrush']:
        for load in [384]:
            for inp in [224]:
                log_name = cl + str(coreset) + str(inp) + str(load)
                subprocess.call(f"python train.py --phase train --load_size {load} --input_size {inp} --project_root_path {root} --coreset_sampling_ratio {coreset} --category {cl} --gpu {n} > logs/{log_name}.txt", shell=True)

