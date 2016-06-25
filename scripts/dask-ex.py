import dask, time
import dask.array as da

t0 = time.time()

x = da.random.random((10000, 10000), chunks=(4096, 4096))
x.dot(x.T).sum().compute()

print(time.time() - t0)
