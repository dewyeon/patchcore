import subprocess
import argparse
parser=argparse.ArgumentParser(description="run")
parser.add_argument("--n", type=int)
args = parser.parse_args()
n = args.n
root = 'results_k'
coreset = 0.01

if args.n == 0:
    for cl in ['screw', 'capsule', 'grid']:
        for load in [256]:
            for inp in [224]:
                for k in [5, 10]:
                    log_name = cl + '_k' + str(k)+'_'+str(coreset) + str(inp) + str(load)
                    subprocess.call(f"python train.py --n_neighbors {k} --phase test --load_size {load} --input_size {inp} --project_root_path {root} --coreset_sampling_ratio {coreset} --category {cl} --gpu {n} > logs/{log_name}.txt", shell=True)

if args.n == 1:
    for cl in ['screw', 'capsule', 'grid']:
        for load in [256]:
            for inp in [224]:
                for k in [15, 20]:
                    log_name = cl + '_k' + str(k)+'_'+str(coreset) + str(inp) + str(load)
                    subprocess.call(f"python train.py --n_neighbors {k} --phase test --load_size {load} --input_size {inp} --project_root_path {root} --coreset_sampling_ratio {coreset} --category {cl} --gpu {n} > logs/{log_name}.txt", shell=True)

if args.n == 2:
    for cl in ['screw', 'capsule', 'grid']:
        for load in [256]:
            for inp in [224]:
                for k in [25, 30]:
                    log_name = cl + '_k' + str(k)+'_'+str(coreset) + str(inp) + str(load)
                    subprocess.call(f"python train.py --n_neighbors {k} --phase test --load_size {load} --input_size {inp} --project_root_path {root} --coreset_sampling_ratio {coreset} --category {cl} --gpu {n} > logs/{log_name}.txt", shell=True)

if args.n == 3:
    for cl in ['screw', 'capsule', 'grid']:
        for load in [256]:
            for inp in [224]:
                for k in [35, 40]:
                    log_name = cl + '_k' + str(k)+'_'+str(coreset) + str(inp) + str(load)
                    subprocess.call(f"python train.py --n_neighbors {k} --phase test --load_size {load} --input_size {inp} --project_root_path {root} --coreset_sampling_ratio {coreset} --category {cl} --gpu {n} > logs/{log_name}.txt", shell=True)

if args.n == 4:
    for cl in ['screw', 'capsule', 'grid']:
        for load in [256]:
            for inp in [224]:
                for k in [45, 50]:
                    log_name = cl + '_k' + str(k)+'_'+str(coreset) + str(inp) + str(load)
                    subprocess.call(f"python train.py --n_neighbors {k} --phase test --load_size {load} --input_size {inp} --project_root_path {root} --coreset_sampling_ratio {coreset} --category {cl} --gpu {n} > logs/{log_name}.txt", shell=True)

if args.n == 5:
    for cl in ['screw', 'capsule', 'grid']:
        for load in [256]:
            for inp in [224]:
                for k in [75, 100]:
                    log_name = cl + '_k' + str(k)+'_'+str(coreset) + str(inp) + str(load)
                    subprocess.call(f"python train.py --n_neighbors {k} --phase test --load_size {load} --input_size {inp} --project_root_path {root} --coreset_sampling_ratio {coreset} --category {cl} --gpu {n} > logs/{log_name}.txt", shell=True)


if args.n == 6:
    for cl in ['screw', 'capsule', 'grid']:
        for load in [256]:
            for inp in [224]:
                for k in [500]:
                    log_name = cl + '_k' + str(k)+'_'+str(coreset) + str(inp) + str(load)
                    subprocess.call(f"python train.py --n_neighbors {k} --phase test --load_size {load} --input_size {inp} --project_root_path {root} --coreset_sampling_ratio {coreset} --category {cl} --gpu {n} > logs/{log_name}.txt", shell=True)

if args.n == 7:
    for cl in ['screw', 'capsule', 'grid']:
        for load in [256]:
            for inp in [224]:
                for k in [1000]:
                    log_name = cl + '_k' + str(k)+'_'+str(coreset) + str(inp) + str(load)
                    subprocess.call(f"python train.py --n_neighbors {k} --phase test --load_size {load} --input_size {inp} --project_root_path {root} --coreset_sampling_ratio {coreset} --category {cl} --gpu {n} > logs/{log_name}.txt", shell=True)



