import tweepy
import csv
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
csvFile = open('result.csv', 'w')
csvWriter = csv.writer(csvFile)

CONSUMER_KEY = 'RehL1nN2zxQzAHOifTQ0TSOjC'
CONSUMER_SECRET = '9riZORBi0hdVCipVdCieGsLZb7jmfXYE365TZ2Y4ZbHuK8iGDo'
ACCESS_KEY = '127129573-BtivR613ehnhclu762jj19fLnRyPoZUCcBNFTHGw'
ACCESS_SECRET = '76WFU22aYL2DcrG16R42GVBWvEySSuEiPZYCSvgIDAx2r'

auth = OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
api = tweepy.API(auth)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

#header of the csv file
csvWriter.writerow(['id','Id_str','Screen_name','Location','Description','Url','Followers_count','Friends_count',
                    'Listed_count','Created_at','Favourites_count','Verified','Statuses_count','Lang','Status',
                    'Default_profile','Default_profile_image','Has_extended_profile','name','bot'])

class TweetListener(StreamListener):
    # A listener handles tweets are the received from the stream.
    #This is a basic listener that just prints received tweets to standard output

    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (status)
#search
api = tweepy.API(auth)
twitterStream = Stream(auth,TweetListener())

users=['@jainayushroxs','@lsarsour','@Vedanad','@tamannaahspeaks','@RED','@owlcity','@BestProAdvice','@KimKardashian', '@ParisJackson',
       '@Pink','@Maisie_Williams','@PochoLavezzi','@AksharaHaasan1','@KAKA','@neymarjr','@iAmNehaKakkar','@owlcity',  '@Gary_Kirsten',
       '@ParisHilton', '@JoshRadnor','@SonuSood','@ArvindKejriwal','@saurav_mawandia','@garvit_kothari','@sachin_rt','@LeoDiCaprio',    '@Tesco_Bengaluru',
       '@facebook','@devaldayal','@GreenDay','@maroon5','@AvrilLavigne','@StephenAmell','@Twitter','@davidguetta','@katyperry',
       '@ishan_handa','@xtina','@Uber_BLR','@SushmaSwaraj','@TwitterU','@nk_neeraj','@murarkanilesh','@narendramodi','@BeingSalmanKhan',
       '@agarwalsays', '@mridulpatwari','@sidharthaT','@agarwalgaurav81','@Bishwajitcool']
bots=[ '@lutadorCesar', '@fslhggi84', '@rodinho1mj', '@hLap3x', '@X4Qj4MjkTykVkPr', '@lowindyGG', '@Lil_HoszyHQ','@Ruffy3020',
       '@brontak994', '@Astfta2', '@MiguelCoCPKM', '@herry_ayco', '@sahzh92', '@testfollow5555', '@thestyleroom12', '@gb_lusho',
        '@tutorial1gamer1', '@ZAKAriaMEJ99', '@zacharysilva66', '@ramzykhattel', '@Fagust_channel', '@Followinges', '@filesroom',
       '@Hubbqtzaxe', '@girl0p9', '@Bestmotivatio10', '@InfoSawabali', '@LilMizzUniquee', '@mrmochawallace', '@asuntopoliticoa',
       '@UNlTEDNATlON', '@lrobertsonus', '@nine_likur', '@7Shadabshaikh', '@KentKiankent', '@camiloopr', '@baguspriwanto1',
       '@girl0p9', '@ramkaranyadav22', '@rezasitepu23', '@disabledaccant', '@tlulu_33', '@Jung26517696', '@Ayu_EIo',
       '@ThisTabletTech', '@Casimematas', '@faiz_salman_', '@ManasRa04856477', '@cyberkill6','@lupat_4pat']
for user in users:
    userDetails = api.get_user(user)
    csvWriter.writerow([userDetails.id,userDetails.id_str,userDetails.screen_name,userDetails.location,userDetails.description.encode('utf-8'),
                       userDetails.url,userDetails.followers_count,userDetails.friends_count,userDetails.listed_count,
                       userDetails.created_at,userDetails.favourites_count,userDetails.verified,userDetails.statuses_count,
                       userDetails.lang,str(userDetails.status._json).encode('utf-8'),userDetails.default_profile,userDetails.default_profile_image,
                       userDetails.has_extended_profile,userDetails.name.encode('utf-8'),0])
for user in bots:
    userDetails = api.get_user(user)
    csvWriter.writerow([userDetails.id, userDetails.id_str, userDetails.screen_name, userDetails.location.encode('utf-8'),
                        userDetails.description.encode('utf-8'),
                        userDetails.url, userDetails.followers_count, userDetails.friends_count,
                        userDetails.listed_count,
                        userDetails.created_at, userDetails.favourites_count, userDetails.verified,
                        userDetails.statuses_count,
                        userDetails.lang, str(userDetails.status._json).encode('utf-8'), userDetails.default_profile,
                        userDetails.default_profile_image,
                        userDetails.has_extended_profile, userDetails.name.encode('utf-8'), 1])
csvFile.close()