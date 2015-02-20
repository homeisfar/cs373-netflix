#TestNetflix.py

#Unit tests

from io         import StringIO
from unittest   import main, TestCase
from Netflix    import netflix_load_cache, netflix_read, netflix_cal, netflix_solve
import sys, json

class TestNetflix (TestCase) :

    def test_netflix_cal_1 (self) :
        r = StringIO( "1:\n30878\n2647871\n1283744\n2488120\n317050\n1904905\n1989766\n")
        w = StringIO()

    def test_netflix_load_cache_1(self) :
        cache = netflix_load_cache();
        f = open('/u/mck782/netflix-tests/pma459-usrAvgCache.json', 'r')
        c = json.load(f)
        f.close()
        self.assertEqual(cache[0], c)

    def test_netflix_load_cache_2(self) :
        cache = netflix_load_cache();
        f = open('/u/mck782/netflix-tests/pma459-mvAvgCache.json', 'r')
        c = json.load(f)
        f.close()
        self.assertEqual(cache[1], c)

    def test_netflix_load_cache_3(self) :
        cache = netflix_load_cache();
        f = open('/u/mck782/netflix-tests/pma459-answersCache.json', 'r')
        c = json.load(f)
        f.close()
        self.assertEqual(cache[2], c)

    def test_netflix_load_cache_4(self) :
        cache = netflix_load_cache();
        f = open('/u/mck782/netflix-tests/af22574-movieDates.json', 'r')
        c = json.load(f)
        f.close()
        self.assertEqual(cache[3], c)

    def test_netflix_load_cache_5(self) :
        cache = netflix_load_cache();
        f = open('/u/mck782/netflix-tests/cdm2697-userRatingsAveragedOver10yInterval-v2.json', 'r')
        c = json.load(f)
        f.close()
        self.assertEqual(cache[4], c)

    def test_netflix_read_1(self) :
        self.assertEqual(netflix_read("1:\n")[0], True)
        self.assertEqual(netflix_read("1:\n")[1], "1")

    def test_netflix_read_2(self) :
        self.assertEqual(netflix_read("1\n")[0], False)
        self.assertEqual(netflix_read("1\n")[1], "1")

    def test_netflix_read_3(self) :
        self.assertEqual(netflix_read("11111\n")[1], "11111")

    def test_netflix_read_4(self) :
        self.assertEqual(netflix_read("11111:\n")[1], "11111")


    def test_netflix_cal_1(self) :
        cache = netflix_load_cache()
        self.assertEqual(netflix_cal('1', '30878', cache)[0], 3.6)

    def test_netflix_cal_2(self) :
        cache = netflix_load_cache()
        self.assertEqual(netflix_cal('1', '2647871',cache)[0], 3.1)

    def test_netflix_cal_3(self) :
        cache = netflix_load_cache()
        self.assertEqual(netflix_cal('10', '1952305', cache)[0],3.3)


    def test_netflix_solve_1(self):
        r = StringIO('10014:\n1626179\n1359761\n430376\n')
        w = StringIO()
        netflix_solve(r,w)
        self.assertEqual(w.getvalue(), "10014:\n3.2\n4.2\n3.1\nRMSE: 0.83\n")

    def test_netflix_solve_2(self):
        r = StringIO('1002:\n2174660\n1685301\n')
        w = StringIO()
        netflix_solve(r,w)
        self.assertEqual(w.getvalue(), "1002:\n3.3\n3.0\nRMSE: 0.86\n")
     
    def test_netflix_solve_3(self):
        r = StringIO('10:\n1952305\n1531863\n')
        w = StringIO()
        netflix_solve(r,w)
        self.assertEqual(w.getvalue(), "10:\n3.3\n3.1\nRMSE: 0.22\n")









if __name__ == "__main__" :
    main()
