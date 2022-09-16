# ImageToASCII
Convert an image to its ASCII representation.

## Dependencies
* Python 3
* NumPy
* Pillow

## Usage
First, install the required modules (check requirements.txt).

#### Installation
Dependencies can be installed via the following command:
```
pip install -r requirements.txt
```

After the installation process, run the script. The script will prompt you for an image path and a scale for resizing the image. Entering the values will start the process and the output image and text file will be saved next to the original image.

## Test Run

Input:

![1623870867144-01 resized128](https://user-images.githubusercontent.com/66966617/190704437-91003afc-2349-48db-b3c8-b703c9d274d9.jpeg)

> Scale: 100

Output Image:

![ASCII_1623870867144-01 resized128](https://user-images.githubusercontent.com/66966617/190704501-e3ccdf84-ecd1-42fb-b0f3-6fa0b47b78f7.jpeg)

Output Text:
```
>>rrrrrr>>>>>>>>>>****>>*****>>rrrr^^;;;^^rrrr^^r^^^;;::""~~,,'',,,''''''''''''''''...',''''''''''''''''''''''''........''''''''
**>>>>>>***************>**???***rr^^;;;;;;;^^^^^;^^^^;;;__""~,''''''''''''''''''''''..''''''''''''''''''''''''''........''''''''
**>>>>>>*>>>>>>>>>***>>>>>**?***rr^^;;::::;;^^^^;;;^^^^^;:_"~,''''''''.'''''''''...'''''''''''''''''''''''''''''................
>>rrrr>>>rr^^^^^;^^^^rrr^rr>>**>>rr^;;::::;;^^^r;;^^^^^^^;:_~,'''........'''''''....''''''''''''''''''''''''''''................
rrr^rrr>>rr^;::____::;;^;^^r>>>>>>r^^;;;:::;;^^^^^^^^^^^;;:_~,'..............''','...''.''''''''................................
rrrrrr>>>>>r^;:_"""_::;^^^r>>>>>>>rr^^^^:::::;;;^^^^^;;::__"~,''..............''"~'..'..''''''''................................
rrrrr>>*>**>r^;:"""__:;;rr>>>>>>rrr^^^^^;;;:::;;^^;;;:__"~~,,'''................~,'',,''''''''''........................''''''''
rrrrrr>>>>**>r^;______::rr>>>>rrr^^^^^^^^^;;;;;;;;:::__",,,,''''................'..'~""~''''''''........................''''''''
?|?r;^>***?||??||?|\\\\/LiiccccliL//LL\*|??*>>r;^;;^;_""""~'',,..-.'.-.'-.''...'-.'''..','''''''-..''''..'''''',''...'''.'''''''
vv7L||/L7v1ttt}FfF]FFF]FF]]]F]]FF]]]]]FF{txx111zv7llciLL\\?>r^;_:::_~'..'''.----..'..'',--.''''',,''..''.',,',~"~~,'''..''''''''
}]F}{}fjFuy2yj2ayjujyyy2yjuuufffjyyyjj2o2yjjjjjjFF]}}FfF]]}txx111xxvllcL\|>^_~'.,'.--.'',~~,'.-`.....''''''..',~~~~,,''.''''''''
SSooSSSS2222juj2jufjSaaZoSyjuFFfuj22yjyS2jjjyyjjfuuFFySS22yjuuuufjjf]FF]]}t1z7cL;:~,,,''-.'...'''''''.-`''....'''',,,,,'''''''''
oS222yyjyjuuuuujuffjSaZZeeZoyffjyjjyyyySyjuy2yjufjj]}fuu2yjfF]FfuyyfFffFfFFFfF]}]{1lL|>;:;:~'',,--..'',,..''''....''''''''''''''
2juuy2SoyfFfjjjuufFujyyyZeea2uuyyf]Fuy2S2yySo2ufujjF}]]]jjuufFfj2ooyufff}}}}]]]]]]]]FFFFxt1c/|?>:",'..''....''..'''''...''''''''
2yyyyy2oyuFuyyjjoS2SS222aZeeo22oSuFu2oaZaS2ooyfFFFFffFF]FFfufFfu2Sao2juujuf]}}}]]]}}{{{}]fu]{{}{1vc\>:~'"~,''''',,,''...''''''''
}]uyyjySyufj2S22oSSS2yjj2oZZaooaojfyaZZemaoaa2fF}{}FufF]]Ffuf]]FfjSao2y2Syu]tt{}ttttt}Ff{FfF]FfFFF]}{17l*r:"~~~~~~,,''''''''''',
]Fuj22yyyjffyaZoaaSyy22jjSZZaaZZZSSoZmweeZZaSjF}tx}ff}]jffj2u}]yy2SaojjZoy]}tx]FF]}]]}]F{}]FuyyuufuF{]u]f{vi\r::__~''~,'~~"~~~"_
yjuuj2oZaaoSameaZa2ufjyjjySSaemmZaZa22amaZayff]{]{{]]}FjZ22ZXwmmwwmmeSya2yFf{{]]fffF]}{}t{}]Fujuffff]Ffff]{t1liL?>;""_"~""___::;
2yjuuj2oZZaSoaa22yf{{]F]FFFf2aeeZaZauFyZamZjfyyfjF{{FjoewE6$khk$9q$66EwXoouy}}]]]fuf}{tt}]]]]FffFfffufFuFffuF}ttv7i\*>^:;;^^rr>>
FffF]fujoSyuuyyjff}tx{{t]}{}fy22o2SojFuS2o2fFy2jjfFF2mk$$qOOKq9$6KKqq$hEXPZeufF]{Ff]{tx1}]]]]]Fffuffjf]ufujjufff}]}xz7i/**>>>>>r
{{{t{Fuyyyjuuyyyjjf]]ffFfF]]FfuujjoeSujSyjffujjuuyoZX6KOdHHHHHO9qR8HdOqq9K6keo2f}]]}{txxxtt{}]fjjyuuyf]uujyjfffu]fuf]}{{li\|?*r^
}]F]Fuufuujjyy22oSyuuyS2jufffFFFFuamoy2aoyuyyjuuSeE$KOddDDDHddKq$ddq9qqKqOOK6Xmy]}{}]]]]{{{{}]fuyyjj2jujujjuF]]]]ff]{{]]}xvlcL/|
fujujyu]ffujjjyyoo2yySoSjufffF]F]F2o22oaSyjyyuu2ewkqdHDRMd99ddqkqOOKddOOqOHKO66Z2F{}FFFffF}}}}]Fffuyy22jfuf]}}}}FFF}}}]]uF}{txz7
yyuFfy2jjjuuuuy2oaaooZaSuF]FffffF}}fjoaoSSSS2yoemmXkqd8gKKKq$69OqKqKDHq6OODqDqHhP2]]F}{}uF}{}{}]{{fjjSojffF{{}]]FFFfuyyjfF]]FF}t
2F{]F]FjuFFfuuj2oooaZZZeayyS2f]F]F]}]fyZeZo2y2oZPh66kk69q$66$9KdKKOdHHdOd8DMdHH6kPey}]Fx{xt{x{]x{]u2S22SFu}}FfuuFjufj2u]fuufffF]
ZSyjF{}uuFFfjjyooaZwwmeewZZZajFF}FF]}}f2maSSoZwh6$9999qK$6$9KKOdqqKdHHdOHRHRdRRHO$PZ2jf}]}}{{}}t}}Ffuj2Sju{}uy2jy2yuujffujjufffF
ZaoSyfuy2uffjj2oy2oZeeZemeeeZSjfuufFf]}F2juSeXkqOKKKOKKqq99qKKqq99KdHHdORRDDdRdRH9Peaj{t{}{t}]}}]}}FfujS2jttfy2ufufF]]]fuuuF]FFF
Zo2SS2yj2jffuj2Sjujy2oewZeZZao2yoj]F2yF}fFjaXE6KHHdOK96k66666kkk669OHdOODHHdOH6dDd6Xw2}tx]}{]]}FF]Fff]]F2jtxFuyufuuuuFFjffF}{}]]
eZooSyf]ufFfuj2oo2yyySePemeaoaaoay]fSojFy2ZPhh$KddO9kPmeZmXXwwwXPh$KOKqqKKKKqKhKdDKhPZu}]juFF}{Fjffuf}ttj2F}Ffyyuufuyuu2jjf}{{}}
ZmmeoyufFFfffuj2Zaao2SameeeaaZemeayj2yjyoZXhk69O$$6PeSyjuSeeZaZemP$KK9$9996$hkE$$KqkEm2F]ff]}{{}yuuyjf]F2a2fFFuu]]{}fuu22yu]tttt
aeweaSyj]fuuF]FfoaZZaSoaZZZeZZemmZ2jyjj2awhk6666EPmojF]]FyooSSSSZw6Kq6k$66EhmmXXkk$$kPey]{{{{]fFjuuSSyjySeojuFf]]F}]fjySjjf}tttx
eeeao2f{{FuuF]Ff2oewmZZemmmwmaoaa2fFj22SeP666kPeweSu]{{}]fuuujy22eh9$EPhPEmPaamaPmP6kPeyj]}}]yoyjujoojff2ZSy2yjFFufFffFfffF}{{{{
eeaSSoyF]fjF{Ff}}yaZaaemwXXmaS22S2f]jewZw6K9hPeSo2f}ttt{t}FfffujjehhwmmmemmZS22So2oe6$ewy{}}{uSafjyjy2u{fjy2SjF]yjyyfjj]f2j]F]}]
jSZeeeaSjjjf]uu]]uyjfuSZaaZaooS2SyufyaemhKd$wZSyyf]txxttt}]FFfuuyZPXeaaaooo2juuujju2m6Pwo]}}F22uujyyf]FjSoSyjf}]ffjyjyjfySj]Fffu
}uomwmZaSyjjuju]fuu]{]jojj2SaaooyfuSZmP6qdOEoufF]}txxxtt{}]FFffujoeZoS2222yjuF]]]f}FyEkmoFFuyaSf]ujFttfoZZoyjf]f2oaZa2uuSoyfuyyy
}]uommaSoyyS2jf}uuf]}]fjFfjoaaoojfuZXh$ddOkZf}}}{txxxttt{}]FFFfffyS2yyyjyjjufF]}{]{{Foheyf222o2fxFf{{uSSoaSyjfFfFj2oZ2u222juuyjj
]{}jaeZaa22SyjufuF]]]F]]]FjSoS222jyeE$qOH$eu{ttttxxxxttt{{}}}}]]]FuffffffFFFF]}{txxzt}wmyuS2jyu]xfjujoa2So2juF]F}uyoZSyajuffFuuf
]]]Fu2aZZS2yffjjuF]FffF]FFuyyufuS2Sm6OOKOEy}txx1xxxxxxxxxxxxxttt{{}{{{{{}}{{{{{{tz171zoPofjyj2jf]f2ao2y2SSyuufFffySZeaaeSjuuFuyy
FuuFFuSoeaoyuuyjuffjyyjuuffuufFfyyoX9ddO$wj}txx1xxxxxx111zzzzzzz11111111xxxxxxxxxvvv7v}maFFujSSSuu2Zayj2SSyujf}}ztf2oZwmo222uyoS
uyjfu2oowmeaSSSyffjSo2yy2uFfuuuujuSPqKqqheyF{xxtxxxxxx11zzvvvvvvvvvzvvzzvvvv7vvzvvlzL7iyefFufu2oyyy2oaS22Syuu}zlv1Fjyoeo2ySoyyoS
SaSu2emZwwmeeZaSjF2y2ayoSu]Fjjjyjfahqdq9$XSF{txt1xxx111z777vvvv7vv777777v7777lclvll7lLivmSt1t}Ffyfu2ao222jfF}17lvxxtjZaSSS2ufjyj
SoSySwhPEPwmwXauF}SoaZyoayFfSaSfyjekqOqqkXou]{ttxx11zvvv11111111xx1zzzzzvv77777lLilvv7iLS2}xtxt{]}}fy2oaoyy2yF{t{}{tF222aZZaaaSy
aaaaowEmk6kEEEZfyuS2SaoeoyFFSmZy22w69OqqkEZj]{txx1z11vv1xxt{}]]FF]{tx11x111zz1zl7liLillifoyfuFuujfFffuySS22SSj]t{FFFujujSaZeeZSj
ZoZeoeej2amXEEwaeoSufy2ZyuFfyaeZSSX69OKq6hmj}}{ttzv1t{fyoaZmwXXXa2f]}{{{t}}{]F]xv7cLilcLxyjfuujy2yjuFFu22oaooSj}}u2SSSSo2oooaao2
waZmZmZf}F2wEPXXEXmoyyj2uF]fuuyoySE$qdOqkhmj]]]{11tf2eE9HHDRRDdOkwSyjufFFuuu2emZj]zlciictaSFuyy2o2jF{t]uuaZyj2j}{fjujySZ222yy22y
Z2ySSS2]f]ueEPwmPXmo2yuftvv{]{{}f2h9qdK96hmyF]{x1FZkKdDDMMWWW8DdKhZoS2yy222Sm6OddkaFzi/LxZ2{]ffFuf}x1t]uuoau]F]xtfjffuj2yyyyyjuf
f]}]FF}t{t{jooS22yf]]]]}z771tx1z{26KKOq9qhZj]}{{um9HDDHOdHDDRDHdqhweZoooaaZwhKDMWMD9wuv/{XeFjyuFzvvzt]j2y22yfFFFFoayyyjfjjjyyjuf
]FFu22jjjjuuF}tx}]{}Fff]}}}{{tx1{oKDddKqqPSF}}FjhqO$kk$$$$9qKKqq9kPXmZZmeewh$qdD8gN8d6a]tPmFfu{1zzz1t{{{]{]ujfuSyZoF]fF{{{{{}}{{
uS2Zwo2SoZZZayujyyuf2ZZSuySoSS2ufmKDHKKOqmu}FFuXhhPXEhk99qKKdHO996hEXeemXeP66qHKdHdOdd$XFPeFFujy}jj}Fj]]}fyuu}fSy2jo2yuuufj]F]Ft
yaamw2uju2SZeoyyoooomEXZSammeZZSuwKHHdOK9af]FfjmPwemh666hh69Odddq6hEXmmwXwh9KdDddK9$996ke6ZfoXXe2emSoZSoSeXwXaaXewePweaoSSZSS2oj
yZmXw2jufjSZwe2ySooawEXZSoemZZa2jwKHHHdK$y]]]fjayZPk$669qqKHDHHDO$hPwZaZwP$ODDHO9qK9hXXhm9muaPPwSmXaZmameEkE6wmkwPXhXmeZaZXmmewa
joZXwo2yySoewZyuoS22ZXwZSSZeaoo2uXOHHDHO6u}F{FyomPh9dKkXEk9OHDDRHqhwouFfohOHRDO9qhwE99wyS6muommZyewaaeamZhhwkeZ6mPmPeZZZoZPwwmXZ
jy2ZZoSj2SSoZSuf2yufyoo2uuy2yjjfFXdRDRDdhF}F{FSZw$ddK9ORgBBWR88Hd9EZut11fhR888HqEEwmE6hejhmyZPPeSmXZemawZhhwhZZ$mPXEwmeeaZPXwmwZ
2yjSS22fujj2oSjjyjuffjuf{xt}}}}{FXH8RRDHEF}F}uamk$qdMgNB#QBRHMWR$EmSFxvv{PMgWNN8MOPZPq$m]EXySeme2ZeoaZSa2wPmPooEePXhXweaoaweeaeS
aSyoSSofffjSmmaaeZaS2yyyF{t]FfufuXdM8RDHEF}FFjomhqddddDW#BgHKddqEmoyFtv7vodgMN@BB#R9k6kXxPXjujyy]fuFjyfju2o2ajyZomamaaSyyyoyyj2f
eaoZaaZjujyehhXwPXma2y2Sj]}Fuy2y2XO8MRDHEf{]Fj2awXwwh69OHDDOKOK9PZyjf{vli}kRD8BB#gM8ROhe{Xmuy2u{1t{tfj]fuuju2uyooZ2SjyyuufjFF]f}
XemmamwSyamXhkEwmwZZ2aaZajFu2ZeaaeKMMMRHEF}F}Ff]ujy2oePk6$669K$E2yjf]{17cvuhKOdHDDqEPkEZ1ww]yyff]tx{]fySoS2SSyjjyZZ2y2yuujjyyjuf
wZZaSePeZmXPhkPeoaoZoZaemSuyomma]}mHgWDDX]{]t{}tt{}FjSeXXEhPwayFufF]{xz7ccxjekKdqKkajuf]lo2{fufuu]}]FFjSoSSo2jufu2yjySSoaoooSS2y
Zoao2ZPXwXXPPEwZ222eZeZmwojyoeeoFt2kH8Hde}{}1xxzvzz1x{FufujjufFFFFFF}tzv7c7t]uSZXPXou}t1iu]{FFfjSyjjufjaooao2f]}FFFuSaZmmeZaaaoo
22oo2awwXXXwmmeZS2yeemaemoyy2aa2aZmePOdKa}{{11zzzvvv7vzz{x1xt{}]}}]]{17ll/c1x1t}{{{{xvcLi]{Fjj2ooSoZa2SeZaaoyF{t}Ff2emmmmeZaZZZe
y2oS2SZeXPXmZaZea2jaZmaaZo222ooyP$6oShqqy}}{11z111zvvvvz11xttxt{uF]}tz77vci71t{1xzv7lcclLx}yaameooZwweZmmZao2u]}]j2owEXweeeeemmm
2S222oZeXXwZoSoao2uSoZSooSSSoaojPkka2Zmhf{}t1x1xx1zvvvvvlzxtt}fyyF{x1vvzzvcLvfuz1zv7i//Lizj2eema2oemwmeeweZao2juuoZeXEPPeeeeeeee
22yyoZmXXweZoSSSS2j2yS2S22SaZmauPXe222ja]{}txx1tx1zv77771t{{]joa]xvz1z1xvzvilFSj}{t1vcL/cvZyeeeyjoeZZemmXmeZaoSS2ZmXPXXPeeZZZZee
jyj2eXXEXmeeeZoS2S22uyy2S2SZwPeuEey]j2uy]{}txtx{x1zvvvzzxt{foXmotzztFFFFuF}vL7jwoutzzvc\Lcmjewm2uoeoSZwXXwmeaSSoSeXEEmeXmeZZZemm
2y2awPXwaaaZeZooySaa2u2eZaZwXPeyPm{2hy]S]}{ttt{{txzzvz1t{]uaPEmofFf2oooaZo2jf1{6wajF}17iciZjXPZa2oaoSoeXPPweeaSoZmXPXmmwXweZemmm
ZaZmXPwmoSoaZoSSy2aZo2oeXmwPPPeywa]okotof]{t{{{}{tx11xt}fyZPkEmeoawk9$kEPwXPPoykhXayu}1licafePmeoZZZoaZmXPXmmZooemXPwmemPweeemmm
wwXPPPwe22SoaS222SZmeZZwEPEhEEwoe2]oPo1w2Ft{}}}]}{{{{}]f2ZE6hmZeE6KD8RO$6kqOKEeh6kXZSj]1claFowwwZemmeZZeXPXwweaammwwwmemPweZZeee
XPEhEPmZSSSoooSSaaewXwwXhEhhEEPmSj}awSxkZu{}]}}F]}]]Ffj2aXkhmoSoP6KdddK$66KqhmaPk6kXeoj}z7SuoemmeemwweZeXPXwweZemeemwmmmXweZaZZZ
XEhhEPwZooooooaammmwXXXPhEEhEEEPju{ZZf{$X2]]F]]fFFFuuySZXk6XaS2ySmhk69996h6PZ2Swh$9kXmSutlyyaaZememXXeZePPwmmeemeZZewwwXXweaaaaZ
PhhEPXmZaaaSSaZeXwmwwXPP6hhhEEhEoFzuFx]9kZuFfffuuuujySamk6kmoS2ujaXEhk$99hPeZSSX69K9kPay{cuSaoaZweeXwZaeEPmZmmmweZZmwwXPXwmZZZZe
EhEXwwmaaZaooZemXwwwXPEh6hhkhEEXwtvxz1fKqPSuujyyyyy22SZX6hXmZSyu2oeXXXPhhXZSaSyX99qq9hZy{7jaaoaamZZwmoamPwZamwwwmmmmwwXPXXmeZeem
EEPmmwmaaZZaaZmmXXXXPEkkkEhkhEPwXvxttFjKdkZyj222SSSSSoeX6PwXwojjjjyoaaaeaojfyfFm966qKkZy{z2eooZaeaameoawXmaamXwwwwwwwwXPXXweeemw
XPXeZZeeamZoZaawwXPPEkkhhEEEEXmea1t{]jykOkmSyaeZSoSSS2aPXPhhwSujujySZwXwaoS2f}FyPk$96EZj}1Sa2ZaaaoammmwPPeoZwPXeXXXXmmwXPXwmmmXP
wwmZZZZZZeZaZemXXEEEEhkhhEXwwmeZa7lccxf$q$Po2ZmaeZSSS2aXhhEEwZewEh69KOK9qqKO9EXP9$66hmSu]{yZSaoaaZewXPPPXeaZwPXwPPXXXXPEEEPPEPXw
eZaZZZZemeeeZmwmXEhEPPEhPXmemmeaei/v11{EqqkZSemameo222owPh$OOKOddOq$kkEXwZaZeXkq9hPPwajuFF}aaZooaewwPhEwwmZZewXXXXPPEPPXwmmwPPwe
eaoaZZZmmZmwZeweXPEPwwPEwwmeeeZaZ1ztx{j9OOkeZmmZeeo22ySeXh9OK6PXaoyuuujuF}}}]FjSweZeZSjuff7yZmaoZewXEhPwwwmZZemwXXPPEEEEPmZaZeZa
maSoaaZmZZXPeewmXPPXeZewemmZaZZZe2yfumhqDd6wmmZeeeZS2y2ZXwwma2uufujySoao22yjF}{]jSaZZo2uj2z2ZeemwmmXEPXwwXwmemwwXwmeemXEZSu}xzvv
weaaoaZewXhEwemmXXXma2SaoaaooewwXaZoSaw68D$EPwZmmweao22aZa2jujy2ujy2SaZZmeojF]Fu]2emeZSuSeuZZZwEPwwPPXwXwPPwwXXwPXweZooSuF{zlLLL
mmmZZemmPhhEPwwXPPXmaSSooaaoZmweeoou7iFhdRO6kPmXXXeaZaooZoyfffuujy2SamPhXwmoyF}}FyZmma2jawZmeZXEXXXXXXXXwXXwwXwemZo2yu}xiiiL/\\/
ewwmmXPXwEPXEEP6hhEPwZZemmmmwwajZojxv}uu$DH9$kXPPXZaeeaaaSjfFFffj2aemXPPEPwZSjF}FuSemo2yeweemmXwwXPwwXXwwwwmwweo]xcLicL/\\\\||\\
2aeZeXEPXEPwwXPhEhkhPwwPwPmEehZjZuyiczf2O6MO9$EEPeoaZZaZoSyuffuuujSZwXXXwXwZ2f]]uuywZyauPwemmmwXXXwmmwXXmy{t{ttxcL|**???|||||\\\
ewwmmXXwPEPeeemPPEkhEPPEwkwSjeaeZ2zviLFy$$8D$9EhEmooaaaaoSyuufuujy2oZeeeeeea2uFF]uooeajmmwwwwwPPemwwwmoytl|?\\|\L/|???????||||||
mwPPPEPwPEXeemXhXPPXwwXPPeZoaeSe2xlciv{jaEqRqK$$kwaoaaoaS2yjuuuuuujjy222yyjuf]}}]uo2oo2PZwXwZaoS}{{}fuf}l/**??????||???*?????|||
hhEXwXPhEEXemmmwwXwmmXEEejXXXXZy}cvLt]f]FowHDdOK6XZoaooa22yjuuuuffFFFFFFF]}{ttttFuuSyyeyFyoy]tzl|?>*L7vvi/\|||||*?||????????||||
{fomXXPhEPmeXPwmwXmemPPXfZ6aawa}z1vxj{a]]uo9Wddq6Peooooo2yjuufffFF]]]]FFf]{txxt{]ffSSS2l7x{1li/|>>rr*||?|???*>>*??||?????|||||||
/7}ju{zvt{{FawwwEEXeewmofXwuZaf1711uf]22]]jP8HDq$hmaooSS2yjuufffFFF]]FFfuf}t11xt{FyjZol|illL||\\*??*>**>***??*?|\||???|||||||\\\
?*|//\\/il71fSoaooyu2mXeoSjoe2j1zz{]]uj2{FFo9DRdK6PeaooSS2yjufffFFfffujjjjf}txxt]fS22t>*??*r^^r>>>>rr*|\>***??|\\|??||||||||\\\\
r^*LiL\\Li/|\\????>?zoEheuyPjjE]xF{tj]ZxtuFuwDHddqhweaoSS2yjuffufujyyy2SooSjF}}}ju2Z{>?>>rr*?*>*r>***?*>????||\\\|??\\\||||||\\\
***>>>>>?>??>**>*_*vmkkP2hwo]t6ojSyj]1FuohFuyED8DdqkXmZZaoSS2yjyjy2SSoaaemma2uufyoa]^>?>*********>r>>r>****??|\\|||||||||||\\\\\
*****>>>;/>:|*:?^>za$kkS2Eot1{FOqh$o}f{2$$}uyZ98RHdO$EwmwmeZoSSoooaZemwXwXPXZ2SaZaqu?|^*>>>rrrr^r^^rrrr>>***???|\\\\\\\\||\\\\\/
*????**>>?*>>*>r|cwkPEmjwo]j{ileqmXjzjj$MO}ujyPd8DHDDK$kEPXwmZeewwwwXPPEkEhkEwmXEqMh{rr^^^^^;;;;^^r>>rrr>>>>****???????|\\\\\\//
||||????\r*|>>?r7ak6Xwk22u]xlvo]kX2S{uXRgRFFu2mhDdKdRMRO$kEEEEPPkkkhhhkk99996hh6X8WREir^;;;;;^^^^^>??*>>>>>>>>>>**>>>**?\\\\\\\\
|||???||*\>>\r*1aE9meXyySyjx}}uSm$oeyZqRgMF]u2am69qqHWg8DK$6$999KOdOKKKOKHDK$$9$2R#Mdor>;;;^^^^^^r>??*>>*****>>>***>**??||\\\\\\
|????|||\/\\|\1ZPqeZoFfomOXaZmuxu6muy$DWBM]]jj2ZekKKORWgNRK9qOdd88M8DddddHO9Kd$mF#NMM$x^^^^^^;;;^^r**>rr*******>*****???||\\\\\\
??|\\\\\c\LiLxaPEXa2j2yh9ko$qEm2jKEfad8NQW}]jujaZwkqOH8gg8HdddHD8RDHddKqdOqqdOwFy@NgNOX\rrr^^^^^r^r>>rrr>>*???*****???||\\\\\\\\
?|\/L//\ic?|t2ZXkwuf]2u{muwXKOXEFKEo$DW#BgF}jyySZoZkKdHR8888RDHDOq$9KOKqqdDDOhS}mW@WgRqtrrrrrrr>rrr>>rrr>>*???**|||\\\\\\\\\\\\\
i/i/|/\**>/]uoeEPZ2]ou]tuF9q6qw9ZwOoq8WNBgf}fjySSoawh9KKdHDR8888HHHOOOddRRROPofth#Q#WRHP?r:*|^rr*^^**^r?**>*?|||\\\\\////\\|\\//
\|/?>?>>*?zfeZmeaSjSaokuZ9eOqhK$PhdEHDRgBNf}fjj22SaeXE6$9qOHDR88DDHdHDDHRdqhZyFt$#B#gM8$}Lr;rr||>>*?***???|\\||?||\\\\\/\///////
|?\?*|*?>lu2a2aoSa2emPREoZ$aEoe6NH$hHRWQQNF}fjjjySaZZeXEEk$KdHDRDDHHDRDdO6XZ2u}tdB#NNWWdPtv\*>*>?\|>r>??>*?||??|||||\\\\//LLL//L
\|/|\\*|i]2ayo2o]2aeXEh9SywhKOE6XeyEdD8gBgF}ujujySoaoaZmwPk$qOddHHHdOOq$hwaS2u}{WQ#NNMMDKSZut7L|>*|\/\?r??????\\||||\\\\/LiciLLL
/\\|\|r|fo2aZXSjtue66eZ6EjakPkjfFoadDRW##gF}ujujy2oaaaaaewPh6$9qKOOq96hPeZS22f}F#Q#NNW8Rdm6hwZj]zL??\\\/\\\\\\\/\\\\\\\\/icllcll
iiL\/\?lSZeSwou}aomd6yEEPy}aouESZXwOKH8gNWf]ujujy2SoaaaoaZmXPhk6$99$kEXwaa2jj]}y#QBNNgM8HXXhh$EwmFc/\||\???|\/\\/////LLLLcl77vzz
illLiilf2Ze2S]Fy6PX6Eyhe6u]jukZewwwOHWWgNguFuuujjy2SoaaaaZemwPEhhkkhEPXmaayjj]FaNBBNNNMMDkZPP6EEXof]]xl/cL\\\//\//LLiicclll7vvzz
\ic/Li1Z2ajjujjP9$6w9PwZfFaoEPXaXwPKKD8NNNjFuffjjjy22SaaZeemmXPEhhEEEPwZoayjyFfmNBBgggMWDKmkPhXPwZ2ySZaSu}viLL////Licll7v77777vv
/i7/LL}o2fF2mPk9$$6Ee2jjoZZXk6amEEh9ORM8gWofffujjjy22SoaZemmwwXXEEEEPXmeooy22]jkRB#gNWWWROmOKOOdOhwfoSXmXXo21liLli/7clcz77777vvv
/LLLixF]j]FZqHqh6hwSff2ZZEX99ZwPE$OddH8gggeuuujjjjy22SoaZemwwXXPhEEEPXmeooyy2f2kDB#ggWWWDOmq9KdDq96kZyyZoeZmyFxcLv7lllzc77777vvz
L\/v7]]{moyah$EeufFfyaZePwKkkEkRNDhhHMRHWgPyuujujyy22SoaZemwXXPEhhEEPwmeoa2y2ya6H#NggWMM8HP$$$KHDRkwa6Emwhkq$kwjvclczl7lllll7vz1
/\L{}]fa$6hwZSjFjySePPwemEkEEhHd9Oq$OdDNMg6Suujujyy22SoaZemwXPPEhEEPXweZoaSy2ow6OggWgWWMWRk69$9KORWHPoe6OKkEP$d9SvvL7vLvcccclvz1
\\/1aomODOkZjfjy2mkEZow$$dOHOHDq9$EhH8D8MgKZyj2yyy22SSoaaZemwXPEEEPXwmeZaZaSoeP6KWWWgWWW8HkhKq99ddRMHEZaXk6kh6O$ha]vivcccccllvz1
\\/zE9ORdhSff2ZmPwwhODd9$6Od9dkOOKkh9Od88WHwoy2yy22SSSoaaZemwXPPPPXwmmeZZZZaeXhkKWWMWMWWMH$PHO9$9dORdDkewh6hh6RRk6uy1L7clll77vz1
\\vykq$hZ2u2ZmmmmE9KOq99kKEqO6OD6669OHDDR88kmSS222SSSooaZZemwXXPPXwwmmeeeZemwPhEOWWMWMMMWD9wHdKqOKKMWR6XZX6$9$DH6EZw2v7v7777vzz1
/Lu9hXouuu2ewXE6OKKq99996$9EKq$Kd9kk9dDDMMgqhZao2SSSooaaZemmwwXPPXwwmmmmeZmXXEhEOgWMW8MMMH9mDDDDqOD6R88EXPkk$6DHqPqwe2v7777vvvzz
juwk2Fy22ymZhKOdO9O$qKEKOmq$6OOqKKqPkdHRM8WRkwmZZaoSSSaeZemwXXXXXwwwwweZemXEEXXPD8MM8MMMWHOXOdDHRD$R8dgdhEkkkh8RkPhdEeu7c7vlv17v
jyujS2yaoXOOh9q69Kk9dKKkqd66$9OK9k99qdO8RRMMKEmeeZaoSSoZZemwXXXXXXwwwmeemwXXPPwED8M88MMM8DOwK8RK88ROMWK8qXqk$ddDdXm6$9Ey1cl777lz
tjjuSaZEOdkq9kEd96dkhH9qdOqq$9P$O$qKqKd88R8WR6wmmeZaS2SoaZmwwwwwXwwmeeeewwPmmmZhR888R888RDqP98ROM$8d9WWNHq99qO8HOEEk6$qhy7lv7llz
yjySeh99qqk$kOHEH$6HqhqH$6H9PH9hKqKq$qHD8M88MKPXwmZao22SoaZeemmmmmmeZZemPmXZZaoqR88RRR88RH9khdHMDMHKdH8MRDqq99WDOEkh666PXFvc7vll
oaX6$99$mO6EOq9$OKqddOH6M9hDdX9Kk$qK9qddDM8RMD$PXmZaS22SSoaZZeeeeeeZZZemXZeao2m8DR8RDRRRRd$6EOHWdgHRMHMHMdD9kHHRKE$h66kPEmfccvic
Z6KKKhX9Khk$qPqH$OR$6Rd6OWHhO9qh$q$KO9KDDMW8M8qPweaoS222SoaaZZZeZZZaaZZemoSSuuPMHDRDDDRRHd9hPDRH8dR8dRN8MRHO9R8HKk9hEkh6E$X{llc7
KKhwEkk$6O9hOd$OOdkDHXKD6Od6dH$O9H9qd9qDR8MM8ROkweoS2yy22SooaaZZZaoooaaaoSuj]j9DdHDDDDRRHOqhPdRHMW8ODDKgRgdDqdNDOkkEhqhh66qZzlvv
6h$kmkKP$q99qH$DDHKHRK9ddD6DqkKKXDK9DdKODdR8R88dweoS2yy222SoooaaaoSSSSS2jyFu]o8DOHDDDDRRRKK6P$HMHHMgRH8MHD8OEdDMPhKqE$Pq9Xqktl17
Ph6hqhkKKXKd6qHdhdREOH$HHRDKDdhdRmO89dHKdHR8RRRR$e2Sjuyyy22SooSS2yy2S2yyff{{FEKddDDDDDDDKD9$k9DK8NhW8DWd8DM6qMM8Dk$q$6$OEhd9ovvv
$PEkK9q9Kd99RD$8HDdHH9HKEDq9HHHOqMOqDO9KdHRRRDDHKXo2jujjyy2SSS22yjjjjuuu]F{]Z8$WOdHHHDDHOO9969RRRHgM$RMd8D89Odg8dE99qkqdkkqKe}1z
PhqEP9HhHq6ddH9R86RROd8dddODdKDq9DHdDDDdHHDRRDHdO6e2yufujyy222yjjufffFFf}xF]R6DHdHDDDDDHHKq$hEqd8$WDDRqWRRHHKqN8h9HqPqdO$k$dXStz
khKK$hKH9qHHwDW9KdDhHdPODKHHHHO889WMO8HOdHHDRDHdOqX2yufjujjyyyjufFFFF]]]{f}HOODdHDRDDHHdO9q9$6dMODDK88HRRRd8$Og8Hk6OqOqO$69Ohefz
$666d9KHKdKD9HdRD8RDRKDd6DD$D8qWRHMHRMqdddHDRRHdOOkZ2uFufuujjjuff]}]F]}{t]6dHdDdHDDHddOOK9q$$kHRHDD8Od8ORd8H9dg8D6KKOqOH$$dq6Xox
hO9w9OK6HOhDRK$8DEdR9$RKKHH8DKDdKMHK8MDOOOdHDDDHdd9PajffffffuufFF}{}}{{t{XD9HODKdHDHHHdOKKq6kmKqRdORRHKRROgqdqNR9dOOE8HO9qDq$Pwf
K9KqK6qHqHOK9DM$DHR$RHXDHqKWROMDRRRRHD89OOddHHHDHdK$wSjfFFFFFF]}}{{{tt{]mDDdOd8KdHDHHHddqO9q$ZD8q8D$8MdRHH8OH$gMM$XHKgOqKqdO6EPZ
$hqq$6HHKHHDddWHH8DKRDDOOMOhRRkR8$8MDW8MKOddddHDDKOKheSffF]]]}}{tt{txt]jH6dHh8dddHDHddOKOd$K$jO8OH8DR68MOWKWO68gHhR$8$DOOqKH6hPX
```
