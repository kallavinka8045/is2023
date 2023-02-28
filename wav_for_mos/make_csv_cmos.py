import glob
import os
import random

prefix = 'https://kallavinka8045.github.io/is2023/wav_for_mos/'
domain_list = ['ablation-study']
category_source = 'proposed'

for domain in domain_list:
    category_list = os.listdir(domain)
    category_list.remove(category_source)
    wav_name_list = os.listdir(os.path.join(domain, category_list[0]))
    with open('audio_url_cmos_{}.csv'.format(domain), 'w', encoding='utf-8') as f:
        for i in range(2):
            if i != 0:
                f.write(',')
            f.write('audio_url{}'.format(i))
        f.write('\n')
        for wav_name in wav_name_list:
            for i, category in enumerate(category_list):
                f.write(os.path.join(prefix, domain, category_source, wav_name))
                f.write(',')
                f.write(os.path.join(prefix, domain, category, wav_name))
                f.write('\n')
