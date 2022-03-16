import subprocess
import argparse
parser=argparse.ArgumentParser(description="run")
parser.add_argument("--n", type=int)
args = parser.parse_args()
n = args.n
root = 'results_k'
coreset = 0.25

if args.n == 0:
    for cl in ['bottle', 'cable', 'wood']:
        subprocess.call(f"python train.py --phase train --project_root_path {root} --coreset_sampling_ratio {coreset} --category {cl} --gpu {n} > logs/{str(cl)}.txt", shell=True)
if args.n == 1:
    for cl in ['capsule', 'carpet']:
        subprocess.call(f"python train.py --phase train --project_root_path {root} --coreset_sampling_ratio {coreset} --category {cl} --gpu {n} > logs/{str(cl)}.txt", shell=True)
if args.n == 2:
    for cl in ['grid', 'hazelnut','zipper']:
        subprocess.call(f"python train.py --phase train --project_root_path {root} --coreset_sampling_ratio {coreset} --category {cl} --gpu {n} > logs/{str(cl)}.txt", shell=True)
if args.n == 3:
    for cl in ['leather', 'transistor']:
        subprocess.call(f"python train.py --phase train --project_root_path {root} --coreset_sampling_ratio {coreset} --category {cl} --gpu {n} > logs/{str(cl)}.txt", shell=True)                                    
if args.n == 4:
    for cl in ['metal_nut', 'pill', 'screw']:
        subprocess.call(f"python train.py --phase train --project_root_path {root} --coreset_sampling_ratio {coreset} --category {cl} --gpu {n} > logs/{str(cl)}.txt", shell=True)
if args.n == 5:
    for cl in ['tile', 'toothbrush']:
        subprocess.call(f"python train.py --phase train --project_root_path {root} --coreset_sampling_ratio {coreset} --category {cl} --gpu {n} > logs/{str(cl)}.txt", shell=True)
