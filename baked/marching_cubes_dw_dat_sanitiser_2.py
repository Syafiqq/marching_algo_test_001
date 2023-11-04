import numpy as np

import dat_loader


def main(input_paths: [str], output_path: str, size_xy: int, iso_value: int, little_endian: bool):
    data, dimension = dat_loader.load_v3(input_paths, size_xy, iso_value, little_endian=little_endian)
    np.savetxt(output_path, data, fmt='%d')
    print(dimension)


def example_bunny_be():
    main(
        [
            '../images/bunny/1',
            '../images/bunny/2',
            '../images/bunny/3',
            '../images/bunny/4',
            '../images/bunny/5',
            '../images/bunny/6',
            '../images/bunny/7',
            '../images/bunny/8',
            '../images/bunny/9',
            '../images/bunny/10',
            '../images/bunny/11',
            '../images/bunny/12',
            '../images/bunny/13',
            '../images/bunny/14',
            '../images/bunny/15',
            '../images/bunny/16',
            '../images/bunny/17',
            '../images/bunny/18',
            '../images/bunny/19',
            '../images/bunny/20',
            '../images/bunny/21',
            '../images/bunny/22',
            '../images/bunny/23',
            '../images/bunny/24',
            '../images/bunny/25',
            '../images/bunny/26',
            '../images/bunny/27',
            '../images/bunny/28',
            '../images/bunny/29',
            '../images/bunny/30',
            '../images/bunny/31',
            '../images/bunny/32',
            '../images/bunny/33',
            '../images/bunny/34',
            '../images/bunny/35',
            '../images/bunny/36',
            '../images/bunny/37',
            '../images/bunny/38',
            '../images/bunny/39',
            '../images/bunny/40',
            '../images/bunny/41',
            '../images/bunny/42',
            '../images/bunny/43',
            '../images/bunny/44',
            '../images/bunny/45',
            '../images/bunny/46',
            '../images/bunny/47',
            '../images/bunny/48',
            '../images/bunny/49',
            '../images/bunny/50',
            '../images/bunny/51',
            '../images/bunny/52',
            '../images/bunny/53',
            '../images/bunny/54',
            '../images/bunny/55',
            '../images/bunny/56',
            '../images/bunny/57',
            '../images/bunny/58',
            '../images/bunny/59',
            '../images/bunny/60',
            '../images/bunny/61',
            '../images/bunny/62',
            '../images/bunny/63',
            '../images/bunny/64',
            '../images/bunny/65',
            '../images/bunny/66',
            '../images/bunny/67',
            '../images/bunny/68',
            '../images/bunny/69',
            '../images/bunny/70',
            '../images/bunny/71',
            '../images/bunny/72',
            '../images/bunny/73',
            '../images/bunny/74',
            '../images/bunny/75',
            '../images/bunny/76',
            '../images/bunny/77',
            '../images/bunny/78',
            '../images/bunny/79',
            '../images/bunny/80',
            '../images/bunny/81',
            '../images/bunny/82',
            '../images/bunny/83',
            '../images/bunny/84',
            '../images/bunny/85',
            '../images/bunny/86',
            '../images/bunny/87',
            '../images/bunny/88',
            '../images/bunny/89',
            '../images/bunny/90',
            '../images/bunny/91',
            '../images/bunny/92',
            '../images/bunny/93',
            '../images/bunny/94',
            '../images/bunny/95',
            '../images/bunny/96',
            '../images/bunny/97',
            '../images/bunny/98',
            '../images/bunny/99',
            '../images/bunny/100',
            '../images/bunny/101',
            '../images/bunny/102',
            '../images/bunny/103',
            '../images/bunny/104',
            '../images/bunny/105',
            '../images/bunny/106',
            '../images/bunny/107',
            '../images/bunny/108',
            '../images/bunny/109',
            '../images/bunny/110',
            '../images/bunny/111',
            '../images/bunny/112',
            '../images/bunny/113',
            '../images/bunny/114',
            '../images/bunny/115',
            '../images/bunny/116',
            '../images/bunny/117',
            '../images/bunny/118',
            '../images/bunny/119',
            '../images/bunny/120',
            '../images/bunny/121',
            '../images/bunny/122',
            '../images/bunny/123',
            '../images/bunny/124',
            '../images/bunny/125',
            '../images/bunny/126',
            '../images/bunny/127',
            '../images/bunny/128',
            '../images/bunny/129',
            '../images/bunny/130',
            '../images/bunny/131',
            '../images/bunny/132',
            '../images/bunny/133',
            '../images/bunny/134',
            '../images/bunny/135',
            '../images/bunny/136',
            '../images/bunny/137',
            '../images/bunny/138',
            '../images/bunny/139',
            '../images/bunny/140',
            '../images/bunny/141',
            '../images/bunny/142',
            '../images/bunny/143',
            '../images/bunny/144',
            '../images/bunny/145',
            '../images/bunny/146',
            '../images/bunny/147',
            '../images/bunny/148',
            '../images/bunny/149',
            '../images/bunny/150',
            '../images/bunny/151',
            '../images/bunny/152',
            '../images/bunny/153',
            '../images/bunny/154',
            '../images/bunny/155',
            '../images/bunny/156',
            '../images/bunny/157',
            '../images/bunny/158',
            '../images/bunny/159',
            '../images/bunny/160',
            '../images/bunny/161',
            '../images/bunny/162',
            '../images/bunny/163',
            '../images/bunny/164',
            '../images/bunny/165',
            '../images/bunny/166',
            '../images/bunny/167',
            '../images/bunny/168',
            '../images/bunny/169',
            '../images/bunny/170',
            '../images/bunny/171',
            '../images/bunny/172',
            '../images/bunny/173',
            '../images/bunny/174',
            '../images/bunny/175',
            '../images/bunny/176',
            '../images/bunny/177',
            '../images/bunny/178',
            '../images/bunny/179',
            '../images/bunny/180',
            '../images/bunny/181',
            '../images/bunny/182',
            '../images/bunny/183',
            '../images/bunny/184',
            '../images/bunny/185',
            '../images/bunny/186',
            '../images/bunny/187',
            '../images/bunny/188',
            '../images/bunny/189',
            '../images/bunny/190',
            '../images/bunny/191',
            '../images/bunny/192',
            '../images/bunny/193',
            '../images/bunny/194',
            '../images/bunny/195',
            '../images/bunny/196',
            '../images/bunny/197',
            '../images/bunny/198',
            '../images/bunny/199',
            '../images/bunny/200',
            '../images/bunny/201',
            '../images/bunny/202',
            '../images/bunny/203',
            '../images/bunny/204',
            '../images/bunny/205',
            '../images/bunny/206',
            '../images/bunny/207',
            '../images/bunny/208',
            '../images/bunny/209',
            '../images/bunny/210',
            '../images/bunny/211',
            '../images/bunny/212',
            '../images/bunny/213',
            '../images/bunny/214',
            '../images/bunny/215',
            '../images/bunny/216',
            '../images/bunny/217',
            '../images/bunny/218',
            '../images/bunny/219',
            '../images/bunny/220',
            '../images/bunny/221',
            '../images/bunny/222',
            '../images/bunny/223',
            '../images/bunny/224',
            '../images/bunny/225',
            '../images/bunny/226',
            '../images/bunny/227',
            '../images/bunny/228',
            '../images/bunny/229',
            '../images/bunny/230',
            '../images/bunny/231',
            '../images/bunny/232',
            '../images/bunny/233',
            '../images/bunny/234',
            '../images/bunny/235',
            '../images/bunny/236',
            '../images/bunny/237',
            '../images/bunny/238',
            '../images/bunny/239',
            '../images/bunny/240',
            '../images/bunny/241',
            '../images/bunny/242',
            '../images/bunny/243',
            '../images/bunny/244',
            '../images/bunny/245',
            '../images/bunny/246',
            '../images/bunny/247',
            '../images/bunny/248',
            '../images/bunny/249',
            '../images/bunny/250',
            '../images/bunny/251',
            '../images/bunny/252',
            '../images/bunny/253',
            '../images/bunny/254',
            '../images/bunny/255',
            '../images/bunny/256',
            '../images/bunny/257',
            '../images/bunny/258',
            '../images/bunny/259',
            '../images/bunny/260',
            '../images/bunny/261',
            '../images/bunny/262',
            '../images/bunny/263',
            '../images/bunny/264',
            '../images/bunny/265',
            '../images/bunny/266',
            '../images/bunny/267',
            '../images/bunny/268',
            '../images/bunny/269',
            '../images/bunny/270',
            '../images/bunny/271',
            '../images/bunny/272',
            '../images/bunny/273',
            '../images/bunny/274',
            '../images/bunny/275',
            '../images/bunny/276',
            '../images/bunny/277',
            '../images/bunny/278',
            '../images/bunny/279',
            '../images/bunny/280',
            '../images/bunny/281',
            '../images/bunny/282',
            '../images/bunny/283',
            '../images/bunny/284',
            '../images/bunny/285',
            '../images/bunny/286',
            '../images/bunny/287',
            '../images/bunny/288',
            '../images/bunny/289',
            '../images/bunny/290',
            '../images/bunny/291',
            '../images/bunny/292',
            '../images/bunny/293',
            '../images/bunny/294',
            '../images/bunny/295',
            '../images/bunny/296',
            '../images/bunny/297',
            '../images/bunny/298',
            '../images/bunny/299',
            '../images/bunny/300',
            '../images/bunny/301',
            '../images/bunny/302',
            '../images/bunny/303',
            '../images/bunny/304',
            '../images/bunny/305',
            '../images/bunny/306',
            '../images/bunny/307',
            '../images/bunny/308',
            '../images/bunny/309',
            '../images/bunny/310',
            '../images/bunny/311',
            '../images/bunny/312',
            '../images/bunny/313',
            '../images/bunny/314',
            '../images/bunny/315',
            '../images/bunny/316',
            '../images/bunny/317',
            '../images/bunny/318',
            '../images/bunny/319',
            '../images/bunny/320',
            '../images/bunny/321',
            '../images/bunny/322',
            '../images/bunny/323',
            '../images/bunny/324',
            '../images/bunny/325',
            '../images/bunny/326',
            '../images/bunny/327',
            '../images/bunny/328',
            '../images/bunny/329',
            '../images/bunny/330',
            '../images/bunny/331',
            '../images/bunny/332',
            '../images/bunny/333',
            '../images/bunny/334',
            '../images/bunny/335',
            '../images/bunny/336',
            '../images/bunny/337',
            '../images/bunny/338',
            '../images/bunny/339',
            '../images/bunny/340',
            '../images/bunny/341',
            '../images/bunny/342',
            '../images/bunny/343',
            '../images/bunny/344',
            '../images/bunny/345',
            '../images/bunny/346',
            '../images/bunny/347',
            '../images/bunny/348',
            '../images/bunny/349',
            '../images/bunny/350',
            '../images/bunny/351',
            '../images/bunny/352',
            '../images/bunny/353',
            '../images/bunny/354',
            '../images/bunny/355',
            '../images/bunny/356',
            '../images/bunny/357',
            '../images/bunny/358',
            '../images/bunny/359',
            '../images/bunny/360',
            '../images/bunny/361',
        ],
        '../input/objs_bunny_sanitised_be.txt',
        512,
        -1,
        False
    )


def example_bunny_le():
    main(
        [
            '../images/bunny/1',
            '../images/bunny/2',
            '../images/bunny/3',
            '../images/bunny/4',
            '../images/bunny/5',
            '../images/bunny/6',
            '../images/bunny/7',
            '../images/bunny/8',
            '../images/bunny/9',
            '../images/bunny/10',
            '../images/bunny/11',
            '../images/bunny/12',
            '../images/bunny/13',
            '../images/bunny/14',
            '../images/bunny/15',
            '../images/bunny/16',
            '../images/bunny/17',
            '../images/bunny/18',
            '../images/bunny/19',
            '../images/bunny/20',
            '../images/bunny/21',
            '../images/bunny/22',
            '../images/bunny/23',
            '../images/bunny/24',
            '../images/bunny/25',
            '../images/bunny/26',
            '../images/bunny/27',
            '../images/bunny/28',
            '../images/bunny/29',
            '../images/bunny/30',
            '../images/bunny/31',
            '../images/bunny/32',
            '../images/bunny/33',
            '../images/bunny/34',
            '../images/bunny/35',
            '../images/bunny/36',
            '../images/bunny/37',
            '../images/bunny/38',
            '../images/bunny/39',
            '../images/bunny/40',
            '../images/bunny/41',
            '../images/bunny/42',
            '../images/bunny/43',
            '../images/bunny/44',
            '../images/bunny/45',
            '../images/bunny/46',
            '../images/bunny/47',
            '../images/bunny/48',
            '../images/bunny/49',
            '../images/bunny/50',
            '../images/bunny/51',
            '../images/bunny/52',
            '../images/bunny/53',
            '../images/bunny/54',
            '../images/bunny/55',
            '../images/bunny/56',
            '../images/bunny/57',
            '../images/bunny/58',
            '../images/bunny/59',
            '../images/bunny/60',
            '../images/bunny/61',
            '../images/bunny/62',
            '../images/bunny/63',
            '../images/bunny/64',
            '../images/bunny/65',
            '../images/bunny/66',
            '../images/bunny/67',
            '../images/bunny/68',
            '../images/bunny/69',
            '../images/bunny/70',
            '../images/bunny/71',
            '../images/bunny/72',
            '../images/bunny/73',
            '../images/bunny/74',
            '../images/bunny/75',
            '../images/bunny/76',
            '../images/bunny/77',
            '../images/bunny/78',
            '../images/bunny/79',
            '../images/bunny/80',
            '../images/bunny/81',
            '../images/bunny/82',
            '../images/bunny/83',
            '../images/bunny/84',
            '../images/bunny/85',
            '../images/bunny/86',
            '../images/bunny/87',
            '../images/bunny/88',
            '../images/bunny/89',
            '../images/bunny/90',
            '../images/bunny/91',
            '../images/bunny/92',
            '../images/bunny/93',
            '../images/bunny/94',
            '../images/bunny/95',
            '../images/bunny/96',
            '../images/bunny/97',
            '../images/bunny/98',
            '../images/bunny/99',
            '../images/bunny/100',
            '../images/bunny/101',
            '../images/bunny/102',
            '../images/bunny/103',
            '../images/bunny/104',
            '../images/bunny/105',
            '../images/bunny/106',
            '../images/bunny/107',
            '../images/bunny/108',
            '../images/bunny/109',
            '../images/bunny/110',
            '../images/bunny/111',
            '../images/bunny/112',
            '../images/bunny/113',
            '../images/bunny/114',
            '../images/bunny/115',
            '../images/bunny/116',
            '../images/bunny/117',
            '../images/bunny/118',
            '../images/bunny/119',
            '../images/bunny/120',
            '../images/bunny/121',
            '../images/bunny/122',
            '../images/bunny/123',
            '../images/bunny/124',
            '../images/bunny/125',
            '../images/bunny/126',
            '../images/bunny/127',
            '../images/bunny/128',
            '../images/bunny/129',
            '../images/bunny/130',
            '../images/bunny/131',
            '../images/bunny/132',
            '../images/bunny/133',
            '../images/bunny/134',
            '../images/bunny/135',
            '../images/bunny/136',
            '../images/bunny/137',
            '../images/bunny/138',
            '../images/bunny/139',
            '../images/bunny/140',
            '../images/bunny/141',
            '../images/bunny/142',
            '../images/bunny/143',
            '../images/bunny/144',
            '../images/bunny/145',
            '../images/bunny/146',
            '../images/bunny/147',
            '../images/bunny/148',
            '../images/bunny/149',
            '../images/bunny/150',
            '../images/bunny/151',
            '../images/bunny/152',
            '../images/bunny/153',
            '../images/bunny/154',
            '../images/bunny/155',
            '../images/bunny/156',
            '../images/bunny/157',
            '../images/bunny/158',
            '../images/bunny/159',
            '../images/bunny/160',
            '../images/bunny/161',
            '../images/bunny/162',
            '../images/bunny/163',
            '../images/bunny/164',
            '../images/bunny/165',
            '../images/bunny/166',
            '../images/bunny/167',
            '../images/bunny/168',
            '../images/bunny/169',
            '../images/bunny/170',
            '../images/bunny/171',
            '../images/bunny/172',
            '../images/bunny/173',
            '../images/bunny/174',
            '../images/bunny/175',
            '../images/bunny/176',
            '../images/bunny/177',
            '../images/bunny/178',
            '../images/bunny/179',
            '../images/bunny/180',
            '../images/bunny/181',
            '../images/bunny/182',
            '../images/bunny/183',
            '../images/bunny/184',
            '../images/bunny/185',
            '../images/bunny/186',
            '../images/bunny/187',
            '../images/bunny/188',
            '../images/bunny/189',
            '../images/bunny/190',
            '../images/bunny/191',
            '../images/bunny/192',
            '../images/bunny/193',
            '../images/bunny/194',
            '../images/bunny/195',
            '../images/bunny/196',
            '../images/bunny/197',
            '../images/bunny/198',
            '../images/bunny/199',
            '../images/bunny/200',
            '../images/bunny/201',
            '../images/bunny/202',
            '../images/bunny/203',
            '../images/bunny/204',
            '../images/bunny/205',
            '../images/bunny/206',
            '../images/bunny/207',
            '../images/bunny/208',
            '../images/bunny/209',
            '../images/bunny/210',
            '../images/bunny/211',
            '../images/bunny/212',
            '../images/bunny/213',
            '../images/bunny/214',
            '../images/bunny/215',
            '../images/bunny/216',
            '../images/bunny/217',
            '../images/bunny/218',
            '../images/bunny/219',
            '../images/bunny/220',
            '../images/bunny/221',
            '../images/bunny/222',
            '../images/bunny/223',
            '../images/bunny/224',
            '../images/bunny/225',
            '../images/bunny/226',
            '../images/bunny/227',
            '../images/bunny/228',
            '../images/bunny/229',
            '../images/bunny/230',
            '../images/bunny/231',
            '../images/bunny/232',
            '../images/bunny/233',
            '../images/bunny/234',
            '../images/bunny/235',
            '../images/bunny/236',
            '../images/bunny/237',
            '../images/bunny/238',
            '../images/bunny/239',
            '../images/bunny/240',
            '../images/bunny/241',
            '../images/bunny/242',
            '../images/bunny/243',
            '../images/bunny/244',
            '../images/bunny/245',
            '../images/bunny/246',
            '../images/bunny/247',
            '../images/bunny/248',
            '../images/bunny/249',
            '../images/bunny/250',
            '../images/bunny/251',
            '../images/bunny/252',
            '../images/bunny/253',
            '../images/bunny/254',
            '../images/bunny/255',
            '../images/bunny/256',
            '../images/bunny/257',
            '../images/bunny/258',
            '../images/bunny/259',
            '../images/bunny/260',
            '../images/bunny/261',
            '../images/bunny/262',
            '../images/bunny/263',
            '../images/bunny/264',
            '../images/bunny/265',
            '../images/bunny/266',
            '../images/bunny/267',
            '../images/bunny/268',
            '../images/bunny/269',
            '../images/bunny/270',
            '../images/bunny/271',
            '../images/bunny/272',
            '../images/bunny/273',
            '../images/bunny/274',
            '../images/bunny/275',
            '../images/bunny/276',
            '../images/bunny/277',
            '../images/bunny/278',
            '../images/bunny/279',
            '../images/bunny/280',
            '../images/bunny/281',
            '../images/bunny/282',
            '../images/bunny/283',
            '../images/bunny/284',
            '../images/bunny/285',
            '../images/bunny/286',
            '../images/bunny/287',
            '../images/bunny/288',
            '../images/bunny/289',
            '../images/bunny/290',
            '../images/bunny/291',
            '../images/bunny/292',
            '../images/bunny/293',
            '../images/bunny/294',
            '../images/bunny/295',
            '../images/bunny/296',
            '../images/bunny/297',
            '../images/bunny/298',
            '../images/bunny/299',
            '../images/bunny/300',
            '../images/bunny/301',
            '../images/bunny/302',
            '../images/bunny/303',
            '../images/bunny/304',
            '../images/bunny/305',
            '../images/bunny/306',
            '../images/bunny/307',
            '../images/bunny/308',
            '../images/bunny/309',
            '../images/bunny/310',
            '../images/bunny/311',
            '../images/bunny/312',
            '../images/bunny/313',
            '../images/bunny/314',
            '../images/bunny/315',
            '../images/bunny/316',
            '../images/bunny/317',
            '../images/bunny/318',
            '../images/bunny/319',
            '../images/bunny/320',
            '../images/bunny/321',
            '../images/bunny/322',
            '../images/bunny/323',
            '../images/bunny/324',
            '../images/bunny/325',
            '../images/bunny/326',
            '../images/bunny/327',
            '../images/bunny/328',
            '../images/bunny/329',
            '../images/bunny/330',
            '../images/bunny/331',
            '../images/bunny/332',
            '../images/bunny/333',
            '../images/bunny/334',
            '../images/bunny/335',
            '../images/bunny/336',
            '../images/bunny/337',
            '../images/bunny/338',
            '../images/bunny/339',
            '../images/bunny/340',
            '../images/bunny/341',
            '../images/bunny/342',
            '../images/bunny/343',
            '../images/bunny/344',
            '../images/bunny/345',
            '../images/bunny/346',
            '../images/bunny/347',
            '../images/bunny/348',
            '../images/bunny/349',
            '../images/bunny/350',
            '../images/bunny/351',
            '../images/bunny/352',
            '../images/bunny/353',
            '../images/bunny/354',
            '../images/bunny/355',
            '../images/bunny/356',
            '../images/bunny/357',
            '../images/bunny/358',
            '../images/bunny/359',
            '../images/bunny/360',
            '../images/bunny/361',
        ],
        '../input/objs_bunny_sanitised_le.txt',
        512,
        -1,
        True
    )


if __name__ == "__main__":
    pass
