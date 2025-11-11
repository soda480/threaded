from threaded_order import ThreadedOrder
from common import runit

def main():
    threaded = ThreadedOrder(workers=5, setup_logging=True)
    threaded.register(lambda: runit('i01'), name='i01')
    threaded.register(lambda: runit('i02'), name='i02')
    threaded.register(lambda: runit('i03'), name='i03')
    threaded.register(lambda: runit('i04'), name='i04')
    threaded.register(lambda: runit('i05'), name='i05', after=['i01'])
    threaded.register(lambda: runit('i06'), name='i06', after=['i01'])
    threaded.register(lambda: runit('i07'), name='i07', after=['i01'])
    threaded.register(lambda: runit('i08'), name='i08', after=['i01'])
    threaded.register(lambda: runit('i09'), name='i09', after=['i04'])
    threaded.register(lambda: runit('i10'), name='i10', after=['i04'])
    threaded.register(lambda: runit('i11'), name='i11', after=['i04'])
    threaded.register(lambda: runit('i12'), name='i12', after=['i06'])
    threaded.register(lambda: runit('i13'), name='i13', after=['i06'])
    threaded.register(lambda: runit('i14'), name='i14', after=['i06'])
    threaded.register(lambda: runit('i15'), name='i15', after=['i09'])
    threaded.register(lambda: runit('i16'), name='i16', after=['i12'])
    threaded.register(lambda: runit('i17'), name='i17', after=['i16'])
    threaded.start()

if __name__ == '__main__':
    main()
