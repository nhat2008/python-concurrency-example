import random
import multiprocessing


def list_append(count, id, out_list):
    for i in range(count):
        out_list.append(random.random())


if __name__ == "__main__":
    size = 10000000  # Number of random numbers
    procs = 2  # Number of processes

    # Create a list of jobs and then iterate through
    # the number of processes appending each process to
    # the job list
    jobs = []
    for i in range(0, procs):
        out_list = list()
        process = multiprocessing.Process(target=list_append,
                                          args=(size, i, out_list))
        jobs.append(process)

    # Start the processes (i.e. calculate the random number lists)
    for j in jobs:
        j.start()

    # Ensure all of the processes have finished
    for j in jobs:
        j.join()

    print "List processing complete."
