#TestNetflix.py

#Unit tests

from io         import StringIO
from unittest   import main, TestCase
from Netflix    import netflix_cal


class TestNetflix (TestCase) :

    def test_netflix_cal_1 (self) :
        r = StringIO( "1:\n30878\n2647871\n1283744\n2488120\n317050\n1904905\n1989766\n")
        w = StringIO()



    def test_netflix_load_cache_1(self) :
        cache = netflix_load_cache();
        self.assertEqual(cache[0], json.load(open('/u/mck782/netflix-tests/pma459-usrAvgCache.json', 'r')))

    def test_netflix_load_cache_2(self) :
        cache = netflix_load_cache();
        self.assertEqual(cache[1], json.load(open('/u/mck782/netflix-tests/pma459-mvAvgCache.json', 'r')))

    def test_netflix_load_cache_3(self) :
        cache = netflix_load_cache();
        self.assertEqual(cache[2], json.load(open('/u/mck782/netflix-tests/pma459-answersCache.json', 'r')))

    def test_netflix_load_cache_4(self) :
        cache = netflix_load_cache();
        self.assertEqual(cache[3], json.load(open('/u/mck782/netflix-tests/af22574-movieDates.json', 'r')))

    def test_netflix_load_cache_5(self) :
        cache = netflix_load_cache();
        self.assertEqual(cache[4], MYcache = json.load(open('/u/mck782/netflix-tests/cdm2697-userRatingsAveragedOver10yInterval-v2.json', 'r')))

    def test_netflix_read_1(self) :

    def test_netflix_read_2(self) :

    def test_netflix_read_3(self) :









if __name__ == "__main__" :
    main()
