#!/usr/bin/python3
#
# Welcome to the Python programming challenge
#
# In this challenge you will need to demonstrate the ability to process a data using Python.
#
#
# You have got two dataset LOGINS_DATA and COUNTRIES.
#
# LOGINS_DATA is a string which contains tab-separated lines with the following structure:
#
# timestamp | app_name | number_of_logins | country_id
# Lines are separated by \n
#
# app_name is an app name, e.g. "Facebook", "Instagram", "YouTube".
#
# number_of_logins is an aggregated number of logins for every app.
# LOGINS_DATA may contain missing values. You must replace them by an average of logins
# for this app.
#
# country_id is a reference to COUNTRIES.
#
#
# You need to calculate an average value of logins for every company per country.
#
# Maximum time: No limit.


LOGINS_DATA = '1522207092\tFаcebook\t613\t3\n1522207092\tInstagram\t993\t1\n1522207092\tYouTube\t102\t3\n1522207093\tFacebook\t334\t1\n1522207093\tInstagram\t442\t1\n1522207093\tYouTube\t503\t1\n1522207094\tFacebook\t442\t3\n1522207094\tInstagram\t925\t3\n1522207094\tYouTube\t\t3\n1522207095\tFacebook\t546\t3\n1522207095\tInstagram\t774\t1\n1522207095\tYouTube\t682\t2\n1522207096\tFacebook\t242\t1\n1522207096\tInstagram\t72\t2\n1522207096\tYouTube\t438\t3\n1522207097\tFacebook\t16\t1\n1522207097\tInstagram\t284\t2\n1522207097\tYouTube\t464\t2\n1522207098\tFacebook\t894\t3\n1522207098\tInstagram\t525\t2\n1522207098\tYouTube\t541\t2\n1522207099\tFacebook\t694\t3\n1522207099\tInstagram\t114\t3\n1522207099\tYouTube\t536\t3\n1522207100\tFacebook\t164\t1\n1522207100\tInstagram\t973\t3\n1522207100\tYouTube\t615\t1\n1522207101\tFacebook\t770\t3\n1522207101\tInstagram\t160\t2\n1522207101\tYouTube\t351\t1\n1522207102\tFacebook\t114\t1\n1522207102\tInstagram\t784\t1\n1522207102\tYouTube\t376\t2\n1522207103\tFacebook\t357\t3\n1522207103\tInstagram\t421\t3\n1522207103\tYouTube\t599\t2\n1522207104\tFacebook\t398\t2\n1522207104\tInstagram\t202\t2\n1522207104\tYouTube\t417\t3\n1522207105\tFacebook\t506\t1\n1522207105\tInstagram\t393\t3\n1522207105\tYouTube\t12\t3\n1522207106\tFacebook\t851\t1\n1522207106\tInstagram\t4\t2\n1522207106\tYouTube\t880\t2\n1522207107\tFacebook\t149\t2\n1522207107\tInstagram\t894\t3\n1522207107\tYouTube\t926\t1\n1522207108\tFacebook\t987\t3\n1522207108\tInstagram\t864\t2\n1522207108\tYouTube\t478\t1\n1522207109\tFacebook\t338\t3\n1522207109\tInstagram\t504\t3\n1522207109\tYouTube\t816\t3\n1522207110\tFacebook\t423\t2\n1522207110\tInstagram\t302\t2\n1522207110\tYouTube\t506\t1\n1522207111\tFacebook\t317\t1\n1522207111\tInstagram\t178\t3\n1522207111\tYouTube\t174\t2\n1522207112\tFacebook\t111\t1\n1522207112\tInstagram\t691\t3\n1522207112\tYouTube\t\t2\n1522207113\tFacebook\t108\t2\n1522207113\tInstagram\t462\t1\n1522207113\tYouTube\t727\t1\n1522207114\tFacebook\t295\t2\n1522207114\tInstagram\t790\t3\n1522207114\tYouTube\t428\t2\n1522207115\tFacebook\t26\t1\n1522207115\tInstagram\t875\t1\n1522207115\tYouTube\t846\t1\n1522207116\tFacebook\t475\t2\n1522207116\tInstagram\t963\t2\n1522207116\tYouTube\t811\t1\n1522207117\tFacebook\t655\t1\n1522207117\tInstagram\t521\t3\n1522207117\tYouTube\t193\t1\n1522207118\tFacebook\t524\t3\n1522207118\tInstagram\t216\t3\n1522207118\tYouTube\t598\t1\n1522207119\tFacebook\t988\t3\n1522207119\tInstagram\t563\t3\n1522207119\tYouTube\t612\t3\n1522207120\tFacebook\t402\t1\n1522207120\tInstagram\t294\t1\n1522207120\tYouTube\t795\t3\n1522207121\tFacebook\t658\t1\n1522207121\tInstagram\t52\t2\n1522207121\tYouTube\t862\t3\n1522207122\tFacebook\t924\t2\n1522207122\tInstagram\t409\t2\n1522207122\tYouTube\t754\t1\n1522207123\tFacebook\t694\t3\n1522207123\tInstagram\t796\t2\n1522207123\tYouTube\t462\t3\n1522207124\tFacebook\t586\t2\n1522207124\tInstagram\t968\t1\n1522207124\tYouTube\t412\t2\n1522207125\tFacebook\t166\t1\n1522207125\tInstagram\t80\t3\n1522207125\tYouTube\t702\t2\n1522207126\tFacebook\t979\t1\n1522207126\tInstagram\t790\t1\n1522207126\tYouTube\t930\t1\n1522207127\tFacebook\t663\t2\n1522207127\tInstagram\t662\t1\n1522207127\tYouTube\t624\t1\n1522207128\tFacebook\t987\t3\n1522207128\tInstagram\t665\t3\n1522207128\tYouTube\t965\t1\n1522207129\tFacebook\t214\t1\n1522207129\tInstagram\t832\t2\n1522207129\tYouTube\t498\t2\n1522207130\tFacebook\t408\t1\n1522207130\tInstagram\t106\t3\n1522207130\tYouTube\t659\t1\n1522207131\tFacebook\t70\t3\n1522207131\tInstagram\t340\t2\n1522207131\tYouTube\t1\t3\n1522207132\tFacebook\t807\t1\n1522207132\tInstagram\t772\t1\n1522207132\tYouTube\t972\t1\n1522207133\tFacebook\t564\t3\n1522207133\tInstagram\t153\t1\n1522207133\tYouTube\t147\t2\n1522207134\tFacebook\t550\t2\n1522207134\tInstagram\t66\t3\n1522207134\tYouTube\t251\t2\n1522207135\tFacebook\t876\t1\n1522207135\tInstagram\t396\t2\n1522207135\tYouTube\t26\t1\n1522207136\tFacёbook\t939\t2\n1522207136\tInstagram\t745\t2\n1522207136\tYouTube\t376\t2\n1522207137\tFacebook\t484\t2\n1522207137\tInstagram\t407\t1\n1522207137\tYouTube\t71\t1\n1522207138\tFacebook\t421\t3\n1522207138\tInstagram\t645\t1\n1522207138\tYouTube\t929\t3\n1522207139\tFacebook\t577\t3\n1522207139\tInstagram\t785\t1\n1522207139\tYouTube\t762\t2\n1522207140\tFacebook\t178\t1\n1522207140\tInstagram\t465\t1\n1522207140\tYouTube\t454\t1\n1522207141\tFacebook\t596\t3\n1522207141\tInstagram\t191\t2\n1522207141\tYouTube\t480\t1\n1522207142\tFacebook\t906\t3\n1522207142\tInstagram\t626\t2\n1522207142\tYouTube\t671\t2\n1522207143\tFacebook\t270\t2\n1522207143\tInstagram\t232\t1\n1522207143\tYouTube\t833\t1\n1522207144\tFacebook\t70\t1\n1522207144\tInstagram\t351\t1\n1522207144\tYouTube\t276\t3\n1522207145\tFacebook\t253\t1\n1522207145\tInstagram\t460\t1\n1522207145\tYouTube\t764\t3\n1522207146\tFacebook\t968\t3\n1522207146\tInstagram\t55\t3\n1522207146\tYouTube\t410\t3\n1522207147\tFacebook\t207\t2\n1522207147\tInstagram\t673\t1\n1522207147\tYouTube\t748\t2\n1522207148\tFacebook\t713\t1\n1522207148\tInstagram\t136\t2\n1522207148\tYouTube\t29\t2\n1522207149\tFacebook\t795\t2\n1522207149\tInstagram\t356\t3\n1522207149\tYouTube\t573\t3\n1522207150\tFacebook\t83\t2\n1522207150\tInstagram\t781\t1\n1522207150\tYouTube\t664\t3\n1522207151\tFacebook\t4\t2\n1522207151\tInstagram\t729\t3\n1522207151\tYouTube\t472\t1\n1522207152\tFacebook\t196\t1\n1522207152\tInstagram\t481\t2\n1522207152\tYouTube\t983\t1\n1522207153\tFacebook\t137\t2\n1522207153\tInstagram\t244\t1\n1522207153\tYouTube\t670\t2\n1522207154\tFacebook\t795\t2\n1522207154\tInstagram\t782\t1\n1522207154\tYouTube\t74\t2\n1522207155\tFacebook\t682\t1\n1522207155\tInstagram\t258\t2\n1522207155\tYouTube\t752\t3\n1522207156\tFacebook\t990\t1\n1522207156\tInstagram\t727\t3\n1522207156\tYouTube\t613\t1\n1522207157\tFacebook\t501\t1\n1522207157\tInstagram\t943\t2\n1522207157\tYouTube\t435\t3\n1522207158\tFacebook\t847\t1\n1522207158\tInstagram\t311\t1\n1522207158\tYouTube\t14\t2\n1522207159\tFacebook\t849\t2\n1522207159\tInstagram\t222\t3\n1522207159\tYouTube\t619\t1\n1522207160\tFacebook\t202\t2\n1522207160\tInstagram\t734\t2\n1522207160\tYouTube\t730\t2\n1522207161\tFacebook\t297\t3\n1522207161\tInstagram\t945\t2\n1522207161\tYouTube\t997\t2\n1522207162\tFacebook\t35\t2\n1522207162\tInstagram\t839\t1\n1522207162\tYouTube\t479\t3\n1522207163\tFacebook\t528\t2\n1522207163\tInstagram\t738\t2\n1522207163\tYouTube\t293\t3\n1522207164\tFacebook\t438\t3\n1522207164\tInstagram\t384\t2\n1522207164\tYouTube\t371\t1\n1522207165\tFacebook\t283\t1\n1522207165\tInstagram\t853\t3\n1522207165\tYouTube\t388\t3\n1522207166\tFacebook\t966\t3\n1522207166\tInstagram\t536\t3\n1522207166\tYouTube\t229\t1\n1522207167\tFacebook\t792\t3\n1522207167\tInstagram\t828\t2\n1522207167\tYouTube\t119\t3\n1522207168\tFacebook\t110\t3\n1522207168\tInstagram\t975\t2\n1522207168\tYouTube\t433\t2\n1522207169\tFacebook\t662\t2\n1522207169\tInstagram\t631\t3\n1522207169\tYouTube\t685\t3\n1522207170\tFacebook\t26\t1\n1522207170\tInstagram\t687\t1\n1522207170\tYouTube\t797\t1\n1522207171\tFacebook\t264\t3\n1522207171\tInstagram\t967\t1\n1522207171\tYouTube\t945\t3\n1522207172\tFacebook\t393\t1\n1522207172\tInstagram\t404\t1\n1522207172\tYouTube\t332\t1\n1522207173\tFacebook\t971\t3\n1522207173\tInstagram\t879\t2\n1522207173\tYouTube\t626\t1\n1522207174\tFacebook\t387\t3\n1522207174\tInstagram\t29\t2\n1522207174\tYouTube\t140\t2\n1522207175\tFacebook\t800\t3\n1522207175\tInstagram\t733\t3\n1522207175\tYouTube\t250\t2\n1522207176\tFacebook\t224\t2\n1522207176\tInstagram\t574\t1\n1522207176\tYouTube\t264\t3\n1522207177\tFacebook\t1\t3\n1522207177\tInstagram\t8\t2\n1522207177\tYouTube\t11\t3\n1522207178\tFacebook\t989\t2\n1522207178\tInstagram\t42\t2\n1522207178\tYouTube\t997\t1\n1522207179\tFacebook\t103\t3\n1522207179\tInstagram\t967\t1\n1522207179\tYouTube\t467\t1\n1522207180\tFacebook\t20\t1\n1522207180\tInstagram\t539\t1\n1522207180\tYouTube\t662\t1\n1522207181\tFacebook\t403\t1\n1522207181\tInstagram\t744\t2\n1522207181\tYouTube\t809\t3\n1522207182\tFacebook\t919\t3\n1522207182\tInstagram\t422\t2\n1522207182\tYouTube\t184\t3\n1522207183\tFacebook\t301\t2\n1522207183\tInstagram\t708\t2\n1522207183\tYouTube\t549\t3\n1522207184\tFacebook\t298\t2\n1522207184\tInstagram\t978\t3\n1522207184\tYouTube\t169\t2\n1522207185\tFacebook\t510\t1\n1522207185\tInstagram\t95\t1\n1522207185\tYouTube\t273\t2\n1522207186\tFacebook\t613\t1\n1522207186\tInstagram\t549\t1\n1522207186\tYouTube\t310\t3\n1522207187\tFacebook\t912\t3\n1522207187\tInstagram\t347\t1\n1522207187\tYouTube\t983\t1\n1522207188\tFacebook\t511\t3\n1522207188\tInstagram\t429\t1\n1522207188\tYouTube\t409\t3\n1522207189\tFacebook\t779\t3\n1522207189\tInstagram\t754\t1\n1522207189\tYouTube\t473\t1\n1522207190\tFacebook\t799\t2\n1522207190\tInstagram\t9\t2\n1522207190\tYouTube\t665\t2\n1522207191\tFacebook\t43\t2\n1522207191\tInstagram\t264\t1\n1522207191\tYouTube\t804\t3\n'

COUNTRIES = {1: 'USA', 2: 'Canada', 3: 'Mexico'}


###################################################
### YOUR WORK BEGINS HERE
###################################################

class Logins():

    def __init__(self):
        pass

    def getCountry(self, countryid):
        country = ''
        if int(countryid) == 1:
            country = 'USA'
        elif int(countryid) == 2:
            country = 'Canada'
        elif int(countryid) == 3:
            country = 'Mexico'
        return country

    def splitpayload(self):
        data = LOGINS_DATA.split('\n')
        return data

    def getpayloadsize(self):
        payloadsize  = self.splitpayload()
        payloadsize = len(payloadsize) -1 #the split adds and empty list so we have to disregard that
        return payloadsize

    def processLogins(self):
        print('processing data.....')
        data = self.splitpayload()
        minstagramcounts = []
        uinstagramcounts = []
        cinstagramcounts = []
        myoutubecounts = []
        uyoutubecounts = []
        cyoutubecounts = []
        mfacebookcounts = []
        ufacebookcounts = []
        cfacebookcounts = []
        facebookdict = {}
        instagramdict = {}
        youtubedict = {}
        facebookcount = 0
        instagramcount = 0
        youtubecount = 0
        mfmissing = 0
        mimissing = 0
        mymissing = 0
        ufmissing = 0
        uimissing = 0
        uymissing = 0
        cfmissing = 0
        cimissing = 0
        cymissing = 0
        facebookmissingdata = []
        instagrammissingdata = []
        youtubemissingdata = []



        for item in data:
            try:
                newdata = item.split('\t')
                app = newdata[1]
                appinitial = app[0]
                logincount = newdata[2]
                countryid = newdata[3]
                countrycode = Logins.getCountry(self, countryid)
                if appinitial == 'F' or app == 'Facebook':
                    if len(logincount) == 0:
                        facebookmissingdata.append(countrycode)
                    facebookcount+=1
                    if countrycode == 'Mexico':
                        if len(logincount[2]) ==0:
                            mfmissing += 1
                        else:
                            mfacebookcounts.append(int(logincount))
                    elif countrycode == 'USA':
                        if len(logincount[2]) ==0:
                            ufmissing += 1
                        else:
                            ufacebookcounts.append(int(logincount))
                    elif countrycode == 'Canada':
                        if len(logincount[2]) ==0:
                            cfmissing += 1
                        else:
                            cfacebookcounts.append(int(logincount))
                if appinitial == 'I' or app == 'Instagram':
                    if len(logincount) == 0:
                       instagrammissingdata.append(countrycode)
                    instagramcount+=1
                    if countrycode == 'Mexico':
                        if len(logincount[2]) ==0:
                            mimissing += 1
                        else:
                            minstagramcounts.append(int(logincount))
                    elif countrycode == 'USA':
                        if len(logincount[2]) ==0:
                            uimissing += 1
                        else:
                            uinstagramcounts.append(int(logincount))
                    elif countrycode == 'Canada':
                        if len(logincount[2]) ==0:
                            cimissing += 1
                        else:
                            cinstagramcounts.append(int(logincount))
                if appinitial == 'Y' or app == 'YouTube':
                    youtubecount+=1
                    if countrycode == 'Mexico':
                        if len(logincount[2]) ==0:
                            mymissing += 1
                        else:
                            myoutubecounts.append(int(logincount))
                    elif countrycode == 'USA':
                        if len(logincount[2]) == 0:
                            uymissing += 1
                        else:
                            uyoutubecounts.append(int(logincount))
                    elif countrycode == 'Canada':
                        if len(logincount[2]) ==0:
                            cymissing += 1
                        else:
                            cyoutubecounts.append(int(logincount))
            except:
                pass


        facebookdict['Mexico'] = mfacebookcounts
        facebookdict['USA'] = ufacebookcounts
        facebookdict['Canada'] = cfacebookcounts
        instagramdict['Mexico'] = minstagramcounts
        instagramdict['USA'] = uinstagramcounts
        instagramdict['Canada'] = cinstagramcounts
        youtubedict['Mexico'] = myoutubecounts
        youtubedict['USA'] = uyoutubecounts
        youtubedict['Canada'] = cyoutubecounts

        return facebookdict, instagramdict, youtubedict, facebookcount, instagramcount, youtubecount, facebookmissingdata, instagrammissingdata, youtubemissingdata



    def getaverages(self):
        self.payloadsize = self.getpayloadsize()
        self.facebookdict, self.instagramdict, self.youtubedict, self.facebookcount, self.instagramcount, self.youtubecount, self.facebookmissingdata, self.instagrammissingdata, self.youtubemissingdata = self.processLogins()



        mexicofacebookavg = (sum(self.facebookdict['Mexico'])+(self.facebookmissingdata.count('Mexico') * sum(self.facebookdict['Mexico']) / len(self.facebookdict['Mexico']))) / (len(self.facebookdict['Mexico']) + self.facebookmissingdata.count('Mexico'))
        usafacebookavg = (sum(self.facebookdict['USA'])+(self.facebookmissingdata.count('USA') * sum(self.facebookdict['USA']) / len(self.facebookdict['USA']))) / (len(self.facebookdict['USA']) + self.facebookmissingdata.count('USA'))
        canadafacebookavg = (sum(self.facebookdict['Canada'])+(self.facebookmissingdata.count('Canada') * sum(self.facebookdict['Canada']) / len(self.facebookdict['Canada']))) / (len(self.facebookdict['Canada']) + self.facebookmissingdata.count('Canada'))
        print('Average for Facebook in Mexico: ', mexicofacebookavg)
        print('Average for Facebook in USA: ', usafacebookavg)
        print('Average for Facebook in Canada: ', canadafacebookavg)


        mexicoinstagramavg = (sum(self.instagramdict['Mexico'])+(self.instagrammissingdata.count('Mexico') * sum(self.instagramdict['Mexico']) / len(self.instagramdict['Mexico']))) / (len(self.instagramdict['Mexico']) + self.instagrammissingdata.count('Mexico'))
        usainstagramavg = (sum(self.instagramdict['USA'])+(self.instagrammissingdata.count('USA') * sum(self.instagramdict['USA']) / len(self.instagramdict['USA']))) / (len(self.instagramdict['USA']) + self.instagrammissingdata.count('USA'))
        canadainstagramavg = (sum(self.instagramdict['Canada'])+(self.instagrammissingdata.count('Canada') * sum(self.instagramdict['Canada']) / len(self.instagramdict['Canada']))) / (len(self.instagramdict['Canada']) + self.instagrammissingdata.count('Canada'))
        print('Average for Instagram in Mexico: ', mexicoinstagramavg)
        print('Average for Instagram in USA: ', usainstagramavg)
        print('Average for Instagram in Canada: ', canadainstagramavg)


        mexicoyoutubeavg = (sum(self.youtubedict['Mexico'])+(self.youtubemissingdata.count('Mexico') * sum(self.youtubedict['Mexico']) / len(self.youtubedict['Mexico']))) / (len(self.youtubedict['Mexico']) + self.youtubemissingdata.count('Mexico'))
        usayoutubeavg = (sum(self.youtubedict['USA'])+(self.youtubemissingdata.count('USA') * sum(self.youtubedict['USA']) / len(self.youtubedict['USA']))) / (len(self.youtubedict['USA']) + self.youtubemissingdata.count('USA'))
        canadayoutubeavg = (sum(self.youtubedict['Canada'])+(self.youtubemissingdata.count('Canada') * sum(self.youtubedict['Canada']) / len(self.youtubedict['Canada']))) / (len(self.youtubedict['Canada']) + self.youtubemissingdata.count('Canada'))

        print('Average for YouTube in Mexico: ', mexicoyoutubeavg)
        print('Average for YouTube in USA: ', usayoutubeavg)
        print('Average for YouTube in Canada: ', canadayoutubeavg)

log = Logins()
# log.processLogins()
log.getaverages()
