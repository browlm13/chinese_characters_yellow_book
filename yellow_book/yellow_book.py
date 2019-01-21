#!/usr/bin/env

"""

	Chinese Yellow Book - Character Practice

"""

# external
import pandas as pd

#
# Settings
#

YELLOW_BOOK_DATA_DIR = "data/"
CHARACTER_WORKBOOK_FILE = YELLOW_BOOK_DATA_DIR + "character_workbook_dictionary.csv"

#
# Character's and Pages from Yellow Book
#     ( page # : [character list] )

yellow_book_characters = {
	1 	: ['我','是','美','国','人'],
	2 	: ['你','们','不','也','都'],
	3 	: ['跟','中','学','生','小'],
	4 	: ['朋','友','还','的','个'],
	5 	: ['男','女','贵','姓','丁'],
	6 	: ['他','这','那','只','狗'],
	7 	: ['张','桌','子','椅','把'],
	8 	: ['呢','吗','谁','哪','咱'],
	9 	: ['大','对','老','师','好'],
	10 	: ['虽','然','可','但','叫'],
	11 	: ['早','看','很','有','名'],
	12 	: ['今','天','觉','得','累'],
	13 	: ['床','软','硬','新','旧'],
	14	: ['宿','舍','屋','间','校'],
	15 	: ['教','室','吃','饭','够'],
	16 	: ['昨','晚','错','点','没'],
	17 	: ['鸡','肉','太','每','蛋'],
	18	: ['上','下','午','多','少'],
	19 	: ['高','矮','性','情','鼻'],
	20 	: ['母','亲','眼','睛','课'],
	21 	: ['奇','怪','请','坐','真'],
	22 	: ['英','文','说','话','坏'],
	23 	: ['什','现','在','怎','么'],
	24 	: ['喜','欢','信','会','只'],
	25 	: ['写','字','就','想','饿'],
	26	: ['喝','气','水','清','茶'],
	27 	: ['死','几','红','绿','半'],
	28	: ['皮','包','极','块','钱'],
	29	: ['事','馆','能','别','啊'],
	30 	: ['谢','东','西','来','进'],
	31 	: ['忙','空','李','谈','吧'],
	32	: ['热','凉','行','或','者'],
	33	: ['要','知','道','时','候'],
	34	: ['法','惯','样','当','住'],
	35 	: ['年','完','已','经','月']
} 

yellow_book_df = pd.DataFrame( yellow_book_characters )

#
# Write to CSV File
#
yellow_book_df.to_csv(CHARACTER_WORKBOOK_FILE)


# creater searcher
#cs = CharacterSearcher()

# test search
#print(cs.search_character('喝'))


#
# Practice sentences from Yellow Book
#

yellow_book_sentences = {

	25 : {

			"Conversation 1": {

				'A1': {

					'english' 		: ['Can you write chinese characters?'],
					'pinyin'  		: ['nǐ', 'huì','xiě','zhōng','guó', 'zì', 'ma', '?'],
					'characters' 	: ['你', '会', '写', '中', '国', '字', '吗','?'] 
				},


				'B1': {

					'english' 		: ['I can only write six Chinese characters.'],
					'pinyin'  		: ['wǒ', 'zhǐ', 'huì', 'xiě', 'liù', 'gè', 'zhōng','guó', 'zì'],
					'characters' 	: ['我', '只', '会', '写', '六', '个', '中', '国', '字','。']
				},

				'A2': {

					'english' 		: ['Which characters can you write?'],
					'pinyin'  		: ['nǐ','huì','xiě', 'shén', 'me', 'zì', '?'],
					'characters' 	: ['你', '会', '写', '什', '么', '字', '?']
				},

				'B2': {

					'english' 		: ['I can write \"you, me, him, all, good\" and also \"eat\".'],
					'pinyin'  		: ['Wǒ','huì','xiě','\"', 'nǐ', 'wǒ', 'tā​', 'dōu​', 'hǎo​', '\"', 'hái', 'yǒu', '\"', 'chī','\"', 'zì'],
					'characters' 	: ['我', '会', '写' '\"','你', '我', '他', '都', '好', '\"', '、', '还', '有', '\"','吃','\"', '字','。']
				}
			},

			"Conversation 2": {

				'A1': {

					'english' 		: ['The characters you write look very good'],
					'pinyin'  		: ['nǐ', 'xiě', 'de', 'zì', 'hěn', 'hǎo', 'kàn', '。'],
					'characters' 	: ['你', '写', '的', '字', '很', '好', '看', '。']
				},

				'B1': {

					'english' 		: ['But I feel hungry as soon as I write characters.'],
					'pinyin'  		: ['kě', 'shì', 'wǒ', 'yī', 'xiě', 'zì', 'jiù', 'jué', 'dé', 'è', '。'],
					'characters' 	: ['可','是','我','一','写','字','就','觉','得','饿','。']
				},


				'A2': {

					'english' 		: ['How do you feel hungry as soon as you write characters?'],
					'pinyin'  		: ['nǐ','zěn', 'me', 'yī','xiě', 'zì', 'jiù', 'jué', 'dé','è','ne', '?'],
					'characters' 	: ['你','怎','么','一', '写', '字', '就', '觉', '得', '饿', '呢', '?'] 
				},

				'B2': {

					'english' 		: ['As soon as I write chinese characters I want to each chinese food.'],
					'pinyin'  		: ['wǒ','yī','xiě','zhōng','guó','zì','jiù','xiǎng','chī','zhōng','guó','fàn','。'],
					'characters' 	: ['我','一','写','中','国','字','就','想','吃','中','国', '饭','。']
				},

				'A3': {
					'english' 		: ['I also want to each chinese food, I\'ll treat you to eact, how does that sound?'],
					'pinyin'  		: ['wǒ','yě','xiǎng', 'chī','zhōng', 'guó','fàn', ',','wǒ','qǐng', 'nǐ','chī', ',', 'hǎo', 'bù','hǎo', '?'],
					'characters' 	: ['我', '也', '想', '吃', '中','国', '饭', ',', '我', '请', '你', '吃', ',', '好', '不', '好', '?'] 
				},

				'B3': {
					'english' 		: ['Ok, great.'],
					'pinyin'  		: ['hǎo', ',','tài', 'hǎo', 'le', '。'],
					'characters' 	: ['好', ',', '太', '好', '了', '。']
				}
			}



	}	
}




