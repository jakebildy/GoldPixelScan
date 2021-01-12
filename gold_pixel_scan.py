import os
from PIL import Image
import time
from threading import Thread


R_VAL = 150
G_VAL = 150
B_VAL = 150

def scanfilter(directory, filename):

    t0 = time.time()

    ref = os.path.join(directory, filename)
    img = Image.open(ref, 'r')
    width, height = img.size

    pix_val = list(filter(lambda a: a != (0, 0, 0) and a[0] > R_VAL and a[1] > G_VAL and a[2] < B_VAL, img.getdata()))

    t1 = time.time()

    results.append([filename, pix_val.__len__(), (pix_val.__len__() * 100 / (width * height)), t1 - t0])

results = []


directory = input("Enter the directory to run the script on: ")

print("Total number of files in folder: " + os.listdir(directory).__len__().__str__() + "\n")

print("      File Name     | # of Gold Pixels | Percentage of Total Pixels")

threads = []

t_start = time.time()

for filename in os.listdir(directory):
    if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".tif"):
        try:
            t = Thread(target=scanfilter, args=(directory, filename))
            t.start()
            threads.append(t)

        except:
            print("Error: unable to start thread")

    else:
        continue

# join all threads
for t in threads:
    t.join()

new_list = sorted(results, key=lambda x: x[2], reverse=True)

for line in new_list:
    print(line[0] + ' ' * (20 - line[0].__len__()) + "| " +

          line[1].__str__() + " pixels" + ' ' * (10 - line[1].__str__().__len__()) +
          "| " + f"{line[2]:.3f}" + "%" + ' '*10 + f" => {line[3]:.2f}" + " sec")



t_end = time.time()

print(f"Finished in {(t_end - t_start):.2f}" + " seconds")
