import dask, time
import dask.array as da

def do_dot():
    t0 = time.time()
    x = da.random.random((12000, 12000), chunks=(4000, 4000))
    x.dot(x.T).sum().compute()
    print('Time: ',time.time() - t0)

for x in range(3):
    do_dot()
