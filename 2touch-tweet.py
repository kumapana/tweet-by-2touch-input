import sys
import tweet

ツータッチ=sys.argv[1]

文字リスト=[['0','わ','を','ん','゛','゜','6','7','8','9'],['E','あ','い','う','え','お','A','B','C','D'],['J','か','き','く','け','こ','F','G','H','I'],['O','さ','し','す','せ','そ','K','L','M','N'],['T','た','ち','つ','て','と','P','Q','R','S'],['Y','な','に','ぬ','ね','の','U','V','W','X'],['/','は','ひ','ふ','へ','ほ','Z','?','!','-'],['','ま','み','む','め','も','￥','&','','☎'],['小','や','(','ゆ',')','よ','*','#','　','♥'],['5','ら','り','る','れ','ろ','1','2','3','4']]

小文字リスト=[['','','','','、','。','','','',''],['e','ぁ','ぃ','ぅ','ぇ','ぉ','a','b','c','d'],['j','','','','','','f','g','h','i'],['o','','','','','','k','l','m','n'],['t','','','っ','','','p','q','r','s'],['y','','','','','','u','v','w','x'],['','','','','','','z','','',''],['','','','','','','','','',''],['小','ゃ','','ゅ','','ょ','','','　',''],['','','','','','','','','','']]


ツイート文字列=[]
小文字モード='オフ'

for イ in range(0,int(len(ツータッチ)),2):
  if 文字リスト[int(ツータッチ[イ])][int(ツータッチ[イ+1])]!='小':
    if 小文字モード=='オフ':
      一時的な変数=文字リスト[int(ツータッチ[イ])][int(ツータッチ[イ+1])]
      ツイート文字列.append(一時的な変数)
    elif 小文字モード=='オン':
      一時的な変数=小文字リスト[int(ツータッチ[イ])][int(ツータッチ[イ+1])]
      ツイート文字列.append(一時的な変数)
  else:
    if 小文字モード=='オフ':
      小文字モード='オン'
    else:
      小文字モード='オフ'

ツイートテキスト=''.join(ツイート文字列)

tweet.tweet(str(ツイートテキスト))
