#TestNetflix.py

#Unit tests

from io         import StringIO
from unittest   import main, TestCase
from Netflix    import netflix_cal


class TestNetflix (TestCase) :

    def test_netflix_cal_1 (self) :
        r = StringIO( "1:\n30878\n2647871\n1283744\n2488120\n317050\n1904905\n1989766\n")
        w = StringIO()












if __name__ == "__main__" :
    main()
