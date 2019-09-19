#coding:utf-8
import os

def gen_grams_suffix():
    suffixs = [str(s) if s>9 else '0'+str(s) for s in range(99)]
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

def download_google_syntactic_ngram_lang(out_dir='google_syntactic_ngrams',lang='all'):
    # 20120701
    suffixs = gen_grams_suffix()
    prefix = ["Nodes", "Arcs", "Biarcs", "Triarcs", "Quadarcs",\
         "Extended Nodes", "Extended Arcs", "Extended Biarcs", \
         "Extended Triarcs", "Extended Quadarcs", "Nounargs", \
         "Unlex Nounargs", "Verbargs", "Unlex Verbargs"]
    ngram_prefix_sufix={ pfx.lower().replace(' ','-'):suffixs for pfx in prefix}
    releasedate = {
        'v1':'20130501'
    }
    lang_prefix = {
        'all':'eng',
        '1million':'eng-1M',
        'fiction':'eng-fiction',
        'us':'eng-us',
        'gb':'eng-gb'
    }
    #http://commondatastorage.googleapis.com/books/syntactic-ngrams/eng/unlex-verbargs.19-of-99.gz
    url_pfx = 'http://commondatastorage.googleapis.com/books/syntactic-ngrams'
    pfx_lg = lang_prefix[lang]
    if not os.path.exists(out_dir+'/'+pfx_lg):
        os.makedirs(out_dir+'/'+pfx_lg)
    lstall = []
    for pfx, sfxs in ngram_prefix_sufix.items():
        if not os.path.exists(out_dir+'/'+pfx_lg+'/'+pfx):
            os.makedirs(out_dir+'/'+pfx_lg+'/'+pfx)
        for sfx in sfxs:
            name_pts = '{pfx}.{sfx}-of-99.gz'.format(pfx_lg=pfx_lg, pfx=pfx, sfx=sfx)
            out_pth = out_dir+'/'+pfx_lg+'/'+pfx+'/'+name_pts
            d_link = url_pfx+'/'+pfx_lg+'/'+name_pts
            lstall.append((out_pth, d_link))
    
    # from pprint import pprint
    # pprint(lstall); return
    for itm_dl in lstall:
        out_pth, d_link = itm_dl
        download_a_file(out_pth, d_link)

def main():
    download_google_syntactic_ngram_lang()

if __name__=="__main__":
    main()