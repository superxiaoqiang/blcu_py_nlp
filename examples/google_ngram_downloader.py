#coding:utf-8
import os

def gen_grams_suffix():
    suffixs = ['0','1','2','3','4','5','6','7','8','9','_ADJ_','_ADP_','_ADV_','_CONJ_','_DET_','_NOUN_','_NUM_','_PRON_','_PRT_','_VERB_']
    letters = [chr(ord('a')+i) for i in range(26)]
    _12 = [ letter+_letter for letter in letters for _letter in ['_']+letters]
    suffixs = suffixs + _12
    return suffixs



def download_a_file(pth, link):
    print('Downloading file:\t{filename}'.format(filename = pth.split('/')[-1]))
    if os.path.exists(pth) and os.path.getsize(pth) < 10485760:
        os.remove(pth)
    if os.path.exists(pth):
        print('{filename} already exists.'.format(filename = pth.split('/')[-1]))
        return
    cmd = 'wget -O "{path}" "{url}"'.format(path=pth, url=link)
    os.system(cmd)

def download_googlebooks_ngram_lang(out_dir='downloads/google_ngrams',lang='english',version='v2',n=1):
    ngram_dir = out_dir+'/'+str(n)
    if not os.path.exists(out_dir+'/'+str(n)):
        os.makedirs(ngram_dir)
    # 20120701
    suffixs = gen_grams_suffix()
    ngram_prefix_sufix={
        '1gram':['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','other','p','pos','punctuation','q','r','s','t','u','v','w','x','y','z'], 
        '2gram':suffixs,
        '3gram':suffixs,
        '4gram':suffixs,
        '5gram':suffixs
    }
    releasedate = {
        'v1':'20090715',
        'v2':'20120701'
    }
    lang_prefix = {
        'english':'eng-all',
        'chinese':'chi-sim-all'
    }
    #http://storage.googleapis.com/books/ngrams/books/googlebooks-eng-all-2gram-20120701-df.gz
    url_pfx = 'http://storage.googleapis.com/books/ngrams/books/'
    pfx = lang_prefix[lang]
    release = releasedate[version]
    ngram=str(n)+'gram'
    ngram_suffix = ngram_prefix_sufix[ngram]
    lstall = []
    for sfx in ngram_suffix:
        name_pts = '-'.join(['googlebooks', pfx, ngram, release, sfx ])+'.gz'
        out_pth = out_dir+'/'+str(n)+'/'+name_pts
        d_link = url_pfx+name_pts
        lstall.append((out_pth, d_link))
    
    # from pprint import pprint
    # pprint(lstall); return
    for itm_dl in lstall:
        out_pth, d_link = itm_dl
        download_a_file(out_pth, d_link)

def main():
    download_googlebooks_ngram_lang(n=1)
    download_googlebooks_ngram_lang(n=2)
    download_googlebooks_ngram_lang(n=3)
    download_googlebooks_ngram_lang(n=4)
    download_googlebooks_ngram_lang(n=5)

    download_googlebooks_ngram_lang(out_dir='downloads/sim_chi_ngrams',lang='chinese',n=1)
    download_googlebooks_ngram_lang(out_dir='downloads/sim_chi_ngrams',lang='chinese',n=2)
    download_googlebooks_ngram_lang(out_dir='downloads/sim_chi_ngrams',lang='chinese',n=3)
    download_googlebooks_ngram_lang(out_dir='downloads/sim_chi_ngrams',lang='chinese',n=4)
    download_googlebooks_ngram_lang(out_dir='downloads/sim_chi_ngrams',lang='chinese',n=5)

if __name__=="__main__":
    main()