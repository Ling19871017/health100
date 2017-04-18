import pandas as pd

def removeCRLF(x):
    return str(x).strip().replace('\n', ';')

def replaceComma(x):
    return str(x).replace(',', '，')


def init():
    d = pd.read_excel('./sys_templet_2014.xls')
    df = pd.DataFrame(d['ID'])
    df['MBMS'] = d['MBMS']
    df['JBBT'] = d['JBBT']
    del d

    df_temp = df[df['ID'] == '0121']
    df_temp['MBMS'] = df_temp['MBMS'].apply(removeCRLF)
    df_temp['MBMS'] = df_temp['MBMS'].apply(replaceComma)

    df_cleaned = df_temp[df_temp['MBMS'] != 'nan']
    seg_df = pd.read_csv('./mn_temp_seg.csv')

    return df_cleaned, seg_df





