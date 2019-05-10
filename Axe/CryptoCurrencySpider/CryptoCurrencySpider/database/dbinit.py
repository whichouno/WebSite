from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String

#CONNECTION_STRING = "mysql+pymysql://root:qwe123@localhost:3306/coin"
# CONNECTION_STRING = "mysql+pymysql://root:123456@192.168.199.176:32768/coin"
CONNECTION_STRING = "mysql+pymysql://root:123456@127.0.0.1:32768/coin"
Base = declarative_base()

#Bitcoin-(BTC)
class Table_Bitcoin(Base):
    __tablename__ = 'Bitcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)
    marketcap = Column('marketcap',FLOAT)

#EthereumClassic-(ETC)
class Table_EthereumClassic(Base):
    __tablename__ = 'EthereumClassic'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)
    marketcap = Column('marketcap',FLOAT)

#Ethereum-(ETH)
class Table_Ethereum(Base):
    __tablename__ = 'Ethereum'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)
    marketcap = Column('marketcap',FLOAT)

#BitcoinCash-(BCH)
class Table_BitcoinCash(Base):
    __tablename__ = 'BitcoinCash'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)
    marketcap = Column('marketcap',FLOAT)

#BitShares-(BTS)
class Table_BitShares(Base):
    __tablename__ = 'BitShares'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)
    marketcap = Column('marketcap',FLOAT)

#EOS-(EOS)
class Table_EOS(Base):
    __tablename__ = 'EOS'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)
    marketcap = Column('marketcap',FLOAT)

#NEO-(NEO)
class Table_NEO(Base):
    __tablename__ = 'NEO'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)
    marketcap = Column('marketcap', FLOAT)

#LiteCoin-(LTC)
class Table_Litecoin(Base):
    __tablename__ = 'Litecoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)
    marketcap = Column('marketcap', FLOAT)

'''
#Dogecoin-(DOGE)

class Table_Dogecoin(Base):
    __tablename__ = 'Dogecoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Waves-(WAVES)

class Table_Waves(Base):
    __tablename__ = 'Waves'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BitConnect-(BCC)

class Table_BitConnect(Base):
    __tablename__ = 'BitConnect'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#KuCoinShares-(KCS)

class Table_KuCoinShares(Base):
    __tablename__ = 'KuCoinShares'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Steem-(STEEM)

class Table_Steem(Base):
    __tablename__ = 'Steem'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Populous-(PPT)

class Table_Populous(Base):
    __tablename__ = 'Populous'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Siacoin-(SC)

class Table_Siacoin(Base):
    __tablename__ = 'Siacoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BinanceCoin-(BNB)

class Table_BinanceCoin(Base):
    __tablename__ = 'BinanceCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Farstcoin-(FRCT)

class Table_Farstcoin(Base):
    __tablename__ = 'Farstcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Verge-(XVG)

class Table_Verge(Base):
    __tablename__ = 'Verge'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Stratis-(STRAT)

class Table_Stratis(Base):
    __tablename__ = 'Stratis'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Madcoin-(MDC)

class Table_Madcoin(Base):
    __tablename__ = 'Madcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#ENTCash-(ENT)

class Table_ENTCash(Base):
    __tablename__ = 'ENTCash'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Tether-(USDT)

class Table_Tether(Base):
    __tablename__ = 'Tether'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#XYLO-(XYLO)

class Table_XYLO(Base):
    __tablename__ = 'XYLO'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#SantaCoin-(STC)

class Table_SantaCoin(Base):
    __tablename__ = 'SantaCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Status-(SNT)

class Table_Status(Base):
    __tablename__ = 'Status'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#KemCredit-(KMC)

class Table_KemCredit(Base):
    __tablename__ = 'KemCredit'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Bytecoin-(BCN)

class Table_Bytecoin(Base):
    __tablename__ = 'Bytecoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#9COIN-(9COIN)

class Table_9COIN(Base):
    __tablename__ = '9COIN'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Royalties-(XRY)

class Table_Royalties(Base):
    __tablename__ = 'Royalties'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BatCoin-(BAT)

class Table_BatCoin(Base):
    __tablename__ = 'BatCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#AidosKuneen-(ADK)

class Table_AidosKuneen(Base):
    __tablename__ = 'AidosKuneen'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#RabbitCoin-(RBBT)

class Table_RabbitCoin(Base):
    __tablename__ = 'RabbitCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#InternetofThings-(XOT)

class Table_InternetofThings(Base):
    __tablename__ = 'InternetofThings'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#OCOW-(OCOW)

class Table_OCOW(Base):
    __tablename__ = 'OCOW'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#GoldUnionCoin-(GUC)

class Table_GoldUnionCoin(Base):
    __tablename__ = 'GoldUnionCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#TeslaCoilCoin-(TESLA)

class Table_TeslaCoilCoin(Base):
    __tablename__ = 'TeslaCoilCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#FutCoin-(FUTC)

class Table_FutCoin(Base):
    __tablename__ = 'FutCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#PresidentJohnson-(GARY)

class Table_PresidentJohnson(Base):
    __tablename__ = 'PresidentJohnson'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#FrankyWillCoin-(FRWC)

class Table_FrankyWillCoin(Base):
    __tablename__ = 'FrankyWillCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#SnakeEyes-(SNAKE)

class Table_SnakeEyes(Base):
    __tablename__ = 'SnakeEyes'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#InvisibleCoin-(IVZ)

class Table_InvisibleCoin(Base):
    __tablename__ = 'InvisibleCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#MobileCash-(MBL)

class Table_MobileCash(Base):
    __tablename__ = 'MobileCash'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#AvatarCoin-(AV)

class Table_AvatarCoin(Base):
    __tablename__ = 'AvatarCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#HyperTV-(HYTV)

class Table_HyperTV(Base):
    __tablename__ = 'HyperTV'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#TrickyCoin-(TRICK)

class Table_TrickyCoin(Base):
    __tablename__ = 'TrickyCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Psilocybin-(PSY)

class Table_Psilocybin(Base):
    __tablename__ = 'Psilocybin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Opescoin-(OPES)

class Table_Opescoin(Base):
    __tablename__ = 'Opescoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#LAthaan-(LTH)

class Table_LAthaan(Base):
    __tablename__ = 'LAthaan'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Cashme-(CME)

class Table_Cashme(Base):
    __tablename__ = 'Cashme'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#UtaCoin-(UTA)

class Table_UtaCoin(Base):
    __tablename__ = 'UtaCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#FirstBitcoinCapital-(BITCF)

class Table_FirstBitcoinCapital(Base):
    __tablename__ = 'FirstBitcoinCapital'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#TeamUp-(TEAM)

class Table_TeamUp(Base):
    __tablename__ = 'TeamUp'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#TheCreed-(TCR)

class Table_TheCreed(Base):
    __tablename__ = 'TheCreed'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#PrismChain-(PRM)

class Table_PrismChain(Base):
    __tablename__ = 'PrismChain'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#DarkLisk-(DISK)

class Table_DarkLisk(Base):
    __tablename__ = 'DarkLisk'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BITFID-(FID)

class Table_BITFID(Base):
    __tablename__ = 'BITFID'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#SportsCoin-(SPORT)

class Table_SportsCoin(Base):
    __tablename__ = 'SportsCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Faceblock-(FBL)

class Table_Faceblock(Base):
    __tablename__ = 'Faceblock'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Operand-(OP)

class Table_Operand(Base):
    __tablename__ = 'Operand'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Voyacoin-(VOYA)

class Table_Voyacoin(Base):
    __tablename__ = 'Voyacoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Lazaruscoin-(LAZ)

class Table_Lazaruscoin(Base):
    __tablename__ = 'Lazaruscoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#MoneyCoin-(MONEY)

class Table_MoneyCoin(Base):
    __tablename__ = 'MoneyCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#DigitalBullionGold-(DBG)

class Table_DigitalBullionGold(Base):
    __tablename__ = 'DigitalBullionGold'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#MMXVI-(MMXVI)

class Table_MMXVI(Base):
    __tablename__ = 'MMXVI'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BitAlphaCoin-(BAC)

class Table_BitAlphaCoin(Base):
    __tablename__ = 'BitAlphaCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Omicron-(OMC)

class Table_Omicron(Base):
    __tablename__ = 'Omicron'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#X2-(X2)

class Table_X2(Base):
    __tablename__ = 'X2'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Xaucoin-(XAU)

class Table_Xaucoin(Base):
    __tablename__ = 'Xaucoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#XDEII-(XDE2)

class Table_XDEII(Base):
    __tablename__ = 'XDEII'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#ShellCoin-(SHELL)

class Table_ShellCoin(Base):
    __tablename__ = 'ShellCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#PresidentTrump-(PRES)

class Table_PresidentTrump(Base):
    __tablename__ = 'PresidentTrump'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Axiom-(AXIOM)

class Table_Axiom(Base):
    __tablename__ = 'Axiom'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#RHFCoin-(RHFC)

class Table_RHFCoin(Base):
    __tablename__ = 'RHFCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#PeopleCoin-(MEN)

class Table_PeopleCoin(Base):
    __tablename__ = 'PeopleCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#WASpace-(WA)

class Table_WASpace(Base):
    __tablename__ = 'WASpace'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#PayPeer-(PAYP)

class Table_PayPeer(Base):
    __tablename__ = 'PayPeer'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Dubstep-(DUB)

class Table_Dubstep(Base):
    __tablename__ = 'Dubstep'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Qora-(QORA)

class Table_Qora(Base):
    __tablename__ = 'Qora'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#InfinityPay-(IPY)

class Table_InfinityPay(Base):
    __tablename__ = 'InfinityPay'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Dashs-(DASHS)

class Table_Dashs(Base):
    __tablename__ = 'Dashs'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#FirstBitcoin-(BIT)

class Table_FirstBitcoin(Base):
    __tablename__ = 'FirstBitcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#PabyosiCoin(Special)-(PCS)

class Table_PabyosiCoinSpecial(Base):
    __tablename__ = 'PabyosiCoinSpecial'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Natcoin-(NTC)

class Table_Natcoin(Base):
    __tablename__ = 'Natcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#FireFlyCoin-(FFC)

class Table_FireFlyCoin(Base):
    __tablename__ = 'FireFlyCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Tattoocoin(LimitedEdition)-(TLE)

class Table_TattoocoinLimitedEdition(Base):
    __tablename__ = 'TattoocoinLimitedEdition'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Facecoin-(FC)

class Table_Facecoin(Base):
    __tablename__ = 'Facecoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#LinkedCoin-(LKC)

class Table_LinkedCoin(Base):
    __tablename__ = 'LinkedCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#HappyCreatorCoin-(HCC)

class Table_HappyCreatorCoin(Base):
    __tablename__ = 'HappyCreatorCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BetaCoin-(BET)

class Table_BetaCoin(Base):
    __tablename__ = 'BetaCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#STEX-(STEX)

class Table_STEX(Base):
    __tablename__ = 'STEX'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#TheVeganInitiative-(XVE)

class Table_TheVeganInitiative(Base):
    __tablename__ = 'TheVeganInitiative'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#GameLeagueCoin-(GML)

class Table_GameLeagueCoin(Base):
    __tablename__ = 'GameLeagueCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Quotient-(XQN)

class Table_Quotient(Base):
    __tablename__ = 'Quotient'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Hyper-(HYPER)

class Table_Hyper(Base):
    __tablename__ = 'Hyper'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#10MToken-(10MT)

class Table_10MToken(Base):
    __tablename__ = '10MToken'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Cheapcoin-(CHEAP)

class Table_Cheapcoin(Base):
    __tablename__ = 'Cheapcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#DeltaCredits-(DCRE)

class Table_DeltaCredits(Base):
    __tablename__ = 'DeltaCredits'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#EggCoin-(EGG)

class Table_EggCoin(Base):
    __tablename__ = 'EggCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Yescoin-(YES)

class Table_Yescoin(Base):
    __tablename__ = 'Yescoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Moneta-(MONETA)

class Table_Moneta(Base):
    __tablename__ = 'Moneta'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#LeekCoin-(LEEK)

class Table_LeekCoin(Base):
    __tablename__ = 'LeekCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#NamoCoin-(NAMO)

class Table_NamoCoin(Base):
    __tablename__ = 'NamoCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BlockchainIndex-(BLX)

class Table_BlockchainIndex(Base):
    __tablename__ = 'BlockchainIndex'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#KashhCoin-(KASHH)

class Table_KashhCoin(Base):
    __tablename__ = 'KashhCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#TopazCoin-(TOPAZ)

class Table_TopazCoin(Base):
    __tablename__ = 'TopazCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#AlpaCoin-(APC)

class Table_AlpaCoin(Base):
    __tablename__ = 'AlpaCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#eUSD-(EUSD)

class Table_eUSD(Base):
    __tablename__ = 'eUSD'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#RichCoin-(RICHX)

class Table_RichCoin(Base):
    __tablename__ = 'RichCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#RoyalCoin-(ROYAL)

class Table_RoyalCoin(Base):
    __tablename__ = 'RoyalCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Huncoin-(HNC)

class Table_Huncoin(Base):
    __tablename__ = 'Huncoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#PokeCoin-(POKE)

class Table_PokeCoin(Base):
    __tablename__ = 'PokeCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Soma-(SCT)

class Table_Soma(Base):
    __tablename__ = 'Soma'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Avoncoin-(ACN)

class Table_Avoncoin(Base):
    __tablename__ = 'Avoncoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#netBit-(NBIT)

class Table_netBit(Base):
    __tablename__ = 'netBit'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Aseancoin-(ASN)

class Table_Aseancoin(Base):
    __tablename__ = 'Aseancoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#eLTC-(ELTC2)

class Table_eLTC(Base):
    __tablename__ = 'eLTC'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Bubble-(BUB)

class Table_Bubble(Base):
    __tablename__ = 'Bubble'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Runners-(RUNNERS)

class Table_Runners(Base):
    __tablename__ = 'Runners'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#TeraCoin-(TERA)

class Table_TeraCoin(Base):
    __tablename__ = 'TeraCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Rupaya[OLD]-(RUPX)

class Table_RupayaOLD(Base):
    __tablename__ = 'RupayaOLD'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Wink-(WINK)

class Table_Wink(Base):
    __tablename__ = 'Wink'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#DeusCoin-(DEUS)

class Table_DeusCoin(Base):
    __tablename__ = 'DeusCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BlazerCoin-(BLAZR)

class Table_BlazerCoin(Base):
    __tablename__ = 'BlazerCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Karmacoin-(KARMA)

class Table_Karmacoin(Base):
    __tablename__ = 'Karmacoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Bastonet-(BSN)

class Table_Bastonet(Base):
    __tablename__ = 'Bastonet'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Tellurion-(TELL)

class Table_Tellurion(Base):
    __tablename__ = 'Tellurion'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Golfcoin-(GOLF)

class Table_Golfcoin(Base):
    __tablename__ = 'Golfcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#CyberCoin-(CC)

class Table_CyberCoin(Base):
    __tablename__ = 'CyberCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Vulcano-(VULC)

class Table_Vulcano(Base):
    __tablename__ = 'Vulcano'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#GlobalBusinessRevolution-(GBRC)

class Table_GlobalBusinessRevolution(Base):
    __tablename__ = 'GlobalBusinessRevolution'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#iBTC-(IBTC)

class Table_iBTC(Base):
    __tablename__ = 'iBTC'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Rcoin-(RCN)

class Table_Rcoin(Base):
    __tablename__ = 'Rcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Mavro-(MAVRO)

class Table_Mavro(Base):
    __tablename__ = 'Mavro'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Birds-(BIRDS)

class Table_Birds(Base):
    __tablename__ = 'Birds'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Primulon-(PRIMU)

class Table_Primulon(Base):
    __tablename__ = 'Primulon'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BitcoinSilver-(BTCS)

class Table_BitcoinSilver(Base):
    __tablename__ = 'BitcoinSilver'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#UAHPay-(UAHPAY)

class Table_UAHPay(Base):
    __tablename__ = 'UAHPay'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Bitcoin2x-(BTC2X)

class Table_Bitcoin2x(Base):
    __tablename__ = 'Bitcoin2x'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Swapcoin-(SWP)

class Table_Swapcoin(Base):
    __tablename__ = 'Swapcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#GoldMaxCoin-(GMX)

class Table_GoldMaxCoin(Base):
    __tablename__ = 'GoldMaxCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#EventChain-(EVC)

class Table_EventChain(Base):
    __tablename__ = 'EventChain'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#OXFina-(OX)

class Table_OXFina(Base):
    __tablename__ = 'OXFina'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Magnetcoin-(MAGN)

class Table_Magnetcoin(Base):
    __tablename__ = 'Magnetcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#CashPokerPro-(CASH)

class Table_CashPokerPro(Base):
    __tablename__ = 'CashPokerPro'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Musiconomi-(MCI)

class Table_Musiconomi(Base):
    __tablename__ = 'Musiconomi'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Elacoin-(ELC)

class Table_Elacoin(Base):
    __tablename__ = 'Elacoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#UGAIN-(GAIN)

class Table_UGAIN(Base):
    __tablename__ = 'UGAIN'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#PinkDog-(PDG)

class Table_PinkDog(Base):
    __tablename__ = 'PinkDog'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#PirateBlocks-(SKULL)

class Table_PirateBlocks(Base):
    __tablename__ = 'PirateBlocks'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#SandCoin-(SND)

class Table_SandCoin(Base):
    __tablename__ = 'SandCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#CORION-(COR)

class Table_CORION(Base):
    __tablename__ = 'CORION'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#MarxCoin-(MARX)

class Table_MarxCoin(Base):
    __tablename__ = 'MarxCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#TopCoin-(TOP)

class Table_TopCoin(Base):
    __tablename__ = 'TopCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#LandCoin-(LDCN)

class Table_LandCoin(Base):
    __tablename__ = 'LandCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Cubits-(QBT)

class Table_Cubits(Base):
    __tablename__ = 'Cubits'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Alphabit-(ABC)

class Table_Alphabit(Base):
    __tablename__ = 'Alphabit'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Triaconta-(TRIA)

class Table_Triaconta(Base):
    __tablename__ = 'Triaconta'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#UR-(UR)

class Table_UR(Base):
    __tablename__ = 'UR'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#CyclingCoin-(CYC)

class Table_CyclingCoin(Base):
    __tablename__ = 'CyclingCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Bitbase-(BTBc)

class Table_Bitbase(Base):
    __tablename__ = 'Bitbase'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Sakuracoin-(SKR)

class Table_Sakuracoin(Base):
    __tablename__ = 'Sakuracoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#T-coin-(TCOIN)

class Table_Tcoin(Base):
    __tablename__ = 'Tcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#StorjcoinX-(SJCX)

class Table_StorjcoinX(Base):
    __tablename__ = 'StorjcoinX'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#DutchCoin-(DUTCH)

class Table_DutchCoin(Base):
    __tablename__ = 'DutchCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#SHACoin-(SHA)

class Table_SHACoin(Base):
    __tablename__ = 'SHACoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#EncryptoTel[ETH]-(ETT)

class Table_EncryptoTelETH(Base):
    __tablename__ = 'EncryptoTelETH'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#ContentandADNetwork-(CAN)

class Table_ContentandADNetwork(Base):
    __tablename__ = 'ContentandADNetwork'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Wowcoin-(WOW)

class Table_Wowcoin(Base):
    __tablename__ = 'Wowcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#FlappyCoin-(FLAP)

class Table_FlappyCoin(Base):
    __tablename__ = 'FlappyCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Everus-(EVR)

class Table_Everus(Base):
    __tablename__ = 'Everus'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Minex-(MINEX)

class Table_Minex(Base):
    __tablename__ = 'Minex'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#UniversalRoyalCoin-(UNRC)

class Table_UniversalRoyalCoin(Base):
    __tablename__ = 'UniversalRoyalCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#WeAreSatoshi-(WSX)

class Table_WeAreSatoshi(Base):
    __tablename__ = 'WeAreSatoshi'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#eGold-(EGOLD)

class Table_eGold(Base):
    __tablename__ = 'eGold'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#DynamicCoin-(DMC)

class Table_DynamicCoin(Base):
    __tablename__ = 'DynamicCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#TodayCoin-(TODAY)

class Table_TodayCoin(Base):
    __tablename__ = 'TodayCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Macro-(MCR)

class Table_Macro(Base):
    __tablename__ = 'Macro'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#TurboCoin-(TURBO)

class Table_TurboCoin(Base):
    __tablename__ = 'TurboCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#MergeCoin-(MGC)

class Table_MergeCoin(Base):
    __tablename__ = 'MergeCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Donationcoin-(DON)

class Table_Donationcoin(Base):
    __tablename__ = 'Donationcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Matryx-(MTX)

class Table_Matryx(Base):
    __tablename__ = 'Matryx'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#LePen-(LEPEN)

class Table_LePen(Base):
    __tablename__ = 'LePen'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Bitok-(BITOK)

class Table_Bitok(Base):
    __tablename__ = 'Bitok'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#XTDCoin-(XTD)

class Table_XTDCoin(Base):
    __tablename__ = 'XTDCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#RubleBit-(RUBIT)

class Table_RubleBit(Base):
    __tablename__ = 'RubleBit'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#SIGMAcoin-(SIGMA)

class Table_SIGMAcoin(Base):
    __tablename__ = 'SIGMAcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Sharkcoin-(SAK)

class Table_Sharkcoin(Base):
    __tablename__ = 'Sharkcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BestChain-(BEST)

class Table_BestChain(Base):
    __tablename__ = 'BestChain'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#SafeCoin-(SFE)

class Table_SafeCoin(Base):
    __tablename__ = 'SafeCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Bitcedi-(BXC)

class Table_Bitcedi(Base):
    __tablename__ = 'Bitcedi'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#HalloweenCoin-(HALLO)

class Table_HalloweenCoin(Base):
    __tablename__ = 'HalloweenCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#InternationalDiamond-(XID)

class Table_InternationalDiamond(Base):
    __tablename__ = 'InternationalDiamond'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#EthereumLite-(ELITE)

class Table_EthereumLite(Base):
    __tablename__ = 'EthereumLite'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#IndiaCoin-(INDIA)

class Table_IndiaCoin(Base):
    __tablename__ = 'IndiaCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Fonziecoin-(FONZ)

class Table_Fonziecoin(Base):
    __tablename__ = 'Fonziecoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#CBDCrystals-(CBD)

class Table_CBDCrystals(Base):
    __tablename__ = 'CBDCrystals'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#UNCoin-(UNC)

class Table_UNCoin(Base):
    __tablename__ = 'UNCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#ANRYZE-(RYZ)

class Table_ANRYZE(Base):
    __tablename__ = 'ANRYZE'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#IrishCoin-(IRL)

class Table_IrishCoin(Base):
    __tablename__ = 'IrishCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#GAYMoney-(GAY)

class Table_GAYMoney(Base):
    __tablename__ = 'GAYMoney'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Zilbercoin-(ZBC)

class Table_Zilbercoin(Base):
    __tablename__ = 'Zilbercoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#AkuyaCoin-(AKY)

class Table_AkuyaCoin(Base):
    __tablename__ = 'AkuyaCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Cryptopay-(CPAY)

class Table_Cryptopay(Base):
    __tablename__ = 'Cryptopay'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#DimonCoin-(FUDD)

class Table_DimonCoin(Base):
    __tablename__ = 'DimonCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#GlobalJobcoin-(GJC)

class Table_GlobalJobcoin(Base):
    __tablename__ = 'GlobalJobcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Francs-(FRN)

class Table_Francs(Base):
    __tablename__ = 'Francs'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#PeepCoin-(PCN)

class Table_PeepCoin(Base):
    __tablename__ = 'PeepCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Animecoin-(ANI)

class Table_Animecoin(Base):
    __tablename__ = 'Animecoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#GlassCoin-(GLS)

class Table_GlassCoin(Base):
    __tablename__ = 'GlassCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#SISA-(SISA)

class Table_SISA(Base):
    __tablename__ = 'SISA'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#MSD-(MSD)

class Table_MSD(Base):
    __tablename__ = 'MSD'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#TechShares-(THS)

class Table_TechShares(Base):
    __tablename__ = 'TechShares'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BTCMoon-(BTCM)

class Table_BTCMoon(Base):
    __tablename__ = 'BTCMoon'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Aces-(ACES)

class Table_Aces(Base):
    __tablename__ = 'Aces'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#PylonNetwork-(PYLNT)

class Table_PylonNetwork(Base):
    __tablename__ = 'PylonNetwork'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#EDRCoin-(EDRC)

class Table_EDRCoin(Base):
    __tablename__ = 'EDRCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#TerraNova-(TER)

class Table_TerraNova(Base):
    __tablename__ = 'TerraNova'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Nimfamoney-(NIMFA)

class Table_Nimfamoney(Base):
    __tablename__ = 'Nimfamoney'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#iQuant-(IQT)

class Table_iQuant(Base):
    __tablename__ = 'iQuant'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#VPNCoin-(VASH)

class Table_VPNCoin(Base):
    __tablename__ = 'VPNCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#EXRNchain-(EXRN)

class Table_EXRNchain(Base):
    __tablename__ = 'EXRNchain'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#GETProtocol-(GET)

class Table_GETProtocol(Base):
    __tablename__ = 'GETProtocol'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Peacecoin-(PEC)

class Table_Peacecoin(Base):
    __tablename__ = 'Peacecoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Spectre.aiUtilityToken-(SXUT)

class Table_SpectreaiUtilityToken(Base):
    __tablename__ = 'SpectreaiUtilityToken'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Phantomx-(PNX)

class Table_Phantomx(Base):
    __tablename__ = 'Phantomx'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#NumusCash-(NUMUS)

class Table_NumusCash(Base):
    __tablename__ = 'NumusCash'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Regacoin-(REGA)

class Table_Regacoin(Base):
    __tablename__ = 'Regacoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Chronologic-(DAY)

class Table_Chronologic(Base):
    __tablename__ = 'Chronologic'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Suretly-(SUR)

class Table_Suretly(Base):
    __tablename__ = 'Suretly'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#MagicCoin-(MAGE)

class Table_MagicCoin(Base):
    __tablename__ = 'MagicCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#WiCoin-(WIC)

class Table_WiCoin(Base):
    __tablename__ = 'WiCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Protean-(PRN)

class Table_Protean(Base):
    __tablename__ = 'Protean'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Leverj-(LEV)

class Table_Leverj(Base):
    __tablename__ = 'Leverj'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#GameChainSystem-(GCS)

class Table_GameChainSystem(Base):
    __tablename__ = 'GameChainSystem'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Kzcash-(KZC)

class Table_Kzcash(Base):
    __tablename__ = 'Kzcash'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Starbase-(STAR)

class Table_Starbase(Base):
    __tablename__ = 'Starbase'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BOScoin-(BOS)

class Table_BOScoin(Base):
    __tablename__ = 'BOScoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#OPCoin-(OPC)

class Table_OPCoin(Base):
    __tablename__ = 'OPCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Granite-(GRN)

class Table_Granite(Base):
    __tablename__ = 'Granite'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#LiteCoinGold-(LTG)

class Table_LiteCoinGold(Base):
    __tablename__ = 'LiteCoinGold'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#ZSEcoin-(ZSE)

class Table_ZSEcoin(Base):
    __tablename__ = 'ZSEcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#StrikeBitClub-(SBC)

class Table_StrikeBitClub(Base):
    __tablename__ = 'StrikeBitClub'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#FidentiaX-(FDX)

class Table_FidentiaX(Base):
    __tablename__ = 'FidentiaX'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#HighGain-(HIGH)

class Table_HighGain(Base):
    __tablename__ = 'HighGain'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#UnitedTradersToken-(UTT)

class Table_UnitedTradersToken(Base):
    __tablename__ = 'UnitedTradersToken'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Compcoin-(CMP)

class Table_Compcoin(Base):
    __tablename__ = 'Compcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BlockCDN-(BCDN)

class Table_BlockCDN(Base):
    __tablename__ = 'BlockCDN'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#HODLBucks-(HDLB)

class Table_HODLBucks(Base):
    __tablename__ = 'HODLBucks'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Spectre.aiDividendToken-(SXDT)

class Table_SpectreaiDividendToken(Base):
    __tablename__ = 'SpectreaiDividendToken'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#PlexCoin-(PLX)

class Table_PlexCoin(Base):
    __tablename__ = 'PlexCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Coupecoin-(COUPE)

class Table_Coupecoin(Base):
    __tablename__ = 'Coupecoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#TOKYO-(TOKC)

class Table_TOKYO(Base):
    __tablename__ = 'TOKYO'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#GOLDRewardToken-(GRX)

class Table_GOLDRewardToken(Base):
    __tablename__ = 'GOLDRewardToken'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BitcoinGod-(GOD)

class Table_BitcoinGod(Base):
    __tablename__ = 'BitcoinGod'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#TIESNetwork-(TIE)

class Table_TIESNetwork(Base):
    __tablename__ = 'TIESNetwork'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Karma-(KRM)

class Table_Karma(Base):
    __tablename__ = 'Karma'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Cloud-(CLD)

class Table_Cloud(Base):
    __tablename__ = 'Cloud'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Bankex-(BKX)

class Table_Bankex(Base):
    __tablename__ = 'Bankex'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#InfinityEconomics-(XIN)

class Table_InfinityEconomics(Base):
    __tablename__ = 'InfinityEconomics'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#ZenGold-(ZENGOLD)

class Table_ZenGold(Base):
    __tablename__ = 'ZenGold'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Tokugawa-(TOK)

class Table_Tokugawa(Base):
    __tablename__ = 'Tokugawa'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#NEOGOLD-(NEOG)

class Table_NEOGOLD(Base):
    __tablename__ = 'NEOGOLD'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Vezt-(VZT)

class Table_Vezt(Base):
    __tablename__ = 'Vezt'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Bloom-(BLT)

class Table_Bloom(Base):
    __tablename__ = 'Bloom'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Escroco-(ESC)

class Table_Escroco(Base):
    __tablename__ = 'Escroco'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#SphreAIR-(XID)

class Table_SphreAIR(Base):
    __tablename__ = 'SphreAIR'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Ignition-(IC)

class Table_Ignition(Base):
    __tablename__ = 'Ignition'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Bitair-(BTCA)

class Table_Bitair(Base):
    __tablename__ = 'Bitair'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#GolosGold-(GBG)

class Table_GolosGold(Base):
    __tablename__ = 'GolosGold'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#DIMCOIN-(DIM)

class Table_DIMCOIN(Base):
    __tablename__ = 'DIMCOIN'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#FAPcoin-(FAP)

class Table_FAPcoin(Base):
    __tablename__ = 'FAPcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Fazzcoin-(FAZZ)

class Table_Fazzcoin(Base):
    __tablename__ = 'Fazzcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#UquidCoin-(UQC)

class Table_UquidCoin(Base):
    __tablename__ = 'UquidCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BitSoar-(BSR)

class Table_BitSoar(Base):
    __tablename__ = 'BitSoar'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#SafeTradeCoin-(XSTC)

class Table_SafeTradeCoin(Base):
    __tablename__ = 'SafeTradeCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Swisscoin-(SIC)

class Table_Swisscoin(Base):
    __tablename__ = 'Swisscoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Antimatter-(ANTX)

class Table_Antimatter(Base):
    __tablename__ = 'Antimatter'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#LightningBitcoin[Futures]-(LBTC)

class Table_LightningBitcoinFutures(Base):
    __tablename__ = 'LightningBitcoinFutures'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Infinitecoin-(IFC)

class Table_Infinitecoin(Base):
    __tablename__ = 'Infinitecoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BitSerial-(BTE)

class Table_BitSerial(Base):
    __tablename__ = 'BitSerial'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#PlusCoin-(PLC)

class Table_PlusCoin(Base):
    __tablename__ = 'PlusCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Numus-(NMS)

class Table_Numus(Base):
    __tablename__ = 'Numus'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#DavorCoin-(DAV)

class Table_DavorCoin(Base):
    __tablename__ = 'DavorCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BitcoinAtom[Futures]-(BCA)

class Table_BitcoinAtomFutures(Base):
    __tablename__ = 'BitcoinAtomFutures'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#TokenClub-(TCT)

class Table_TokenClub(Base):
    __tablename__ = 'TokenClub'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#LLToken-(LLT)

class Table_LLToken(Base):
    __tablename__ = 'LLToken'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Zap-(ZAP)

class Table_Zap(Base):
    __tablename__ = 'Zap'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#CryptopiaFeeShares-(CEFS)

class Table_CryptopiaFeeShares(Base):
    __tablename__ = 'CryptopiaFeeShares'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#B3Coin-(B3)

class Table_B3Coin(Base):
    __tablename__ = 'B3Coin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#ClubCoin-(CLUB)

class Table_ClubCoin(Base):
    __tablename__ = 'ClubCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Polis-(POLIS)

class Table_Polis(Base):
    __tablename__ = 'Polis'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#HomeBlockCoin-(HBC)

class Table_HomeBlockCoin(Base):
    __tablename__ = 'HomeBlockCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#WETH-(WETH)

class Table_WETH(Base):
    __tablename__ = 'WETH'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#COMSA[XEM]-(CMS)

class Table_COMSAXEM(Base):
    __tablename__ = 'COMSAXEM'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#HTML5COIN-(HTML5)

class Table_HTML5COIN(Base):
    __tablename__ = 'HTML5COIN'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#JingtumTech-(SWTC)

class Table_JingtumTech(Base):
    __tablename__ = 'JingtumTech'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#WINCOIN-(WC)

class Table_WINCOIN(Base):
    __tablename__ = 'WINCOIN'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#POLYAI-(AI)

class Table_POLYAI(Base):
    __tablename__ = 'POLYAI'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#InfChain-(INF)

class Table_InfChain(Base):
    __tablename__ = 'InfChain'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#UnitedBitcoin-(UBTC)

class Table_UnitedBitcoin(Base):
    __tablename__ = 'UnitedBitcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#ATN-(ATN)

class Table_ATN(Base):
    __tablename__ = 'ATN'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#HackspaceCapital-(HAC)

class Table_HackspaceCapital(Base):
    __tablename__ = 'HackspaceCapital'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BitDegree-(BDG)

class Table_BitDegree(Base):
    __tablename__ = 'BitDegree'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#StrongHands-(SHND)

class Table_StrongHands(Base):
    __tablename__ = 'StrongHands'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#EACoin-(EAG)

class Table_EACoin(Base):
    __tablename__ = 'EACoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Mixin-(XIN)

class Table_Mixin(Base):
    __tablename__ = 'Mixin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#COMSA[ETH]-(CMS)

class Table_COMSAETH(Base):
    __tablename__ = 'COMSAETH'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Rebellious-(REBL)

class Table_Rebellious(Base):
    __tablename__ = 'Rebellious'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Maker-(MKR)

class Table_Maker(Base):
    __tablename__ = 'Maker'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#OneRootNetwork-(RNT)

class Table_OneRootNetwork(Base):
    __tablename__ = 'OneRootNetwork'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Ace-(ACE)

class Table_Ace(Base):
    __tablename__ = 'Ace'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BigONEToken-(BIG)

class Table_BigONEToken(Base):
    __tablename__ = 'BigONEToken'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Telcoin-(TEL)

class Table_Telcoin(Base):
    __tablename__ = 'Telcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Filecoin[Futures]-(FIL)

class Table_FilecoinFutures(Base):
    __tablename__ = 'FilecoinFutures'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#UGToken-(UGT)

class Table_UGToken(Base):
    __tablename__ = 'UGToken'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#MeasurableDataToken-(MDT)

class Table_MeasurableDataToken(Base):
    __tablename__ = 'MeasurableDataToken'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#CFun-(CFUN)

class Table_CFun(Base):
    __tablename__ = 'CFun'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Cyder-(CYDER)

class Table_Cyder(Base):
    __tablename__ = 'Cyder'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Ignis-(IGNIS)

class Table_Ignis(Base):
    __tablename__ = 'Ignis'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#SegWit2x-(B2X)

class Table_SegWit2x(Base):
    __tablename__ = 'SegWit2x'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#AWARE-(AWR)

class Table_AWARE(Base):
    __tablename__ = 'AWARE'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Viuly-(VIU)

class Table_Viuly(Base):
    __tablename__ = 'Viuly'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#ugChain-(UGC)

class Table_ugChain(Base):
    __tablename__ = 'ugChain'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#MOAC-(MOAC)

class Table_MOAC(Base):
    __tablename__ = 'MOAC'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Aigang-(AIX)

class Table_Aigang(Base):
    __tablename__ = 'Aigang'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Coinlancer-(CL)

class Table_Coinlancer(Base):
    __tablename__ = 'Coinlancer'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Fargocoin-(FRGC)

class Table_Fargocoin(Base):
    __tablename__ = 'Fargocoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#SophiaTX-(SPHTX)

class Table_SophiaTX(Base):
    __tablename__ = 'SophiaTX'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Qbao-(QBT)

class Table_Qbao(Base):
    __tablename__ = 'Qbao'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BitClave-(CAT)

class Table_BitClave(Base):
    __tablename__ = 'BitClave'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#FairGame-(FAIR)

class Table_FairGame(Base):
    __tablename__ = 'FairGame'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Tezos(Pre-Launch)-(XTZ)

class Table_TezosPreLaunch(Base):
    __tablename__ = 'TezosPreLaunch'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Cappasity-(CAPP)

class Table_Cappasity(Base):
    __tablename__ = 'Cappasity'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#KuberaCoin-(KBR)

class Table_KuberaCoin(Base):
    __tablename__ = 'KuberaCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#TradeToken-(TIO)

class Table_TradeToken(Base):
    __tablename__ = 'TradeToken'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#HyperPay-(HPY)

class Table_HyperPay(Base):
    __tablename__ = 'HyperPay'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#OlympusLabs-(MOT)

class Table_OlympusLabs(Base):
    __tablename__ = 'OlympusLabs'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#CanYaCoin-(CAN)

class Table_CanYaCoin(Base):
    __tablename__ = 'CanYaCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#MicroMoney-(AMM)

class Table_MicroMoney(Base):
    __tablename__ = 'MicroMoney'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#SuperBitcoin-(SBTC)

class Table_SuperBitcoin(Base):
    __tablename__ = 'SuperBitcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Energo-(TSL)

class Table_Energo(Base):
    __tablename__ = 'Energo'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#QLINK-(QLC)

class Table_QLINK(Base):
    __tablename__ = 'QLINK'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#TopChain-(TOPC)

class Table_TopChain(Base):
    __tablename__ = 'TopChain'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#LendConnect-(LCT)

class Table_LendConnect(Base):
    __tablename__ = 'LendConnect'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Bottos-(BTO)

class Table_Bottos(Base):
    __tablename__ = 'Bottos'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#HTMLCOIN-(HTML)

class Table_HTMLCOIN(Base):
    __tablename__ = 'HTMLCOIN'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#HighPerformanceBlockchain-(HPB)

class Table_HighPerformanceBlockchain(Base):
    __tablename__ = 'HighPerformanceBlockchain'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BitcoinX[Futures]-(BCX)

class Table_BitcoinXFutures(Base):
    __tablename__ = 'BitcoinXFutures'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Kcash-(KCASH)

class Table_Kcash(Base):
    __tablename__ = 'Kcash'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Game-(GTC)

class Table_Game(Base):
    __tablename__ = 'Game'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#EchoLink-(EKO)

class Table_EchoLink(Base):
    __tablename__ = 'EchoLink'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#WaykiChain-(WIC)

class Table_WaykiChain(Base):
    __tablename__ = 'WaykiChain'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#AIDoctor-(AIDOC)

class Table_AIDoctor(Base):
    __tablename__ = 'AIDoctor'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#SmartMesh-(SMT)

class Table_SmartMesh(Base):
    __tablename__ = 'SmartMesh'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BiboxToken-(BIX)

class Table_BiboxToken(Base):
    __tablename__ = 'BiboxToken'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#GenaroNetwork-(GNX)

class Table_GenaroNetwork(Base):
    __tablename__ = 'GenaroNetwork'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#InternetNodeToken-(INT)

class Table_InternetNodeToken(Base):
    __tablename__ = 'InternetNodeToken'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Selfkey-(KEY)

class Table_Selfkey(Base):
    __tablename__ = 'Selfkey'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#MediShares-(MDS)

class Table_MediShares(Base):
    __tablename__ = 'MediShares'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BitcoinDiamond-(BCD)

class Table_BitcoinDiamond(Base):
    __tablename__ = 'BitcoinDiamond'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#SwftCoin-(SWFTC)

class Table_SwftCoin(Base):
    __tablename__ = 'SwftCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Show-(SHOW)

class Table_Show(Base):
    __tablename__ = 'Show'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#IOStoken-(IOST)

class Table_IOStoken(Base):
    __tablename__ = 'IOStoken'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#ATMCoin-(ATMC)

class Table_ATMCoin(Base):
    __tablename__ = 'ATMCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#PizzaCoin-(PIZZA)

class Table_PizzaCoin(Base):
    __tablename__ = 'PizzaCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BurstOcean-(OCEAN)

class Table_BurstOcean(Base):
    __tablename__ = 'BurstOcean'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#INSEcosystem-(INS)

class Table_INSEcosystem(Base):
    __tablename__ = 'INSEcosystem'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#QibuckAsset-(QBK)

class Table_QibuckAsset(Base):
    __tablename__ = 'QibuckAsset'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#DigitalCredits-(DGCS)

class Table_DigitalCredits(Base):
    __tablename__ = 'DigitalCredits'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#CoffeeCoin-(CFC)

class Table_CoffeeCoin(Base):
    __tablename__ = 'CoffeeCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Lex4All-(LEX)

class Table_Lex4All(Base):
    __tablename__ = 'Lex4All'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#CCMiner-(CCM100)

class Table_CCMiner(Base):
    __tablename__ = 'CCMiner'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#AgrolifeCoin-(AGLC)

class Table_AgrolifeCoin(Base):
    __tablename__ = 'AgrolifeCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#GBCGoldCoin-(GBC)

class Table_GBCGoldCoin(Base):
    __tablename__ = 'GBCGoldCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Frazcoin-(FRAZ)

class Table_Frazcoin(Base):
    __tablename__ = 'Frazcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#NodeCoin-(NODC)

class Table_NodeCoin(Base):
    __tablename__ = 'NodeCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Antilitecoin-(ALTC)

class Table_Antilitecoin(Base):
    __tablename__ = 'Antilitecoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#SydPak-(SDP)

class Table_SydPak(Base):
    __tablename__ = 'SydPak'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#OsmiumCoin-(OS76)

class Table_OsmiumCoin(Base):
    __tablename__ = 'OsmiumCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#CryptoEscudo-(CESC)

class Table_CryptoEscudo(Base):
    __tablename__ = 'CryptoEscudo'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Sojourn-(SOJ)

class Table_Sojourn(Base):
    __tablename__ = 'Sojourn'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#CRTCoin-(CRT)

class Table_CRTCoin(Base):
    __tablename__ = 'CRTCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#LetItRide-(LIR)

class Table_LetItRide(Base):
    __tablename__ = 'LetItRide'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Steps-(STEPS)

class Table_Steps(Base):
    __tablename__ = 'Steps'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#G3N-(G3N)

class Table_G3N(Base):
    __tablename__ = 'G3N'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Xonecoin-(XOC)

class Table_Xonecoin(Base):
    __tablename__ = 'Xonecoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Tychocoin-(TYCHO)

class Table_Tychocoin(Base):
    __tablename__ = 'Tychocoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#MTMGaming-(MTM)

class Table_MTMGaming(Base):
    __tablename__ = 'MTMGaming'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#MorningStar-(MRNG)

class Table_MorningStar(Base):
    __tablename__ = 'MorningStar'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Zonecoin-(ZNE)

class Table_Zonecoin(Base):
    __tablename__ = 'Zonecoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#TAGRcoin-(TAGR)

class Table_TAGRcoin(Base):
    __tablename__ = 'TAGRcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Zayedcoin-(ZYD)

class Table_Zayedcoin(Base):
    __tablename__ = 'Zayedcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BiosCrypto-(BIOS)

class Table_BiosCrypto(Base):
    __tablename__ = 'BiosCrypto'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#RiptoBux-(RBX)

class Table_RiptoBux(Base):
    __tablename__ = 'RiptoBux'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#MindCoin-(MND)

class Table_MindCoin(Base):
    __tablename__ = 'MindCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#CryptoWorldXToken-(CWXT)

class Table_CryptoWorldXToken(Base):
    __tablename__ = 'CryptoWorldXToken'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Crypto-(CTO)

class Table_Crypto(Base):
    __tablename__ = 'Crypto'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#RSGPcoin-(RSGP)

class Table_RSGPcoin(Base):
    __tablename__ = 'RSGPcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BowsCoin-(BSC)

class Table_BowsCoin(Base):
    __tablename__ = 'BowsCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BillaryCoin-(BLRY)

class Table_BillaryCoin(Base):
    __tablename__ = 'BillaryCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Asiadigicoin-(ADCN)

class Table_Asiadigicoin(Base):
    __tablename__ = 'Asiadigicoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#FlavorCoin-(FLVR)

class Table_FlavorCoin(Base):
    __tablename__ = 'FlavorCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Destiny-(DES)

class Table_Destiny(Base):
    __tablename__ = 'Destiny'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Dreamcoin-(DRM)

class Table_Dreamcoin(Base):
    __tablename__ = 'Dreamcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BeaverCoin-(BVC)

class Table_BeaverCoin(Base):
    __tablename__ = 'BeaverCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#YellowToken-(YEL)

class Table_YellowToken(Base):
    __tablename__ = 'YellowToken'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#GameBetCoin-(GBT)

class Table_GameBetCoin(Base):
    __tablename__ = 'GameBetCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Jewels-(JWL)

class Table_Jewels(Base):
    __tablename__ = 'Jewels'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#VIPTokens-(VIP)

class Table_VIPTokens(Base):
    __tablename__ = 'VIPTokens'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#PIECoin-(PIE)

class Table_PIECoin(Base):
    __tablename__ = 'PIECoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Blackstar-(BSTAR)

class Table_Blackstar(Base):
    __tablename__ = 'Blackstar'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Pulse-(PULSE)

class Table_Pulse(Base):
    __tablename__ = 'Pulse'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#JavaScriptToken-(JS)

class Table_JavaScriptToken(Base):
    __tablename__ = 'JavaScriptToken'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Californium-(CF)

class Table_Californium(Base):
    __tablename__ = 'Californium'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#WARP-(WARP)

class Table_WARP(Base):
    __tablename__ = 'WARP'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#SACoin-(SAC)

class Table_SACoin(Base):
    __tablename__ = 'SACoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BoostCoin-(BOST)

class Table_BoostCoin(Base):
    __tablename__ = 'BoostCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#IslaCoin-(ISL)

class Table_IslaCoin(Base):
    __tablename__ = 'IslaCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#VectorAI-(VEC2)

class Table_VectorAI(Base):
    __tablename__ = 'VectorAI'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#WMCoin-(WMC)

class Table_WMCoin(Base):
    __tablename__ = 'WMCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Sling-(SLING)

class Table_Sling(Base):
    __tablename__ = 'Sling'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Franko-(FRK)

class Table_Franko(Base):
    __tablename__ = 'Franko'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Newbium-(NEWB)

class Table_Newbium(Base):
    __tablename__ = 'Newbium'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Yacoin-(YAC)

class Table_Yacoin(Base):
    __tablename__ = 'Yacoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Bitz-(BITZ)

class Table_Bitz(Base):
    __tablename__ = 'Bitz'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#E4ROW-(E4ROW)

class Table_E4ROW(Base):
    __tablename__ = 'E4ROW'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Freicoin-(FRC)

class Table_Freicoin(Base):
    __tablename__ = 'Freicoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Firecoin-(FIRE)

class Table_Firecoin(Base):
    __tablename__ = 'Firecoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#CoExistCoin-(COXST)

class Table_CoExistCoin(Base):
    __tablename__ = 'CoExistCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#SproutsExtreme-(SPEX)

class Table_SproutsExtreme(Base):
    __tablename__ = 'SproutsExtreme'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#SecretCoin-(SCRT)

class Table_SecretCoin(Base):
    __tablename__ = 'SecretCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BTCtalkcoin-(TALK)

class Table_BTCtalkcoin(Base):
    __tablename__ = 'BTCtalkcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#MutualCoin-(MUT)

class Table_MutualCoin(Base):
    __tablename__ = 'MutualCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Shilling-(SH)

class Table_Shilling(Base):
    __tablename__ = 'Shilling'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Grantcoin-(GRT)

class Table_Grantcoin(Base):
    __tablename__ = 'Grantcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Joincoin-(J)

class Table_Joincoin(Base):
    __tablename__ = 'Joincoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#ShadowToken-(SHDW)

class Table_ShadowToken(Base):
    __tablename__ = 'ShadowToken'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#PX-(PX)

class Table_PX(Base):
    __tablename__ = 'PX'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Flycoin-(FLY)

class Table_Flycoin(Base):
    __tablename__ = 'Flycoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#WayGuide-(WAY)

class Table_WayGuide(Base):
    __tablename__ = 'WayGuide'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BlazeCoin-(BLZ)

class Table_BlazeCoin(Base):
    __tablename__ = 'BlazeCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BriaCoin-(BRIA)

class Table_BriaCoin(Base):
    __tablename__ = 'BriaCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BTSR-(BTSR)

class Table_BTSR(Base):
    __tablename__ = 'BTSR'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#GanjaCoin-(MRJA)

class Table_GanjaCoin(Base):
    __tablename__ = 'GanjaCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#GlobalCoin-(GLC)

class Table_GlobalCoin(Base):
    __tablename__ = 'GlobalCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Valorbit-(VAL)

class Table_Valorbit(Base):
    __tablename__ = 'Valorbit'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#AmberCoin-(AMBER)

class Table_AmberCoin(Base):
    __tablename__ = 'AmberCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Remicoin-(RMC)

class Table_Remicoin(Base):
    __tablename__ = 'Remicoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Bankcoin-(B@)

class Table_Bankcoin(Base):
    __tablename__ = 'Bankcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Interzone-(ITZ)

class Table_Interzone(Base):
    __tablename__ = 'Interzone'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Stress-(STS)

class Table_Stress(Base):
    __tablename__ = 'Stress'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#CorgiCoin-(CORG)

class Table_CorgiCoin(Base):
    __tablename__ = 'CorgiCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Universe-(UNI)

class Table_Universe(Base):
    __tablename__ = 'Universe'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#LottoCoin-(LOT)

class Table_LottoCoin(Base):
    __tablename__ = 'LottoCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Casino-(CASINO)

class Table_Casino(Base):
    __tablename__ = 'Casino'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#ColossuscoinV2-(CV2)

class Table_ColossuscoinV2(Base):
    __tablename__ = 'ColossuscoinV2'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#ArcadeToken-(ARC)

class Table_ArcadeToken(Base):
    __tablename__ = 'ArcadeToken'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#UltimateSecureCash-(USC)

class Table_UltimateSecureCash(Base):
    __tablename__ = 'UltimateSecureCash'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Shorty-(SHORTY)

class Table_Shorty(Base):
    __tablename__ = 'Shorty'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#MetalCoin-(METAL)

class Table_MetalCoin(Base):
    __tablename__ = 'MetalCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#IncaKoin-(NKA)

class Table_IncaKoin(Base):
    __tablename__ = 'IncaKoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#YashCoin-(YASH)

class Table_YashCoin(Base):
    __tablename__ = 'YashCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Woodcoin-(LOG)

class Table_Woodcoin(Base):
    __tablename__ = 'Woodcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#CryptCoin-(CRYPT)

class Table_CryptCoin(Base):
    __tablename__ = 'CryptCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#EthereumMovieVenture-(EMV)

class Table_EthereumMovieVenture(Base):
    __tablename__ = 'EthereumMovieVenture'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BunnyCoin-(BUN)

class Table_BunnyCoin(Base):
    __tablename__ = 'BunnyCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#FIMKrypto-(FIMK)

class Table_FIMKrypto(Base):
    __tablename__ = 'FIMKrypto'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Rustbits-(RUSTBITS)

class Table_Rustbits(Base):
    __tablename__ = 'Rustbits'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#InPay-(INPAY)

class Table_InPay(Base):
    __tablename__ = 'InPay'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Ergo-(EFYT)

class Table_Ergo(Base):
    __tablename__ = 'Ergo'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#TheCypherfunks-(FUNK)

class Table_TheCypherfunks(Base):
    __tablename__ = 'TheCypherfunks'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#TheGCCcoin-(GCC)

class Table_TheGCCcoin(Base):
    __tablename__ = 'TheGCCcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Bitswift-(SWIFT)

class Table_Bitswift(Base):
    __tablename__ = 'Bitswift'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#GCoin-(GCN)

class Table_GCoin(Base):
    __tablename__ = 'GCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Virtacoin-(VTA)

class Table_Virtacoin(Base):
    __tablename__ = 'Virtacoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#ProspectorsGold-(PGL)

class Table_ProspectorsGold(Base):
    __tablename__ = 'ProspectorsGold'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Photon-(PHO)

class Table_Photon(Base):
    __tablename__ = 'Photon'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Abncoin-(ABN)

class Table_Abncoin(Base):
    __tablename__ = 'Abncoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#AppleCoin-(APW)

class Table_AppleCoin(Base):
    __tablename__ = 'AppleCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Hush-(HUSH)

class Table_Hush(Base):
    __tablename__ = 'Hush'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BCAP-(BCAP)

class Table_BCAP(Base):
    __tablename__ = 'BCAP'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#DigitalMoneyBits-(DMB)

class Table_DigitalMoneyBits(Base):
    __tablename__ = 'DigitalMoneyBits'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#CaliphCoin-(CALC)

class Table_CaliphCoin(Base):
    __tablename__ = 'CaliphCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#EbittreeCoin-(EBT)

class Table_EbittreeCoin(Base):
    __tablename__ = 'EbittreeCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#HarmonyCoin-(HMC)

class Table_HarmonyCoin(Base):
    __tablename__ = 'HarmonyCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Enigma-(XNG)

# class Table_Enigma(Base):
#     __tablename__ = 'Enigma'
#     date = Column('date', DATE,primary_key=True)
#     open = Column('open', FLOAT)
#     high = Column('high', FLOAT)
#     low = Column('low', FLOAT)
#     close = Column('close', FLOAT)
#     volume = Column('volume', FLOAT)

#TristarCoin-(TSTR)

class Table_TristarCoin(Base):
    __tablename__ = 'TristarCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Concoin-(CONX)

class Table_Concoin(Base):
    __tablename__ = 'Concoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Selfiecoin-(SLFI)

class Table_Selfiecoin(Base):
    __tablename__ = 'Selfiecoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#GeyserCoin-(GSR)

class Table_GeyserCoin(Base):
    __tablename__ = 'GeyserCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Magnum-(MGM)

class Table_Magnum(Base):
    __tablename__ = 'Magnum'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#P7Coin-(P7C)

class Table_P7Coin(Base):
    __tablename__ = 'P7Coin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#FuturXe-(FXE)

class Table_FuturXe(Base):
    __tablename__ = 'FuturXe'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Ulatech-(ULA)

class Table_Ulatech(Base):
    __tablename__ = 'Ulatech'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Rawcoin-(XRC)

class Table_Rawcoin(Base):
    __tablename__ = 'Rawcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#SaveandGain-(SANDG)

class Table_SaveandGain(Base):
    __tablename__ = 'SaveandGain'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#LevoPlus-(LVPS)

class Table_LevoPlus(Base):
    __tablename__ = 'LevoPlus'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Project-X-(NANOX)

class Table_ProjectX(Base):
    __tablename__ = 'ProjectX'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Elysium-(ELS)

class Table_Elysium(Base):
    __tablename__ = 'Elysium'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#CrevaCoin-(CREVA)

class Table_CrevaCoin(Base):
    __tablename__ = 'CrevaCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Coimatic2.0-(CTIC2)

class Table_Coimatic20(Base):
    __tablename__ = 'Coimatic20'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Corethum-(CRTM)

class Table_Corethum(Base):
    __tablename__ = 'Corethum'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#ImpulseCoin-(IMPS)

class Table_ImpulseCoin(Base):
    __tablename__ = 'ImpulseCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BioBar-(BIOB)

class Table_BioBar(Base):
    __tablename__ = 'BioBar'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Argus-(ARGUS)

class Table_Argus(Base):
    __tablename__ = 'Argus'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#EGO-(EGO)

class Table_EGO(Base):
    __tablename__ = 'EGO'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#KingNCoin-(KNC)

class Table_KingNCoin(Base):
    __tablename__ = 'KingNCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Coimatic3.0-(CTIC3)

class Table_Coimatic30(Base):
    __tablename__ = 'Coimatic30'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#ARbit-(ARB)

class Table_ARbit(Base):
    __tablename__ = 'ARbit'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Braincoin-(BRAIN)

class Table_Braincoin(Base):
    __tablename__ = 'Braincoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Unrealcoin-(URC)

class Table_Unrealcoin(Base):
    __tablename__ = 'Unrealcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#DollarOnline-(DOLLAR)

class Table_DollarOnline(Base):
    __tablename__ = 'DollarOnline'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Veros-(VRS)

class Table_Veros(Base):
    __tablename__ = 'Veros'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#JobsCoin-(JOBS)

class Table_JobsCoin(Base):
    __tablename__ = 'JobsCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#iBank-(IBANK)

class Table_iBank(Base):
    __tablename__ = 'iBank'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#SocialCoin-(SOCC)

class Table_SocialCoin(Base):
    __tablename__ = 'SocialCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Quebecoin-(QBC)

class Table_Quebecoin(Base):
    __tablename__ = 'Quebecoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Bitvolt-(VOLT)

class Table_Bitvolt(Base):
    __tablename__ = 'Bitvolt'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#RideMyCar-(RIDE)

class Table_RideMyCar(Base):
    __tablename__ = 'RideMyCar'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Orlycoin-(ORLY)

class Table_Orlycoin(Base):
    __tablename__ = 'Orlycoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#HighVoltage-(HVCO)

class Table_HighVoltage(Base):
    __tablename__ = 'HighVoltage'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#AnarchistsPrime-(ACP)

class Table_AnarchistsPrime(Base):
    __tablename__ = 'AnarchistsPrime'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Litecred-(LTCR)

class Table_Litecred(Base):
    __tablename__ = 'Litecred'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#MiloCoin-(MILO)

class Table_MiloCoin(Base):
    __tablename__ = 'MiloCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#CredenceCoin-(CRDNC)

class Table_CredenceCoin(Base):
    __tablename__ = 'CredenceCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#PonziCoin-(PONZI)

class Table_PonziCoin(Base):
    __tablename__ = 'PonziCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#PRCoin-(PRC)

class Table_PRCoin(Base):
    __tablename__ = 'PRCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#DIBCOIN-(DIBC)

class Table_DIBCOIN(Base):
    __tablename__ = 'DIBCOIN'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#VaultCoin-(VLTC)

class Table_VaultCoin(Base):
    __tablename__ = 'VaultCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#PLNcoin-(PLNC)

class Table_PLNcoin(Base):
    __tablename__ = 'PLNcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Speedcash-(SCS)

class Table_Speedcash(Base):
    __tablename__ = 'Speedcash'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#WildBeastBlock-(WBB)

class Table_WildBeastBlock(Base):
    __tablename__ = 'WildBeastBlock'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#GeertCoin-(GEERT)

class Table_GeertCoin(Base):
    __tablename__ = 'GeertCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Cabbage-(CAB)

class Table_Cabbage(Base):
    __tablename__ = 'Cabbage'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Printerium-(PRX)

class Table_Printerium(Base):
    __tablename__ = 'Printerium'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#bitEUR-(BITEUR)

class Table_bitEUR(Base):
    __tablename__ = 'bitEUR'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#PosEx-(PEX)

class Table_PosEx(Base):
    __tablename__ = 'PosEx'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#WomenCoin-(WOMEN)

class Table_WomenCoin(Base):
    __tablename__ = 'WomenCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#CybCSec-(XCS)

class Table_CybCSec(Base):
    __tablename__ = 'CybCSec'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#PlayerCoin-(PLACO)

class Table_PlayerCoin(Base):
    __tablename__ = 'PlayerCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Roofs-(ROOFS)

class Table_Roofs(Base):
    __tablename__ = 'Roofs'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Iconic-(ICON)

class Table_Iconic(Base):
    __tablename__ = 'Iconic'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#DAPPSTER-(DLISK)

class Table_DAPPSTER(Base):
    __tablename__ = 'DAPPSTER'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#ArtexCoin-(ATX)

class Table_ArtexCoin(Base):
    __tablename__ = 'ArtexCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Skeincoin-(SKC)

class Table_Skeincoin(Base):
    __tablename__ = 'Skeincoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BOAT-(BOAT)

class Table_BOAT(Base):
    __tablename__ = 'BOAT'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Debitcoin-(DBTC)

class Table_Debitcoin(Base):
    __tablename__ = 'Debitcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Slevin-(SLEVIN)

class Table_Slevin(Base):
    __tablename__ = 'Slevin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#AntiBitcoin-(ANTI)

class Table_AntiBitcoin(Base):
    __tablename__ = 'AntiBitcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Uro-(URO)

class Table_Uro(Base):
    __tablename__ = 'Uro'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#SwapToken-(TOKEN)

class Table_SwapToken(Base):
    __tablename__ = 'SwapToken'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#VapersCoin-(VPRC)

class Table_VapersCoin(Base):
    __tablename__ = 'VapersCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Impact-(IMX)

class Table_Impact(Base):
    __tablename__ = 'Impact'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Rupaya-(RUPX)

class Table_Rupaya(Base):
    __tablename__ = 'Rupaya'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Torcoin-(TOR)

class Table_Torcoin(Base):
    __tablename__ = 'Torcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#AllSafe-(ASAFE2)

class Table_AllSafe(Base):
    __tablename__ = 'AllSafe'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#UselessEthereumToken-(UET)

class Table_UselessEthereumToken(Base):
    __tablename__ = 'UselessEthereumToken'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#GlobalTourCoin-(GTC)

class Table_GlobalTourCoin(Base):
    __tablename__ = 'GlobalTourCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#HealthyWormCoin-(WORM)

class Table_HealthyWormCoin(Base):
    __tablename__ = 'HealthyWormCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#ExchangeN-(EXN)

class Table_ExchangeN(Base):
    __tablename__ = 'ExchangeN'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#TajCoin-(TAJ)

class Table_TajCoin(Base):
    __tablename__ = 'TajCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#LunaCoin-(LUNA)

class Table_LunaCoin(Base):
    __tablename__ = 'LunaCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#LeaCoin-(LEA)

class Table_LeaCoin(Base):
    __tablename__ = 'LeaCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#bitGold-(BITGOLD)

class Table_bitGold(Base):
    __tablename__ = 'bitGold'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Comet-(CMT)

class Table_Comet(Base):
    __tablename__ = 'Comet'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BnrtxCoin-(BNX)

class Table_BnrtxCoin(Base):
    __tablename__ = 'BnrtxCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Coinonat-(CXT)

class Table_Coinonat(Base):
    __tablename__ = 'Coinonat'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#MasterSwiscoin-(MSCN)

class Table_MasterSwiscoin(Base):
    __tablename__ = 'MasterSwiscoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#EcoCoin-(ECO)

class Table_EcoCoin(Base):
    __tablename__ = 'EcoCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Flaxscript-(FLAX)

class Table_Flaxscript(Base):
    __tablename__ = 'Flaxscript'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#USDe-(USDE)

class Table_USDe(Base):
    __tablename__ = 'USDe'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Eryllium-(ERY)

class Table_Eryllium(Base):
    __tablename__ = 'Eryllium'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Bitcoin21-(XBTC21)

class Table_Bitcoin21(Base):
    __tablename__ = 'Bitcoin21'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Spots-(SPT)

class Table_Spots(Base):
    __tablename__ = 'Spots'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#GuccioneCoin-(GCC)

class Table_GuccioneCoin(Base):
    __tablename__ = 'GuccioneCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Aerium-(AERM)

class Table_Aerium(Base):
    __tablename__ = 'Aerium'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#ZetaMicron-(ZMC)

class Table_ZetaMicron(Base):
    __tablename__ = 'ZetaMicron'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#EagleCoin-(EAGLE)

class Table_EagleCoin(Base):
    __tablename__ = 'EagleCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#eREAL-(EREAL)

class Table_eREAL(Base):
    __tablename__ = 'eREAL'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#SongCoin-(SONG)

class Table_SongCoin(Base):
    __tablename__ = 'SongCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#LiteCoinUltra-(LTCU)

class Table_LiteCoinUltra(Base):
    __tablename__ = 'LiteCoinUltra'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BenjiRolls-(BENJI)

class Table_BenjiRolls(Base):
    __tablename__ = 'BenjiRolls'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BipCoin-(BIP)

class Table_BipCoin(Base):
    __tablename__ = 'BipCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#300Token-(300)

class Table_300Token(Base):
    __tablename__ = '300Token'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#HempCoin-(HMP)

class Table_HempCoin(Base):
    __tablename__ = 'HempCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#NevaCoin-(NEVA)

class Table_NevaCoin(Base):
    __tablename__ = 'NevaCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#CompuCoin-(CPN)

class Table_CompuCoin(Base):
    __tablename__ = 'CompuCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#CthulhuOfferings-(OFF)

class Table_CthulhuOfferings(Base):
    __tablename__ = 'CthulhuOfferings'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Allion-(ALL)

class Table_Allion(Base):
    __tablename__ = 'Allion'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#TheresaMayCoin-(MAY)

class Table_TheresaMayCoin(Base):
    __tablename__ = 'TheresaMayCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Creatio-(XCRE)

class Table_Creatio(Base):
    __tablename__ = 'Creatio'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#DigitalRupees-(DRS)

class Table_DigitalRupees(Base):
    __tablename__ = 'DigitalRupees'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Solarflarecoin-(SFC)

class Table_Solarflarecoin(Base):
    __tablename__ = 'Solarflarecoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#RonPaulCoin-(RPC)

class Table_RonPaulCoin(Base):
    __tablename__ = 'RonPaulCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Acoin-(ACOIN)

class Table_Acoin(Base):
    __tablename__ = 'Acoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#bitSilver-(BITSILVER)

class Table_bitSilver(Base):
    __tablename__ = 'bitSilver'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Virtacoinplus-(XVP)

class Table_Virtacoinplus(Base):
    __tablename__ = 'Virtacoinplus'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#ReeCoin-(REE)

class Table_ReeCoin(Base):
    __tablename__ = 'ReeCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#X-Coin-(XCO)

class Table_XCoin(Base):
    __tablename__ = 'XCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Bolenum-(BLN)

class Table_Bolenum(Base):
    __tablename__ = 'Bolenum'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BumbaCoin-(BUMBA)

class Table_BumbaCoin(Base):
    __tablename__ = 'BumbaCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#ICOBID-(ICOB)

class Table_ICOBID(Base):
    __tablename__ = 'ICOBID'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#JinCoin-(JIN)

class Table_JinCoin(Base):
    __tablename__ = 'JinCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#GoldPieces-(GP)

class Table_GoldPieces(Base):
    __tablename__ = 'GoldPieces'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Beatcoin-(XBTS)

class Table_Beatcoin(Base):
    __tablename__ = 'Beatcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#GPUCoin-(GPU)

class Table_GPUCoin(Base):
    __tablename__ = 'GPUCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#SOILcoin-(SOIL)

class Table_SOILcoin(Base):
    __tablename__ = 'SOILcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#GlobalToken-(GLT)

class Table_GlobalToken(Base):
    __tablename__ = 'GlobalToken'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#FuzzBalls-(FUZZ)

class Table_FuzzBalls(Base):
    __tablename__ = 'FuzzBalls'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#MetalMusicCoin-(MTLMC3)

class Table_MetalMusicCoin(Base):
    __tablename__ = 'MetalMusicCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Cashcoin-(CASH)

class Table_Cashcoin(Base):
    __tablename__ = 'Cashcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#iDice-(ICE)

class Table_iDice(Base):
    __tablename__ = 'iDice'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#QuazarCoin-(QCN)

class Table_QuazarCoin(Base):
    __tablename__ = 'QuazarCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#SatoshiMadness-(MAD)

class Table_SatoshiMadness(Base):
    __tablename__ = 'SatoshiMadness'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Honey-(HONEY)

class Table_Honey(Base):
    __tablename__ = 'Honey'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Bitgem-(BTG)

class Table_Bitgem(Base):
    __tablename__ = 'Bitgem'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#MaoZedong-(MAO)

class Table_MaoZedong(Base):
    __tablename__ = 'MaoZedong'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Sativacoin-(STV)

class Table_Sativacoin(Base):
    __tablename__ = 'Sativacoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Evotion-(EVO)

class Table_Evotion(Base):
    __tablename__ = 'Evotion'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#TEKcoin-(TEK)

class Table_TEKcoin(Base):
    __tablename__ = 'TEKcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Money-($$$)

class Table_Money(Base):
    __tablename__ = 'Money'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#SixEleven-(611)

class Table_SixEleven(Base):
    __tablename__ = 'SixEleven'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Cypher-(CYP)

class Table_Cypher(Base):
    __tablename__ = 'Cypher'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#GoldPressedLatinum-(GPL)

class Table_GoldPressedLatinum(Base):
    __tablename__ = 'GoldPressedLatinum'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#VirtaUniqueCoin-(VUC)

class Table_VirtaUniqueCoin(Base):
    __tablename__ = 'VirtaUniqueCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#GlobalBoost-Y-(BSTY)

class Table_GlobalBoostY(Base):
    __tablename__ = 'GlobalBoostY'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Neuro-(NRO)

class Table_Neuro(Base):
    __tablename__ = 'Neuro'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#SoonCoin-(SOON)

class Table_SoonCoin(Base):
    __tablename__ = 'SoonCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#TagCoin-(TAG)

class Table_TagCoin(Base):
    __tablename__ = 'TagCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Catcoin-(CAT)

class Table_Catcoin(Base):
    __tablename__ = 'Catcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#PhilosopherStones-(PHS)

class Table_PhilosopherStones(Base):
    __tablename__ = 'PhilosopherStones'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#AquariusCoin-(ARCO)

class Table_AquariusCoin(Base):
    __tablename__ = 'AquariusCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Kayicoin-(KAYI)

class Table_Kayicoin(Base):
    __tablename__ = 'Kayicoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Kronecoin-(KRONE)

class Table_Kronecoin(Base):
    __tablename__ = 'Kronecoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Rubies-(RBIES)

class Table_Rubies(Base):
    __tablename__ = 'Rubies'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Swing-(SWING)

class Table_Swing(Base):
    __tablename__ = 'Swing'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#MustangCoin-(MST)

class Table_MustangCoin(Base):
    __tablename__ = 'MustangCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Hexx-(HXX)

class Table_Hexx(Base):
    __tablename__ = 'Hexx'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Zurcoin-(ZUR)

class Table_Zurcoin(Base):
    __tablename__ = 'Zurcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Mincoin-(MNC)

class Table_Mincoin(Base):
    __tablename__ = 'Mincoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BitQuark-(BTQ)

class Table_BitQuark(Base):
    __tablename__ = 'BitQuark'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#EmeraldCrypto-(EMD)

class Table_EmeraldCrypto(Base):
    __tablename__ = 'EmeraldCrypto'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#ZoZoCoin-(ZZC)

class Table_ZoZoCoin(Base):
    __tablename__ = 'ZoZoCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#bitBTC-(BITBTC)

class Table_bitBTC(Base):
    __tablename__ = 'bitBTC'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Bolivarcoin-(BOLI)

class Table_Bolivarcoin(Base):
    __tablename__ = 'Bolivarcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BERNcash-(BERN)

class Table_BERNcash(Base):
    __tablename__ = 'BERNcash'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Marijuanacoin-(MAR)

class Table_Marijuanacoin(Base):
    __tablename__ = 'Marijuanacoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Senderon-(SDRN)

class Table_Senderon(Base):
    __tablename__ = 'Senderon'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#TridentGroup-(TRDT)

class Table_TridentGroup(Base):
    __tablename__ = 'TridentGroup'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#ParallelCoin-(DUO)

class Table_ParallelCoin(Base):
    __tablename__ = 'ParallelCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BitTokens-(BXT)

class Table_BitTokens(Base):
    __tablename__ = 'BitTokens'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#eBitcoinCash-(EBCH)

class Table_eBitcoinCash(Base):
    __tablename__ = 'eBitcoinCash'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Dalecoin-(DALC)

class Table_Dalecoin(Base):
    __tablename__ = 'Dalecoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Marscoin-(MARS)

class Table_Marscoin(Base):
    __tablename__ = 'Marscoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BitAsean-(BAS)

class Table_BitAsean(Base):
    __tablename__ = 'BitAsean'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Prime-XI-(PXI)

class Table_PrimeXI(Base):
    __tablename__ = 'PrimeXI'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BROTHER-(BRAT)

class Table_BROTHER(Base):
    __tablename__ = 'BROTHER'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Eurocoin-(EUC)

class Table_Eurocoin(Base):
    __tablename__ = 'Eurocoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#VoteCoin-(VOT)

class Table_VoteCoin(Base):
    __tablename__ = 'VoteCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#RevolverCoin-(XRE)

class Table_RevolverCoin(Base):
    __tablename__ = 'RevolverCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Blakecoin-(BLC)

class Table_Blakecoin(Base):
    __tablename__ = 'Blakecoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#LiteBitcoin-(LBTC)

class Table_LiteBitcoin(Base):
    __tablename__ = 'LiteBitcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#DigitalDevelopersFund-(DDF)

class Table_DigitalDevelopersFund(Base):
    __tablename__ = 'DigitalDevelopersFund'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Tattoocoin(StandardEdition)-(TSE)

class Table_TattoocoinStandardEdition(Base):
    __tablename__ = 'TattoocoinStandardEdition'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Fujinto-(NTO)

class Table_Fujinto(Base):
    __tablename__ = 'Fujinto'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Cannation-(CNNC)

class Table_Cannation(Base):
    __tablename__ = 'Cannation'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#SovereignHero-(HERO)

class Table_SovereignHero(Base):
    __tablename__ = 'SovereignHero'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Quatloo-(QTL)

class Table_Quatloo(Base):
    __tablename__ = 'Quatloo'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BitcoinPlanet-(BTPL)

class Table_BitcoinPlanet(Base):
    __tablename__ = 'BitcoinPlanet'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#EOTToken-(EOT)

class Table_EOTToken(Base):
    __tablename__ = 'EOTToken'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#LiteBar-(LTB)

class Table_LiteBar(Base):
    __tablename__ = 'LiteBar'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#RouletteToken-(RLT)

class Table_RouletteToken(Base):
    __tablename__ = 'RouletteToken'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#iCoin-(ICN)

class Table_iCoin(Base):
    __tablename__ = 'iCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Sterlingcoin-(SLG)

class Table_Sterlingcoin(Base):
    __tablename__ = 'Sterlingcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#NetworkToken-(NTWK)

class Table_NetworkToken(Base):
    __tablename__ = 'NetworkToken'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#GameUnits-(UNITS)

class Table_GameUnits(Base):
    __tablename__ = 'GameUnits'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#YENTEN-(YTN)

class Table_YENTEN(Base):
    __tablename__ = 'YENTEN'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Helleniccoin-(HNC)

class Table_Helleniccoin(Base):
    __tablename__ = 'Helleniccoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Darsek-(KED)

class Table_Darsek(Base):
    __tablename__ = 'Darsek'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#ChessCoin-(CHESS)

class Table_ChessCoin(Base):
    __tablename__ = 'ChessCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Gapcoin-(GAP)

class Table_Gapcoin(Base):
    __tablename__ = 'Gapcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#CacheCoin-(CACH)

class Table_CacheCoin(Base):
    __tablename__ = 'CacheCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BitCoal-(COAL)

class Table_BitCoal(Base):
    __tablename__ = 'BitCoal'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#LitecoinPlus-(LCP)

class Table_LitecoinPlus(Base):
    __tablename__ = 'LitecoinPlus'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Motocoin-(MOTO)

class Table_Motocoin(Base):
    __tablename__ = 'Motocoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#SpaceCoin-(SPACE)

class Table_SpaceCoin(Base):
    __tablename__ = 'SpaceCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#ETHGAS-(EGAS)

class Table_ETHGAS(Base):
    __tablename__ = 'ETHGAS'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Bit20-(BTWTY)

class Table_Bit20(Base):
    __tablename__ = 'Bit20'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#SecureCoin-(SRC)

class Table_SecureCoin(Base):
    __tablename__ = 'SecureCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#PioneerCoin-(PCOIN)

class Table_PioneerCoin(Base):
    __tablename__ = 'PioneerCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#ChanCoin-(CHAN)

class Table_ChanCoin(Base):
    __tablename__ = 'ChanCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#CannaCoin-(CCN)

class Table_CannaCoin(Base):
    __tablename__ = 'CannaCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Prototanium-(PR)

class Table_Prototanium(Base):
    __tablename__ = 'Prototanium'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Mineum-(MNM)

class Table_Mineum(Base):
    __tablename__ = 'Mineum'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Ratecoin-(XRA)

class Table_Ratecoin(Base):
    __tablename__ = 'Ratecoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#PayCon-(CON)

class Table_PayCon(Base):
    __tablename__ = 'PayCon'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#EvilCoin-(EVIL)

class Table_EvilCoin(Base):
    __tablename__ = 'EvilCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Coin(O)-(CNO)

class Table_CoinO(Base):
    __tablename__ = 'CoinO'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Xios-(XIOS)

class Table_Xios(Base):
    __tablename__ = 'Xios'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Onix-(ONX)

class Table_Onix(Base):
    __tablename__ = 'Onix'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#FinCoin-(FNC)

class Table_FinCoin(Base):
    __tablename__ = 'FinCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#UniCoin-(UNIC)

class Table_UniCoin(Base):
    __tablename__ = 'UniCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#C-Bit-(XCT)

class Table_CBit(Base):
    __tablename__ = 'CBit'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#KushCoin-(KUSH)

class Table_KushCoin(Base):
    __tablename__ = 'KushCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#HiCoin-(XHI)

class Table_HiCoin(Base):
    __tablename__ = 'HiCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#UnityIngot-(UNY)

class Table_UnityIngot(Base):
    __tablename__ = 'UnityIngot'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Chronos-(CRX)

class Table_Chronos(Base):
    __tablename__ = 'Chronos'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#OctoCoin-(888)

class Table_OctoCoin(Base):
    __tablename__ = 'OctoCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Pakcoin-(PAK)

class Table_Pakcoin(Base):
    __tablename__ = 'Pakcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#GoldReserve-(XGR)

class Table_GoldReserve(Base):
    __tablename__ = 'GoldReserve'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Phoenixcoin-(PXC)

class Table_Phoenixcoin(Base):
    __tablename__ = 'Phoenixcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Grimcoin-(GRIM)

class Table_Grimcoin(Base):
    __tablename__ = 'Grimcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#PayCoin-(XPY)

class Table_PayCoin(Base):
    __tablename__ = 'PayCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Argentum-(ARG)

class Table_Argentum(Base):
    __tablename__ = 'Argentum'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Tigercoin-(TGC)

class Table_Tigercoin(Base):
    __tablename__ = 'Tigercoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Signatum-(SIGT)

class Table_Signatum(Base):
    __tablename__ = 'Signatum'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#AdvancedInternetBlocks-(AIB)

class Table_AdvancedInternetBlocks(Base):
    __tablename__ = 'AdvancedInternetBlocks'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#SwagBucks-(BUCKS)

class Table_SwagBucks(Base):
    __tablename__ = 'SwagBucks'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#PlatinumBAR-(XPTX)

class Table_PlatinumBAR(Base):
    __tablename__ = 'PlatinumBAR'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#RedCoin-(RED)

class Table_RedCoin(Base):
    __tablename__ = 'RedCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BitcoinFast-(BCF)

class Table_BitcoinFast(Base):
    __tablename__ = 'BitcoinFast'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BlockPay-(BLOCKPAY)

class Table_BlockPay(Base):
    __tablename__ = 'BlockPay'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Cryptojacks-(CJ)

class Table_Cryptojacks(Base):
    __tablename__ = 'Cryptojacks'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#DixAsset-(DIX)

class Table_DixAsset(Base):
    __tablename__ = 'DixAsset'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#GigaWattToken-(WTT)

class Table_GigaWattToken(Base):
    __tablename__ = 'GigaWattToken'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Opal-(OPAL)

class Table_Opal(Base):
    __tablename__ = 'Opal'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Joulecoin-(XJO)

class Table_Joulecoin(Base):
    __tablename__ = 'Joulecoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#GoldBlocks-(GB)

class Table_GoldBlocks(Base):
    __tablename__ = 'GoldBlocks'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#8Bit-(8BIT)

class Table_8Bit(Base):
    __tablename__ = '8Bit'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#EthereumDark-(ETHD)

class Table_EthereumDark(Base):
    __tablename__ = 'EthereumDark'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#CrystalClear-(CCT)

class Table_CrystalClear(Base):
    __tablename__ = 'CrystalClear'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#808Coin-(808)

class Table_808Coin(Base):
    __tablename__ = '808Coin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BlakeStar-(BLAS)

class Table_BlakeStar(Base):
    __tablename__ = 'BlakeStar'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#FUNCoin-(FUNC)

class Table_FUNCoin(Base):
    __tablename__ = 'FUNCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#WhaleCoin-(WHL)

class Table_WhaleCoin(Base):
    __tablename__ = 'WhaleCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#PostCoin-(POST)

class Table_PostCoin(Base):
    __tablename__ = 'PostCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#PascalLite-(PASL)

class Table_PascalLite(Base):
    __tablename__ = 'PascalLite'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Truckcoin-(TRK)

class Table_Truckcoin(Base):
    __tablename__ = 'Truckcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#IndependentMoneySystem-(IMS)

class Table_IndependentMoneySystem(Base):
    __tablename__ = 'IndependentMoneySystem'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Visio-(VISIO)

class Table_Visio(Base):
    __tablename__ = 'Visio'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Nyancoin-(NYAN)

class Table_Nyancoin(Base):
    __tablename__ = 'Nyancoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BritCoin-(BRIT)

class Table_BritCoin(Base):
    __tablename__ = 'BritCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#AmmoReloaded-(AMMO)

class Table_AmmoReloaded(Base):
    __tablename__ = 'AmmoReloaded'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#SugarExchange-(SGR)

class Table_SugarExchange(Base):
    __tablename__ = 'SugarExchange'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Rimbit-(RBT)

class Table_Rimbit(Base):
    __tablename__ = 'Rimbit'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Coin2.1-(C2)

class Table_Coin21(Base):
    __tablename__ = 'Coin21'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Veltor-(VLT)

class Table_Veltor(Base):
    __tablename__ = 'Veltor'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#VirtualCoin-(VC)

class Table_VirtualCoin(Base):
    __tablename__ = 'VirtualCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#WavesGo-(WGO)

class Table_WavesGo(Base):
    __tablename__ = 'WavesGo'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Octanox-(OTX)

class Table_Octanox(Base):
    __tablename__ = 'Octanox'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#LanaCoin-(LANA)

class Table_LanaCoin(Base):
    __tablename__ = 'LanaCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#AdCoin-(ACC)

class Table_AdCoin(Base):
    __tablename__ = 'AdCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#SuperCoin-(SUPER)

class Table_SuperCoin(Base):
    __tablename__ = 'SuperCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#DROXNE-(DRXNE)

class Table_DROXNE(Base):
    __tablename__ = 'DROXNE'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Titcoin-(TIT)

class Table_Titcoin(Base):
    __tablename__ = 'Titcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Kobocoin-(KOBO)

class Table_Kobocoin(Base):
    __tablename__ = 'Kobocoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BigUp-(BIGUP)

class Table_BigUp(Base):
    __tablename__ = 'BigUp'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#I0Coin-(I0C)

class Table_I0Coin(Base):
    __tablename__ = 'I0Coin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Zlancer-(ZCG)

class Table_Zlancer(Base):
    __tablename__ = 'Zlancer'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Bitstar-(BITS)

class Table_Bitstar(Base):
    __tablename__ = 'Bitstar'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Piggycoin-(PIGGY)

class Table_Piggycoin(Base):
    __tablename__ = 'Piggycoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#AmsterdamCoin-(AMS)

class Table_AmsterdamCoin(Base):
    __tablename__ = 'AmsterdamCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#PetroDollar-(XPD)

class Table_PetroDollar(Base):
    __tablename__ = 'PetroDollar'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Guncoin-(GUN)

class Table_Guncoin(Base):
    __tablename__ = 'Guncoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#MaxCoin-(MAX)

class Table_MaxCoin(Base):
    __tablename__ = 'MaxCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BitcoinRed-(BTCRED)

class Table_BitcoinRed(Base):
    __tablename__ = 'BitcoinRed'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#TittieCoin-(TTC)

class Table_TittieCoin(Base):
    __tablename__ = 'TittieCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#HoboNickels-(HBN)

class Table_HoboNickels(Base):
    __tablename__ = 'HoboNickels'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Happycoin-(HPC)

class Table_Happycoin(Base):
    __tablename__ = 'Happycoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BitparkCoin-(BPC)

class Table_BitparkCoin(Base):
    __tablename__ = 'BitparkCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#ICOOpenLedger-(ICOO)

class Table_ICOOpenLedger(Base):
    __tablename__ = 'ICOOpenLedger'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Confido-(CFD)

class Table_Confido(Base):
    __tablename__ = 'Confido'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#MojoCoin-(MOJO)

class Table_MojoCoin(Base):
    __tablename__ = 'MojoCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#SmileyCoin-(SMLY)

class Table_SmileyCoin(Base):
    __tablename__ = 'SmileyCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#UltraCoin-(UTC)

class Table_UltraCoin(Base):
    __tablename__ = 'UltraCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Triangles-(TRI)

class Table_Triangles(Base):
    __tablename__ = 'Triangles'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#DigiCube-(CUBE)

class Table_DigiCube(Base):
    __tablename__ = 'DigiCube'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#GAIA-(GAIA)

class Table_GAIA(Base):
    __tablename__ = 'GAIA'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#SkinCoin-(SKIN)

class Table_SkinCoin(Base):
    __tablename__ = 'SkinCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Bitcurrency-(BTCR)

class Table_Bitcurrency(Base):
    __tablename__ = 'Bitcurrency'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Dollarcoin-(DLC)

class Table_Dollarcoin(Base):
    __tablename__ = 'Dollarcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#TrumpCoin-(TRUMP)

class Table_TrumpCoin(Base):
    __tablename__ = 'TrumpCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#QubitCoin-(Q2C)

class Table_QubitCoin(Base):
    __tablename__ = 'QubitCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#PoSToken-(POS)

class Table_PoSToken(Base):
    __tablename__ = 'PoSToken'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BitBar-(BTB)

class Table_BitBar(Base):
    __tablename__ = 'BitBar'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#CryptoInsight-(TKR)

class Table_CryptoInsight(Base):
    __tablename__ = 'CryptoInsight'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#DaxxCoin-(DAXX)

class Table_DaxxCoin(Base):
    __tablename__ = 'DaxxCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BillionaireToken-(XBL)

class Table_BillionaireToken(Base):
    __tablename__ = 'BillionaireToken'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Ccore-(CCO)

class Table_Ccore(Base):
    __tablename__ = 'Ccore'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#42-coin-(42)

class Table_42coin(Base):
    __tablename__ = '42coin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Aricoin-(ARI)

class Table_Aricoin(Base):
    __tablename__ = 'Aricoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#StarCredits-(STRC)

class Table_StarCredits(Base):
    __tablename__ = 'StarCredits'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#iEthereum-(IETH)

class Table_iEthereum(Base):
    __tablename__ = 'iEthereum'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#ShadowCash-(SDC)

class Table_ShadowCash(Base):
    __tablename__ = 'ShadowCash'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Nekonium-(NUKO)

class Table_Nekonium(Base):
    __tablename__ = 'Nekonium'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Zennies-(ZENI)

class Table_Zennies(Base):
    __tablename__ = 'Zennies'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#RasputinOnlineCoin-(ROC)

class Table_RasputinOnlineCoin(Base):
    __tablename__ = 'RasputinOnlineCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#iTicoin-(ITI)

class Table_iTicoin(Base):
    __tablename__ = 'iTicoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#CoinonatX-(XCXT)

class Table_CoinonatX(Base):
    __tablename__ = 'CoinonatX'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BiblePay-(BBP)

class Table_BiblePay(Base):
    __tablename__ = 'BiblePay'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#HOdlcoin-(HODL)

class Table_HOdlcoin(Base):
    __tablename__ = 'HOdlcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Fantomcoin-(FCN)

class Table_Fantomcoin(Base):
    __tablename__ = 'Fantomcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Netko-(NETKO)

class Table_Netko(Base):
    __tablename__ = 'Netko'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Authorship-(ATS)

class Table_Authorship(Base):
    __tablename__ = 'Authorship'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#AtomicCoin-(ATOM)

class Table_AtomicCoin(Base):
    __tablename__ = 'AtomicCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#EthBet-(EBET)

class Table_EthBet(Base):
    __tablename__ = 'EthBet'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Minereum-(MNE)

class Table_Minereum(Base):
    __tablename__ = 'Minereum'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#StarCashNetwork-(STARS)

class Table_StarCashNetwork(Base):
    __tablename__ = 'StarCashNetwork'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Kurrent-(KURT)

class Table_Kurrent(Base):
    __tablename__ = 'Kurrent'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#GrowersInternational-(GRWI)

class Table_GrowersInternational(Base):
    __tablename__ = 'GrowersInternational'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Zetacoin-(ZET)

class Table_Zetacoin(Base):
    __tablename__ = 'Zetacoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#FuelCoin-(FC2)

class Table_FuelCoin(Base):
    __tablename__ = 'FuelCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Trollcoin-(TROLL)

class Table_Trollcoin(Base):
    __tablename__ = 'Trollcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Fastcoin-(FST)

class Table_Fastcoin(Base):
    __tablename__ = 'Fastcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#PiplCoin-(PIPL)

class Table_PiplCoin(Base):
    __tablename__ = 'PiplCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#DeutscheeMark-(DEM)

class Table_DeutscheeMark(Base):
    __tablename__ = 'DeutscheeMark'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#MonsterByte-(MBI)

class Table_MonsterByte(Base):
    __tablename__ = 'MonsterByte'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Eternity-(ENT)

class Table_Eternity(Base):
    __tablename__ = 'Eternity'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Tracto-(TRCT)

class Table_Tracto(Base):
    __tablename__ = 'Tracto'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#HitCoin-(HTC)

class Table_HitCoin(Base):
    __tablename__ = 'HitCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Desire-(DSR)

class Table_Desire(Base):
    __tablename__ = 'Desire'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#DFSCoin-(DFS)

class Table_DFSCoin(Base):
    __tablename__ = 'DFSCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#AcceleratorNetwork-(ACC)

class Table_AcceleratorNetwork(Base):
    __tablename__ = 'AcceleratorNetwork'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Digitalcoin-(DGC)

class Table_Digitalcoin(Base):
    __tablename__ = 'Digitalcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Capricoin-(CPC)

class Table_Capricoin(Base):
    __tablename__ = 'Capricoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Miners'RewardToken-(MRT)

class Table_MinersRewardToken(Base):
    __tablename__ = 'MinersRewardToken'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#KekCoin-(KEK)

class Table_KekCoin(Base):
    __tablename__ = 'KekCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#SagaCoin-(SAGA)

class Table_SagaCoin(Base):
    __tablename__ = 'SagaCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#FuckToken-(FUCK)

class Table_FuckToken(Base):
    __tablename__ = 'FuckToken'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#SmartCoin-(SMC)

class Table_SmartCoin(Base):
    __tablename__ = 'SmartCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#CryptoCarbon-(CCRB)

class Table_CryptoCarbon(Base):
    __tablename__ = 'CryptoCarbon'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Orbitcoin-(ORB)

class Table_Orbitcoin(Base):
    __tablename__ = 'Orbitcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Machinecoin-(MAC)

class Table_Machinecoin(Base):
    __tablename__ = 'Machinecoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Janus-(JNS)

class Table_Janus(Base):
    __tablename__ = 'Janus'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#DraftCoin-(DFT)

class Table_DraftCoin(Base):
    __tablename__ = 'DraftCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#CryptoForecast-(CFT)

class Table_CryptoForecast(Base):
    __tablename__ = 'CryptoForecast'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Elcoin-(EL)

class Table_Elcoin(Base):
    __tablename__ = 'Elcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#AurumCoin-(AU)

class Table_AurumCoin(Base):
    __tablename__ = 'AurumCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Greencoin-(GRE)

class Table_Greencoin(Base):
    __tablename__ = 'Greencoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#SteneumCoin-(STN)

class Table_SteneumCoin(Base):
    __tablename__ = 'SteneumCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#MazaCoin-(MZC)

class Table_MazaCoin(Base):
    __tablename__ = 'MazaCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Bytecent-(BYC)

class Table_Bytecent(Base):
    __tablename__ = 'Bytecent'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#MACRON-(MCRN)

class Table_MACRON(Base):
    __tablename__ = 'MACRON'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#AltCommunityCoin-(ALTCOM)

class Table_AltCommunityCoin(Base):
    __tablename__ = 'AltCommunityCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Influxcoin-(INFX)

class Table_Influxcoin(Base):
    __tablename__ = 'Influxcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#TeslaCoin-(TES)

class Table_TeslaCoin(Base):
    __tablename__ = 'TeslaCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Elementrem-(ELE)

class Table_Elementrem(Base):
    __tablename__ = 'Elementrem'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#InflationCoin-(IFLT)

class Table_InflationCoin(Base):
    __tablename__ = 'InflationCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#UnbreakableCoin-(UNB)

class Table_UnbreakableCoin(Base):
    __tablename__ = 'UnbreakableCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#LiteDoge-(LDOGE)

class Table_LiteDoge(Base):
    __tablename__ = 'LiteDoge'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#SmartInvestmentFundToken-(SIFT)

class Table_SmartInvestmentFundToken(Base):
    __tablename__ = 'SmartInvestmentFundToken'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Oceanlab-(OCL)

class Table_Oceanlab(Base):
    __tablename__ = 'Oceanlab'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Kolion-(KLN)

class Table_Kolion(Base):
    __tablename__ = 'Kolion'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#FujiCoin-(FJC)

class Table_FujiCoin(Base):
    __tablename__ = 'FujiCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#LegendsRoom-(LGD)

class Table_LegendsRoom(Base):
    __tablename__ = 'LegendsRoom'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Cryptonite-(XCN)

class Table_Cryptonite(Base):
    __tablename__ = 'Cryptonite'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Unitus-(UIS)

class Table_Unitus(Base):
    __tablename__ = 'Unitus'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Scorecoin-(SCORE)

class Table_Scorecoin(Base):
    __tablename__ = 'Scorecoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#LinkPlatform-(LNK)

class Table_LinkPlatform(Base):
    __tablename__ = 'LinkPlatform'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#NetCoin-(NET)

class Table_NetCoin(Base):
    __tablename__ = 'NetCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#InsaneCoin-(INSN)

class Table_InsaneCoin(Base):
    __tablename__ = 'InsaneCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Cream-(CRM)

class Table_Cream(Base):
    __tablename__ = 'Cream'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Jetcoin-(JET)

class Table_Jetcoin(Base):
    __tablename__ = 'Jetcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#EthereumGold-(ETG)

class Table_EthereumGold(Base):
    __tablename__ = 'EthereumGold'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#FundYourselfNow-(FYN)

class Table_FundYourselfNow(Base):
    __tablename__ = 'FundYourselfNow'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Ethbits-(ETBS)

class Table_Ethbits(Base):
    __tablename__ = 'Ethbits'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Etheriya-(RIYA)

class Table_Etheriya(Base):
    __tablename__ = 'Etheriya'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Copico-(XCPO)

class Table_Copico(Base):
    __tablename__ = 'Copico'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Version-(V)

class Table_Version(Base):
    __tablename__ = 'Version'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#CampusCoin-(CMPCO)

class Table_CampusCoin(Base):
    __tablename__ = 'CampusCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Adzcoin-(ADZ)

class Table_Adzcoin(Base):
    __tablename__ = 'Adzcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Starta-(STA)

class Table_Starta(Base):
    __tablename__ = 'Starta'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Electra-(ECA)

class Table_Electra(Base):
    __tablename__ = 'Electra'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#CanadaeCoin-(CDN)

class Table_CanadaeCoin(Base):
    __tablename__ = 'CanadaeCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Renos-(RNS)

class Table_Renos(Base):
    __tablename__ = 'Renos'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#ERC20-(ERC20)

class Table_ERC20(Base):
    __tablename__ = 'ERC20'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Moin-(MOIN)

class Table_Moin(Base):
    __tablename__ = 'Moin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#IntelligentTradingTech-(ITT)

class Table_IntelligentTradingTech(Base):
    __tablename__ = 'IntelligentTradingTech'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Darcrus-(DAR)

class Table_Darcrus(Base):
    __tablename__ = 'Darcrus'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#MonkeyProject-(MONK)

class Table_MonkeyProject(Base):
    __tablename__ = 'MonkeyProject'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#DigitalPrice-(DP)

class Table_DigitalPrice(Base):
    __tablename__ = 'DigitalPrice'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Bata-(BTA)

class Table_Bata(Base):
    __tablename__ = 'Bata'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Unify-(UNIFY)

class Table_Unify(Base):
    __tablename__ = 'Unify'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Bitradio-(BRO)

class Table_Bitradio(Base):
    __tablename__ = 'Bitradio'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Emphy-(EPY)

class Table_Emphy(Base):
    __tablename__ = 'Emphy'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#LeviarCoin-(XLC)

class Table_LeviarCoin(Base):
    __tablename__ = 'LeviarCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#FlutterCoin-(FLT)

class Table_FlutterCoin(Base):
    __tablename__ = 'FlutterCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#PrimalbaseToken-(PBT)

class Table_PrimalbaseToken(Base):
    __tablename__ = 'PrimalbaseToken'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Centurion-(CNT)

class Table_Centurion(Base):
    __tablename__ = 'Centurion'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Condensate-(RAIN)

class Table_Condensate(Base):
    __tablename__ = 'Condensate'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Abjcoin-(ABJ)

class Table_Abjcoin(Base):
    __tablename__ = 'Abjcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#e-Gulden-(EFL)

class Table_eGulden(Base):
    __tablename__ = 'eGulden'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#EthereumCash-(ECASH)

class Table_EthereumCash(Base):
    __tablename__ = 'EthereumCash'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Dinastycoin-(DCY)

class Table_Dinastycoin(Base):
    __tablename__ = 'Dinastycoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Yocoin-(YOC)

class Table_Yocoin(Base):
    __tablename__ = 'Yocoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#CryptoBullion-(CBX)

class Table_CryptoBullion(Base):
    __tablename__ = 'CryptoBullion'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#InterstellarHoldings-(HOLD)

class Table_InterstellarHoldings(Base):
    __tablename__ = 'InterstellarHoldings'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Goodomy-(GOOD)

class Table_Goodomy(Base):
    __tablename__ = 'Goodomy'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#MCAP-(MCAP)

class Table_MCAP(Base):
    __tablename__ = 'MCAP'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Hawala.Today-(HAT)

class Table_HawalaToday(Base):
    __tablename__ = 'HawalaToday'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#STRAKS-(STAK)

class Table_STRAKS(Base):
    __tablename__ = 'STRAKS'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BitcoinScrypt-(BTCS)

class Table_BitcoinScrypt(Base):
    __tablename__ = 'BitcoinScrypt'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#PopularCoin-(POP)

class Table_PopularCoin(Base):
    __tablename__ = 'PopularCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Megacoin-(MEC)

class Table_Megacoin(Base):
    __tablename__ = 'Megacoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Denarius-(DNR)

class Table_Denarius(Base):
    __tablename__ = 'Denarius'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BlueCoin-(BLU)

class Table_BlueCoin(Base):
    __tablename__ = 'BlueCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#ArcticCoin-(ARC)

class Table_ArcticCoin(Base):
    __tablename__ = 'ArcticCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#CryptoPing-(PING)

class Table_CryptoPing(Base):
    __tablename__ = 'CryptoPing'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Qvolta-(QVT)

class Table_Qvolta(Base):
    __tablename__ = 'Qvolta'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#FLiK-(FLIK)

class Table_FLiK(Base):
    __tablename__ = 'FLiK'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Gimli-(GIM)

class Table_Gimli(Base):
    __tablename__ = 'Gimli'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#CHIPS-(CHIPS)

class Table_CHIPS(Base):
    __tablename__ = 'CHIPS'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Anoncoin-(ANC)

class Table_Anoncoin(Base):
    __tablename__ = 'Anoncoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#NEVERDIE-(NDC)

class Table_NEVERDIE(Base):
    __tablename__ = 'NEVERDIE'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#CarTaxiToken-(CTX)

class Table_CarTaxiToken(Base):
    __tablename__ = 'CarTaxiToken'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#ELTCOIN-(ELTCOIN)

class Table_ELTCOIN(Base):
    __tablename__ = 'ELTCOIN'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#SmartBillions-(SMART)

class Table_SmartBillions(Base):
    __tablename__ = 'SmartBillions'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Halcyon-(HAL)

class Table_Halcyon(Base):
    __tablename__ = 'Halcyon'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#MarteXcoin-(MXT)

class Table_MarteXcoin(Base):
    __tablename__ = 'MarteXcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BitBoost-(BBT)

class Table_BitBoost(Base):
    __tablename__ = 'BitBoost'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#bitJob-(STU)

class Table_bitJob(Base):
    __tablename__ = 'bitJob'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#ParkByte-(PKB)

class Table_ParkByte(Base):
    __tablename__ = 'ParkByte'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Linx-(LINX)

class Table_Linx(Base):
    __tablename__ = 'Linx'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Karbo-(KRB)

class Table_Karbo(Base):
    __tablename__ = 'Karbo'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#APX-(APX)

class Table_APX(Base):
    __tablename__ = 'APX'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#FORCE-(FOR)

class Table_FORCE(Base):
    __tablename__ = 'FORCE'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#NobleCoin-(NOBL)

class Table_NobleCoin(Base):
    __tablename__ = 'NobleCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Regalcoin-(REC)

class Table_Regalcoin(Base):
    __tablename__ = 'Regalcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#EverGreenCoin-(EGC)

class Table_EverGreenCoin(Base):
    __tablename__ = 'EverGreenCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#HunterCoin-(HUC)

class Table_HunterCoin(Base):
    __tablename__ = 'HunterCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#PutinCoin-(PUT)

class Table_PutinCoin(Base):
    __tablename__ = 'PutinCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Zephyr-(ZEPH)

class Table_Zephyr(Base):
    __tablename__ = 'Zephyr'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#ZrCoin-(ZRC)

class Table_ZrCoin(Base):
    __tablename__ = 'ZrCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Dynamic-(DYN)

class Table_Dynamic(Base):
    __tablename__ = 'Dynamic'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#LuckChain-(BASH)

class Table_LuckChain(Base):
    __tablename__ = 'LuckChain'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#FootyCash-(XFT)

class Table_FootyCash(Base):
    __tablename__ = 'FootyCash'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Quark-(QRK)

class Table_Quark(Base):
    __tablename__ = 'Quark'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#PureVidz-(VIDZ)

class Table_PureVidz(Base):
    __tablename__ = 'PureVidz'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#REAL-(REAL)

class Table_REAL(Base):
    __tablename__ = 'REAL'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Zeitcoin-(ZEIT)

class Table_Zeitcoin(Base):
    __tablename__ = 'Zeitcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Terracoin-(TRC)

class Table_Terracoin(Base):
    __tablename__ = 'Terracoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Embers-(MBRS)

class Table_Embers(Base):
    __tablename__ = 'Embers'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#WorldCoin-(WDC)

class Table_WorldCoin(Base):
    __tablename__ = 'WorldCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Magi-(XMG)

class Table_Magi(Base):
    __tablename__ = 'Magi'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Dai-(DAI)

class Table_Dai(Base):
    __tablename__ = 'Dai'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#EquiTrader-(EQT)

class Table_EquiTrader(Base):
    __tablename__ = 'EquiTrader'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#ProCurrency-(PROC)

class Table_ProCurrency(Base):
    __tablename__ = 'ProCurrency'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#EuropeCoin-(ERC)

class Table_EuropeCoin(Base):
    __tablename__ = 'EuropeCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Farad-(FRD)

class Table_Farad(Base):
    __tablename__ = 'Farad'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Sexcoin-(SXC)

class Table_Sexcoin(Base):
    __tablename__ = 'Sexcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Tokes-(TKS)

class Table_Tokes(Base):
    __tablename__ = 'Tokes'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#CommodityAdNetwork-(CDX)

class Table_CommodityAdNetwork(Base):
    __tablename__ = 'CommodityAdNetwork'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#eBoost-(EBST)

class Table_eBoost(Base):
    __tablename__ = 'eBoost'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Ellaism-(ELLA)

class Table_Ellaism(Base):
    __tablename__ = 'Ellaism'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#eBitcoin-(EBTC)

class Table_eBitcoin(Base):
    __tablename__ = 'eBitcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Eroscoin-(ERO)

class Table_Eroscoin(Base):
    __tablename__ = 'Eroscoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Altcoin-(ALT)

class Table_Altcoin(Base):
    __tablename__ = 'Altcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#EncryptoTel[WAVES]-(ETT)

class Table_EncryptoTelWAVES(Base):
    __tablename__ = 'EncryptoTelWAVES'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Ixcoin-(IXC)

class Table_Ixcoin(Base):
    __tablename__ = 'Ixcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#WandX-(WAND)

class Table_WandX(Base):
    __tablename__ = 'WandX'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Sharechain-(SSS)

class Table_Sharechain(Base):
    __tablename__ = 'Sharechain'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#TrustPlus-(TRUST)

class Table_TrustPlus(Base):
    __tablename__ = 'TrustPlus'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#XGOX-(XGOX)

class Table_XGOX(Base):
    __tablename__ = 'XGOX'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#ProjectDecorum-(PDC)

class Table_ProjectDecorum(Base):
    __tablename__ = 'ProjectDecorum'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#1337-(1337)

class Table_1337(Base):
    __tablename__ = '1337'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Pure-(PURE)

class Table_Pure(Base):
    __tablename__ = 'Pure'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Social-(SCL)

class Table_Social(Base):
    __tablename__ = 'Social'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Dotcoin-(DOT)

class Table_Dotcoin(Base):
    __tablename__ = 'Dotcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#ToaCoin-(TOA)

class Table_ToaCoin(Base):
    __tablename__ = 'ToaCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Adelphoi-(ADL)

class Table_Adelphoi(Base):
    __tablename__ = 'Adelphoi'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#vTorrent-(VTR)

class Table_vTorrent(Base):
    __tablename__ = 'vTorrent'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#2GIVE-(2GIVE)

class Table_2GIVE(Base):
    __tablename__ = '2GIVE'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BuzzCoin-(BUZZ)

class Table_BuzzCoin(Base):
    __tablename__ = 'BuzzCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#TrueFlip-(TFL)

class Table_TrueFlip(Base):
    __tablename__ = 'TrueFlip'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#ExclusiveCoin-(EXCL)

class Table_ExclusiveCoin(Base):
    __tablename__ = 'ExclusiveCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#HubiiNetwork-(HBT)

class Table_HubiiNetwork(Base):
    __tablename__ = 'HubiiNetwork'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#RoyalKingdomCoin-(RKC)

class Table_RoyalKingdomCoin(Base):
    __tablename__ = 'RoyalKingdomCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Internxt-(INXT)

class Table_Internxt(Base):
    __tablename__ = 'Internxt'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#HollyWoodCoin-(HWC)

class Table_HollyWoodCoin(Base):
    __tablename__ = 'HollyWoodCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#VIVO-(VIVO)

class Table_VIVO(Base):
    __tablename__ = 'VIVO'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Creativecoin-(CREA)

class Table_Creativecoin(Base):
    __tablename__ = 'Creativecoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Bowhead-(AHT)

class Table_Bowhead(Base):
    __tablename__ = 'Bowhead'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Startcoin-(START)

class Table_Startcoin(Base):
    __tablename__ = 'Startcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#PRIZM-(PZM)

class Table_PRIZM(Base):
    __tablename__ = 'PRIZM'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#DigiPulse-(DGPT)

class Table_DigiPulse(Base):
    __tablename__ = 'DigiPulse'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Rupee-(RUP)

class Table_Rupee(Base):
    __tablename__ = 'Rupee'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Privatix-(PRIX)

class Table_Privatix(Base):
    __tablename__ = 'Privatix'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#E-DinarCoin-(EDR)

class Table_EDinarCoin(Base):
    __tablename__ = 'EDinarCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Carboncoin-(CARBON)

class Table_Carboncoin(Base):
    __tablename__ = 'Carboncoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BreakoutStake-(BRX)

class Table_BreakoutStake(Base):
    __tablename__ = 'BreakoutStake'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#DCORP-(DRP)

class Table_DCORP(Base):
    __tablename__ = 'DCORP'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BitcoinZ-(BTCZ)

class Table_BitcoinZ(Base):
    __tablename__ = 'BitcoinZ'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Bitcloud-(BTDX)

class Table_Bitcloud(Base):
    __tablename__ = 'Bitcloud'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#ChainCoin-(CHC)

class Table_ChainCoin(Base):
    __tablename__ = 'ChainCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#vSlice-(VSL)

class Table_vSlice(Base):
    __tablename__ = 'vSlice'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Kore-(KORE)

class Table_Kore(Base):
    __tablename__ = 'Kore'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#NuBits-(USNBT)

class Table_NuBits(Base):
    __tablename__ = 'NuBits'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Breakout-(BRK)

class Table_Breakout(Base):
    __tablename__ = 'Breakout'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#IndorseToken-(IND)

class Table_IndorseToken(Base):
    __tablename__ = 'IndorseToken'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BitcoinPlus-(XBC)

class Table_BitcoinPlus(Base):
    __tablename__ = 'BitcoinPlus'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#CrowdCoin-(CRC)

class Table_CrowdCoin(Base):
    __tablename__ = 'CrowdCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Synergy-(SNRG)

class Table_Synergy(Base):
    __tablename__ = 'Synergy'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#GoldCoin-(GLD)

class Table_GoldCoin(Base):
    __tablename__ = 'GoldCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Auroracoin-(AUR)

class Table_Auroracoin(Base):
    __tablename__ = 'Auroracoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#DNotes-(NOTE)

class Table_DNotes(Base):
    __tablename__ = 'DNotes'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Blitzcash-(BLITZ)

class Table_Blitzcash(Base):
    __tablename__ = 'Blitzcash'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Astro-(ASTRO)

class Table_Astro(Base):
    __tablename__ = 'Astro'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#B2B-(B2B)

class Table_B2B(Base):
    __tablename__ = 'B2B'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#VeriumReserve-(VRM)

class Table_VeriumReserve(Base):
    __tablename__ = 'VeriumReserve'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#HyperStake-(HYP)

class Table_HyperStake(Base):
    __tablename__ = 'HyperStake'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Memetic/PepeCoin-(MEME)

class Table_MemeticPepeCoin(Base):
    __tablename__ = 'MemeticPepeCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#TheChampCoin-(TCC)

class Table_TheChampCoin(Base):
    __tablename__ = 'TheChampCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Blockpool-(BPL)

class Table_Blockpool(Base):
    __tablename__ = 'Blockpool'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Syndicate-(SYNX)

class Table_Syndicate(Base):
    __tablename__ = 'Syndicate'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#IntenseCoin-(ITNS)

class Table_IntenseCoin(Base):
    __tablename__ = 'IntenseCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Masternodecoin-(MTNC)

class Table_Masternodecoin(Base):
    __tablename__ = 'Masternodecoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Tao-(XTO)

class Table_Tao(Base):
    __tablename__ = 'Tao'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#CannabisCoin-(CANN)

class Table_CannabisCoin(Base):
    __tablename__ = 'CannabisCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Crave-(CRAVE)

class Table_Crave(Base):
    __tablename__ = 'Crave'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Zero-(ZER)

class Table_Zero(Base):
    __tablename__ = 'Zero'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#WildCrypto-(WILD)

class Table_WildCrypto(Base):
    __tablename__ = 'WildCrypto'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Novacoin-(NVC)

class Table_Novacoin(Base):
    __tablename__ = 'Novacoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Riecoin-(RIC)

class Table_Riecoin(Base):
    __tablename__ = 'Riecoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#UniversalCurrency-(UNIT)

class Table_UniversalCurrency(Base):
    __tablename__ = 'UniversalCurrency'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Bela-(BELA)

class Table_Bela(Base):
    __tablename__ = 'Bela'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#REX-(REX)

class Table_REX(Base):
    __tablename__ = 'REX'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#DopeCoin-(DOPE)

class Table_DopeCoin(Base):
    __tablename__ = 'DopeCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#TransferCoin-(TX)

class Table_TransferCoin(Base):
    __tablename__ = 'TransferCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Opus-(OPT)

class Table_Opus(Base):
    __tablename__ = 'Opus'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Bonpay-(BON)

class Table_Bonpay(Base):
    __tablename__ = 'Bonpay'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Qwark-(QWARK)

class Table_Qwark(Base):
    __tablename__ = 'Qwark'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#UFOCoin-(UFO)

class Table_UFOCoin(Base):
    __tablename__ = 'UFOCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Bitzeny-(ZNY)

class Table_Bitzeny(Base):
    __tablename__ = 'Bitzeny'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#RussiaCoin-(RC)

class Table_RussiaCoin(Base):
    __tablename__ = 'RussiaCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Creditbit-(CRB)

class Table_Creditbit(Base):
    __tablename__ = 'Creditbit'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Hacken-(HKN)

class Table_Hacken(Base):
    __tablename__ = 'Hacken'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#TrezarCoin-(TZC)

class Table_TrezarCoin(Base):
    __tablename__ = 'TrezarCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Lampix-(PIX)

class Table_Lampix(Base):
    __tablename__ = 'Lampix'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#HEROcoin-(PLAY)

class Table_HEROcoin(Base):
    __tablename__ = 'HEROcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Sprouts-(SPRTS)

class Table_Sprouts(Base):
    __tablename__ = 'Sprouts'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#ExchangeUnion-(XUC)

class Table_ExchangeUnion(Base):
    __tablename__ = 'ExchangeUnion'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Innova-(INN)

class Table_Innova(Base):
    __tablename__ = 'Innova'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Pesetacoin-(PTC)

class Table_Pesetacoin(Base):
    __tablename__ = 'Pesetacoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#ProChain-(PRO)

class Table_ProChain(Base):
    __tablename__ = 'ProChain'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#SpreadCoin-(SPR)

class Table_SpreadCoin(Base):
    __tablename__ = 'SpreadCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Pluton-(PLU)

class Table_Pluton(Base):
    __tablename__ = 'Pluton'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#MyWish-(WISH)

class Table_MyWish(Base):
    __tablename__ = 'MyWish'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Curecoin-(CURE)

class Table_Curecoin(Base):
    __tablename__ = 'Curecoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#HelloGold-(HGT)

class Table_HelloGold(Base):
    __tablename__ = 'HelloGold'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Upfiring-(UFR)

class Table_Upfiring(Base):
    __tablename__ = 'Upfiring'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#EarthCoin-(EAC)

class Table_EarthCoin(Base):
    __tablename__ = 'EarthCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#CVCoin-(CVCOIN)

class Table_CVCoin(Base):
    __tablename__ = 'CVCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Sumokoin-(SUMO)

class Table_Sumokoin(Base):
    __tablename__ = 'Sumokoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#NVO-(NVST)

class Table_NVO(Base):
    __tablename__ = 'NVO'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Etheroll-(DICE)

class Table_Etheroll(Base):
    __tablename__ = 'Etheroll'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Bitdeal-(BDL)

class Table_Bitdeal(Base):
    __tablename__ = 'Bitdeal'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Atmos-(ATMS)

class Table_Atmos(Base):
    __tablename__ = 'Atmos'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Bitmark-(BTM)

class Table_Bitmark(Base):
    __tablename__ = 'Bitmark'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Magnet-(MAG)

class Table_Magnet(Base):
    __tablename__ = 'Magnet'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#OBITS-(OBITS)

class Table_OBITS(Base):
    __tablename__ = 'OBITS'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Sphere-(SPHR)

class Table_Sphere(Base):
    __tablename__ = 'Sphere'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#PinkCoin-(PINK)

class Table_PinkCoin(Base):
    __tablename__ = 'PinkCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Vsync-(VSX)

class Table_Vsync(Base):
    __tablename__ = 'Vsync'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#AdShares-(ADST)

class Table_AdShares(Base):
    __tablename__ = 'AdShares'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Primecoin-(XPM)

class Table_Primecoin(Base):
    __tablename__ = 'Primecoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#SportyFi-(SPF)

class Table_SportyFi(Base):
    __tablename__ = 'SportyFi'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#FlypMe-(FYP)

class Table_FlypMe(Base):
    __tablename__ = 'FlypMe'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Ecobit-(ECOB)

class Table_Ecobit(Base):
    __tablename__ = 'Ecobit'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#FirstCoin-(FRST)

class Table_FirstCoin(Base):
    __tablename__ = 'FirstCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#SocialSend-(SEND)

class Table_SocialSend(Base):
    __tablename__ = 'SocialSend'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#RussianMinerCoin-(RMC)

class Table_RussianMinerCoin(Base):
    __tablename__ = 'RussianMinerCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Vcash-(XVC)

class Table_Vcash(Base):
    __tablename__ = 'Vcash'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Flixxo-(FLIXX)

class Table_Flixxo(Base):
    __tablename__ = 'Flixxo'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Pirl-(PIRL)

class Table_Pirl(Base):
    __tablename__ = 'Pirl'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BitDice-(CSNO)

class Table_BitDice(Base):
    __tablename__ = 'BitDice'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#QunQun-(QUN)

class Table_QunQun(Base):
    __tablename__ = 'QunQun'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#OracleChain-(OCT)

class Table_OracleChain(Base):
    __tablename__ = 'OracleChain'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Mysterium-(MYST)

class Table_Mysterium(Base):
    __tablename__ = 'Mysterium'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Solaris-(XLR)

class Table_Solaris(Base):
    __tablename__ = 'Solaris'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Espers-(ESP)

class Table_Espers(Base):
    __tablename__ = 'Espers'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Unobtanium-(UNO)

class Table_Unobtanium(Base):
    __tablename__ = 'Unobtanium'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Autonio-(NIO)

class Table_Autonio(Base):
    __tablename__ = 'Autonio'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#LockChain-(LOC)

class Table_LockChain(Base):
    __tablename__ = 'LockChain'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Primas-(PST)

class Table_Primas(Base):
    __tablename__ = 'Primas'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#AudioCoin-(ADC)

class Table_AudioCoin(Base):
    __tablename__ = 'AudioCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Aventus-(AVT)

class Table_Aventus(Base):
    __tablename__ = 'Aventus'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Xaurum-(XAUR)

class Table_Xaurum(Base):
    __tablename__ = 'Xaurum'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Boolberry-(BBR)

class Table_Boolberry(Base):
    __tablename__ = 'Boolberry'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Sequence-(SEQ)

class Table_Sequence(Base):
    __tablename__ = 'Sequence'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Zoin-(ZOI)

class Table_Zoin(Base):
    __tablename__ = 'Zoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BitSend-(BSD)

class Table_BitSend(Base):
    __tablename__ = 'BitSend'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#InternetofPeople-(IOP)

class Table_InternetofPeople(Base):
    __tablename__ = 'InternetofPeople'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#DAO.Casino-(BET)

class Table_DAOCasino(Base):
    __tablename__ = 'DAOCasino'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Monoeci-(XMCC)

class Table_Monoeci(Base):
    __tablename__ = 'Monoeci'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#GeoCoin-(GEO)

class Table_GeoCoin(Base):
    __tablename__ = 'GeoCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Bulwark-(BWK)

class Table_Bulwark(Base):
    __tablename__ = 'Bulwark'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Chronobank-(TIME)

class Table_Chronobank(Base):
    __tablename__ = 'Chronobank'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#MercuryProtocol-(GMT)

class Table_MercuryProtocol(Base):
    __tablename__ = 'MercuryProtocol'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Quantum-(QAU)

class Table_Quantum(Base):
    __tablename__ = 'Quantum'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Neutron-(NTRN)

class Table_Neutron(Base):
    __tablename__ = 'Neutron'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Stealthcoin-(XST)

class Table_Stealthcoin(Base):
    __tablename__ = 'Stealthcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#LUXCoin-(LUX)

class Table_LUXCoin(Base):
    __tablename__ = 'LUXCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Publica-(PBL)

class Table_Publica(Base):
    __tablename__ = 'Publica'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#onG.social-(ONG)

class Table_onGsocial(Base):
    __tablename__ = 'onGsocial'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Gambit-(GAM)

class Table_Gambit(Base):
    __tablename__ = 'Gambit'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#bitUSD-(BITUSD)

class Table_bitUSD(Base):
    __tablename__ = 'bitUSD'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#ArtByte-(ABY)

class Table_ArtByte(Base):
    __tablename__ = 'ArtByte'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Verify-(CRED)

class Table_Verify(Base):
    __tablename__ = 'Verify'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#E-coin-(ECN)

class Table_Ecoin(Base):
    __tablename__ = 'Ecoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#CircuitsofValue-(COVAL)

class Table_CircuitsofValue(Base):
    __tablename__ = 'CircuitsofValue'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Polybius-(PLBT)

class Table_Polybius(Base):
    __tablename__ = 'Polybius'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Oxycoin-(OXY)

class Table_Oxycoin(Base):
    __tablename__ = 'Oxycoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#WavesCommunityToken-(WCT)

class Table_WavesCommunityToken(Base):
    __tablename__ = 'WavesCommunityToken'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Payfair-(PFR)

class Table_Payfair(Base):
    __tablename__ = 'Payfair'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#ATLANT-(ATL)

class Table_ATLANT(Base):
    __tablename__ = 'ATLANT'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Musicoin-(MUSIC)

class Table_Musicoin(Base):
    __tablename__ = 'Musicoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#GoByte-(GBX)

class Table_GoByte(Base):
    __tablename__ = 'GoByte'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Clams-(CLAM)

class Table_Clams(Base):
    __tablename__ = 'Clams'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#bitqy-(BQ)

class Table_bitqy(Base):
    __tablename__ = 'bitqy'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Soarcoin-(SOAR)

class Table_Soarcoin(Base):
    __tablename__ = 'Soarcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Energycoin-(ENRG)

class Table_Energycoin(Base):
    __tablename__ = 'Energycoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#FoldingCoin-(FLDC)

class Table_FoldingCoin(Base):
    __tablename__ = 'FoldingCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Mintcoin-(MINT)

class Table_Mintcoin(Base):
    __tablename__ = 'Mintcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#HEAT-(HEAT)

class Table_HEAT(Base):
    __tablename__ = 'HEAT'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#SwarmCity-(SWT)

class Table_SwarmCity(Base):
    __tablename__ = 'SwarmCity'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#GlobalCurrencyReserve-(GCR)

class Table_GlobalCurrencyReserve(Base):
    __tablename__ = 'GlobalCurrencyReserve'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Change-(CAG)

class Table_Change(Base):
    __tablename__ = 'Change'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BlockCAT-(CAT)

class Table_BlockCAT(Base):
    __tablename__ = 'BlockCAT'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Elixir-(ELIX)

class Table_Elixir(Base):
    __tablename__ = 'Elixir'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Obsidian-(ODN)

class Table_Obsidian(Base):
    __tablename__ = 'Obsidian'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#ColossusCoinXT-(COLX)

class Table_ColossusCoinXT(Base):
    __tablename__ = 'ColossusCoinXT'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#ICOS-(ICOS)

class Table_ICOS(Base):
    __tablename__ = 'ICOS'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Aeron-(ARN)

class Table_Aeron(Base):
    __tablename__ = 'Aeron'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#FedoraCoin-(TIPS)

class Table_FedoraCoin(Base):
    __tablename__ = 'FedoraCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BlackmoonCrypto-(BMC)

class Table_BlackmoonCrypto(Base):
    __tablename__ = 'BlackmoonCrypto'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#PoSWCoin-(POSW)

class Table_PoSWCoin(Base):
    __tablename__ = 'PoSWCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Linda-(LINDA)

class Table_Linda(Base):
    __tablename__ = 'Linda'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Incent-(INCNT)

class Table_Incent(Base):
    __tablename__ = 'Incent'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Playkey-(PKT)

class Table_Playkey(Base):
    __tablename__ = 'Playkey'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#OAX-(OAX)

class Table_OAX(Base):
    __tablename__ = 'OAX'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#KickCoin-(KICK)

class Table_KickCoin(Base):
    __tablename__ = 'KickCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#LEOcoin-(LEO)

class Table_LEOcoin(Base):
    __tablename__ = 'LEOcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Credo-(CREDO)

class Table_Credo(Base):
    __tablename__ = 'Credo'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#LoMoCoin-(LMC)

class Table_LoMoCoin(Base):
    __tablename__ = 'LoMoCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#ALQO-(ALQO)

class Table_ALQO(Base):
    __tablename__ = 'ALQO'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#TargetCoin-(TGT)

class Table_TargetCoin(Base):
    __tablename__ = 'TargetCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Pandacoin-(PND)

class Table_Pandacoin(Base):
    __tablename__ = 'Pandacoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Paragon-(PRG)

class Table_Paragon(Base):
    __tablename__ = 'Paragon'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Bitcrystals-(BCY)

class Table_Bitcrystals(Base):
    __tablename__ = 'Bitcrystals'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#LIFE-(LIFE)

class Table_LIFE(Base):
    __tablename__ = 'LIFE'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#ALIS-(ALIS)

class Table_ALIS(Base):
    __tablename__ = 'ALIS'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BLUE-(BLUE)

class Table_BLUE(Base):
    __tablename__ = 'BLUE'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#MyBitToken-(MYB)

class Table_MyBitToken(Base):
    __tablename__ = 'MyBitToken'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#SteemDollars-(SBD)

class Table_SteemDollars(Base):
    __tablename__ = 'SteemDollars'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Bismuth-(BIS)

class Table_Bismuth(Base):
    __tablename__ = 'Bismuth'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BlockMasonCreditProtocol-(BCPT)

class Table_BlockMasonCreditProtocol(Base):
    __tablename__ = 'BlockMasonCreditProtocol'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Patientory-(PTOY)

class Table_Patientory(Base):
    __tablename__ = 'Patientory'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#FlorinCoin-(FLO)

class Table_FlorinCoin(Base):
    __tablename__ = 'FlorinCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#OpenTradingNetwork-(OTN)

class Table_OpenTradingNetwork(Base):
    __tablename__ = 'OpenTradingNetwork'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Databits-(DTB)

class Table_Databits(Base):
    __tablename__ = 'Databits'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Hedge-(HDG)

class Table_Hedge(Base):
    __tablename__ = 'Hedge'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#InvestFeed-(IFT)

class Table_InvestFeed(Base):
    __tablename__ = 'InvestFeed'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Omni-(OMNI)

class Table_Omni(Base):
    __tablename__ = 'Omni'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#DecentBet-(DBET)

class Table_DecentBet(Base):
    __tablename__ = 'DecentBet'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Rialto-(XRL)

class Table_Rialto(Base):
    __tablename__ = 'Rialto'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#KiloCoin-(KLC)

class Table_KiloCoin(Base):
    __tablename__ = 'KiloCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#ATBCoin-(ATB)

class Table_ATBCoin(Base):
    __tablename__ = 'ATBCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BeanCash-(BITB)

class Table_BeanCash(Base):
    __tablename__ = 'BeanCash'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#AsiaCoin-(AC)

class Table_AsiaCoin(Base):
    __tablename__ = 'AsiaCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Stox-(STX)

class Table_Stox(Base):
    __tablename__ = 'Stox'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Radium-(RADS)

class Table_Radium(Base):
    __tablename__ = 'Radium'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Nexium-(NXC)

class Table_Nexium(Base):
    __tablename__ = 'Nexium'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#OKCash-(OK)

class Table_OKCash(Base):
    __tablename__ = 'OKCash'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Maecenas-(ART)

class Table_Maecenas(Base):
    __tablename__ = 'Maecenas'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#MonetaryUnit-(MUE)

class Table_MonetaryUnit(Base):
    __tablename__ = 'MonetaryUnit'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Peerplays-(PPY)

class Table_Peerplays(Base):
    __tablename__ = 'Peerplays'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Bounty0x-(BNTY)

class Table_Bounty0x(Base):
    __tablename__ = 'Bounty0x'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Myriad-(XMY)

class Table_Myriad(Base):
    __tablename__ = 'Myriad'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#NeosCoin-(NEOS)

class Table_NeosCoin(Base):
    __tablename__ = 'NeosCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Propy-(PRO)

class Table_Propy(Base):
    __tablename__ = 'Propy'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Divi-(DIVX)

class Table_Divi(Base):
    __tablename__ = 'Divi'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Numeraire-(NMR)

class Table_Numeraire(Base):
    __tablename__ = 'Numeraire'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#AirToken-(AIR)

class Table_AirToken(Base):
    __tablename__ = 'AirToken'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Rubycoin-(RBY)

class Table_Rubycoin(Base):
    __tablename__ = 'Rubycoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#ClearPoll-(POLL)

class Table_ClearPoll(Base):
    __tablename__ = 'ClearPoll'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Neumark-(NEU)

class Table_Neumark(Base):
    __tablename__ = 'Neumark'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Rivetz-(RVT)

class Table_Rivetz(Base):
    __tablename__ = 'Rivetz'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Golos-(GOLOS)

class Table_Golos(Base):
    __tablename__ = 'Golos'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#VeriCoin-(VRC)

class Table_VeriCoin(Base):
    __tablename__ = 'VeriCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Bodhi-(BOT)

class Table_Bodhi(Base):
    __tablename__ = 'Bodhi'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#SunContract-(SNC)

class Table_SunContract(Base):
    __tablename__ = 'SunContract'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#GridCoin-(GRC)

class Table_GridCoin(Base):
    __tablename__ = 'GridCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#OrmeusCoin-(ORME)

class Table_OrmeusCoin(Base):
    __tablename__ = 'OrmeusCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#MoedaLoyaltyPoints-(MDA)

class Table_MoedaLoyaltyPoints(Base):
    __tablename__ = 'MoedaLoyaltyPoints'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Xenon-(XNN)

class Table_Xenon(Base):
    __tablename__ = 'Xenon'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#EncrypGen-(DNA)

class Table_EncrypGen(Base):
    __tablename__ = 'EncrypGen'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Phore-(PHR)

class Table_Phore(Base):
    __tablename__ = 'Phore'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Dimecoin-(DIME)

class Table_Dimecoin(Base):
    __tablename__ = 'Dimecoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Blocktix-(TIX)

class Table_Blocktix(Base):
    __tablename__ = 'Blocktix'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#NuShares-(NSR)

class Table_NuShares(Base):
    __tablename__ = 'NuShares'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Snovio-(SNOV)

class Table_Snovio(Base):
    __tablename__ = 'Snovio'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#NewYorkCoin-(NYC)

class Table_NewYorkCoin(Base):
    __tablename__ = 'NewYorkCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#DeepOnion-(ONION)

class Table_DeepOnion(Base):
    __tablename__ = 'DeepOnion'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Expanse-(EXP)

class Table_Expanse(Base):
    __tablename__ = 'Expanse'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#ION-(ION)

class Table_ION(Base):
    __tablename__ = 'ION'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#FairCoin-(FAIR)

class Table_FairCoin(Base):
    __tablename__ = 'FairCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#NoLimitCoin-(NLC2)

class Table_NoLimitCoin(Base):
    __tablename__ = 'NoLimitCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Nimiq-(NET)

class Table_Nimiq(Base):
    __tablename__ = 'Nimiq'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BlackCoin-(BLK)

class Table_BlackCoin(Base):
    __tablename__ = 'BlackCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Worldcore-(WRC)

class Table_Worldcore(Base):
    __tablename__ = 'Worldcore'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#DubaiCoin-(DBIX)

class Table_DubaiCoin(Base):
    __tablename__ = 'DubaiCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Datum-(DAT)

class Table_Datum(Base):
    __tablename__ = 'Datum'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Mothership-(MSP)

class Table_Mothership(Base):
    __tablename__ = 'Mothership'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#SIBCoin-(SIB)

class Table_SIBCoin(Base):
    __tablename__ = 'SIBCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Dovu-(DOVU)

class Table_Dovu(Base):
    __tablename__ = 'Dovu'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#PotCoin-(POT)

class Table_PotCoin(Base):
    __tablename__ = 'PotCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Mercury-(MER)

class Table_Mercury(Base):
    __tablename__ = 'Mercury'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Elastic-(XEL)

class Table_Elastic(Base):
    __tablename__ = 'Elastic'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#adToken-(ADT)

class Table_adToken(Base):
    __tablename__ = 'adToken'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Crown-(CRW)

class Table_Crown(Base):
    __tablename__ = 'Crown'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#SafeExchangeCoin-(SAFEX)

class Table_SafeExchangeCoin(Base):
    __tablename__ = 'SafeExchangeCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#PascalCoin-(PASC)

class Table_PascalCoin(Base):
    __tablename__ = 'PascalCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Diamond-(DMD)

class Table_Diamond(Base):
    __tablename__ = 'Diamond'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Monetha-(MTH)

class Table_Monetha(Base):
    __tablename__ = 'Monetha'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#DomRaider-(DRT)

class Table_DomRaider(Base):
    __tablename__ = 'DomRaider'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Synereo-(AMP)

class Table_Synereo(Base):
    __tablename__ = 'Synereo'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#SolarCoin-(SLR)

class Table_SolarCoin(Base):
    __tablename__ = 'SolarCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Delphy-(DPY)

class Table_Delphy(Base):
    __tablename__ = 'Delphy'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#PepeCash-(PEPECASH)

class Table_PepeCash(Base):
    __tablename__ = 'PepeCash'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Paypex-(PAYX)

class Table_Paypex(Base):
    __tablename__ = 'Paypex'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Viberate-(VIB)

class Table_Viberate(Base):
    __tablename__ = 'Viberate'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#ECC-(ECC)

class Table_ECC(Base):
    __tablename__ = 'ECC'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Zeusshield-(ZSC)

class Table_Zeusshield(Base):
    __tablename__ = 'Zeusshield'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#bitCNY-(BITCNY)

class Table_bitCNY(Base):
    __tablename__ = 'bitCNY'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#YOYOW-(YOYOW)

class Table_YOYOW(Base):
    __tablename__ = 'YOYOW'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Humaniq-(HMQ)

class Table_Humaniq(Base):
    __tablename__ = 'Humaniq'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Everex-(EVX)

class Table_Everex(Base):
    __tablename__ = 'Everex'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Matchpool-(GUP)

class Table_Matchpool(Base):
    __tablename__ = 'Matchpool'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Mooncoin-(MOON)

class Table_Mooncoin(Base):
    __tablename__ = 'Mooncoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#SHIELD-(XSH)

class Table_SHIELD(Base):
    __tablename__ = 'SHIELD'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Grid+-(GRID)

class Table_Grid(Base):
    __tablename__ = 'Grid'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Agrello-(DLT)

class Table_Agrello(Base):
    __tablename__ = 'Agrello'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Voise-(VOISE)

class Table_Voise(Base):
    __tablename__ = 'Voise'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Spectrecoin-(XSPEC)

class Table_Spectrecoin(Base):
    __tablename__ = 'Spectrecoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Flash-(FLASH)

class Table_Flash(Base):
    __tablename__ = 'Flash'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#TaaS-(TAAS)

class Table_TaaS(Base):
    __tablename__ = 'TaaS'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#LAToken-(LA)

class Table_LAToken(Base):
    __tablename__ = 'LAToken'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Lykke-(LKK)

class Table_Lykke(Base):
    __tablename__ = 'Lykke'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#TokenCard-(TKN)

class Table_TokenCard(Base):
    __tablename__ = 'TokenCard'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Groestlcoin-(GRS)

class Table_Groestlcoin(Base):
    __tablename__ = 'Groestlcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Presearch-(PRS)

class Table_Presearch(Base):
    __tablename__ = 'Presearch'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#GenesisVision-(GVT)

class Table_GenesisVision(Base):
    __tablename__ = 'GenesisVision'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Pura-(PURA)

class Table_Pura(Base):
    __tablename__ = 'Pura'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Feathercoin-(FTC)

class Table_Feathercoin(Base):
    __tablename__ = 'Feathercoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#WhiteCoin-(XWC)

class Table_WhiteCoin(Base):
    __tablename__ = 'WhiteCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#DecisionToken-(HST)

class Table_DecisionToken(Base):
    __tablename__ = 'DecisionToken'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#COSS-(COSS)

class Table_COSS(Base):
    __tablename__ = 'COSS'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#iXledger-(IXT)

class Table_iXledger(Base):
    __tablename__ = 'iXledger'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Shift-(SHIFT)

class Table_Shift(Base):
    __tablename__ = 'Shift'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Jinn-(JINN)

class Table_Jinn(Base):
    __tablename__ = 'Jinn'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Lunyr-(LUN)

class Table_Lunyr(Base):
    __tablename__ = 'Lunyr'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Ink-(INK)

class Table_Ink(Base):
    __tablename__ = 'Ink'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Gifto-(GTO)

class Table_Gifto(Base):
    __tablename__ = 'Gifto'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#CoinDash-(CDT)

class Table_CoinDash(Base):
    __tablename__ = 'CoinDash'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#SaluS-(SLS)

class Table_SaluS(Base):
    __tablename__ = 'SaluS'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Aeon-(AEON)

class Table_Aeon(Base):
    __tablename__ = 'Aeon'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Namecoin-(NMC)

class Table_Namecoin(Base):
    __tablename__ = 'Namecoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#MinexCoin-(MNX)

class Table_MinexCoin(Base):
    __tablename__ = 'MinexCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Cofound.it-(CFI)

class Table_Cofoundit(Base):
    __tablename__ = 'Cofoundit'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#WeTrust-(TRST)

class Table_WeTrust(Base):
    __tablename__ = 'WeTrust'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#I/OCoin-(IOC)

class Table_IOCoin(Base):
    __tablename__ = 'IOCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#DECENT-(DCT)

class Table_DECENT(Base):
    __tablename__ = 'DECENT'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Lamden-(TAU)

class Table_Lamden(Base):
    __tablename__ = 'Lamden'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Hive-(HVN)

class Table_Hive(Base):
    __tablename__ = 'Hive'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#CloakCoin-(CLOAK)

class Table_CloakCoin(Base):
    __tablename__ = 'CloakCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Oyster-(PRL)

class Table_Oyster(Base):
    __tablename__ = 'Oyster'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Voxels-(VOX)

class Table_Voxels(Base):
    __tablename__ = 'Voxels'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Asch-(XAS)

class Table_Asch(Base):
    __tablename__ = 'Asch'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Bread-(BRD)

class Table_Bread(Base):
    __tablename__ = 'Bread'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Ambrosus-(AMB)

class Table_Ambrosus(Base):
    __tablename__ = 'Ambrosus'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Rise-(RISE)

class Table_Rise(Base):
    __tablename__ = 'Rise'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Tierion-(TNT)

class Table_Tierion(Base):
    __tablename__ = 'Tierion'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Metal-(MTL)

class Table_Metal(Base):
    __tablename__ = 'Metal'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#FirstBlood-(1ST)

class Table_FirstBlood(Base):
    __tablename__ = 'FirstBlood'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#UTRUST-(UTK)

class Table_UTRUST(Base):
    __tablename__ = 'UTRUST'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#district0x-(DNT)

class Table_district0x(Base):
    __tablename__ = 'district0x'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#AgorasTokens-(AGRS)

class Table_AgorasTokens(Base):
    __tablename__ = 'AgorasTokens'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Melon-(MLN)

class Table_Melon(Base):
    __tablename__ = 'Melon'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#HempCoin-(THC)

# class Table_HempCoin(Base):
#     __tablename__ = 'HempCoin'
#     date = Column('date', DATE,primary_key=True)
#     open = Column('open', FLOAT)
#     high = Column('high', FLOAT)
#     low = Column('low', FLOAT)
#     close = Column('close', FLOAT)
#     volume = Column('volume', FLOAT)

#Eidoo-(EDO)

class Table_Eidoo(Base):
    __tablename__ = 'Eidoo'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Nuls-(NULS)

class Table_Nuls(Base):
    __tablename__ = 'Nuls'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Etherparty-(FUEL)

class Table_Etherparty(Base):
    __tablename__ = 'Etherparty'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#IoTChain-(ITC)

class Table_IoTChain(Base):
    __tablename__ = 'IoTChain'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Wings-(WINGS)

class Table_Wings(Base):
    __tablename__ = 'Wings'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#MobileGo-(MGO)

class Table_MobileGo(Base):
    __tablename__ = 'MobileGo'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Burst-(BURST)

class Table_Burst(Base):
    __tablename__ = 'Burst'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Cindicator-(CND)

class Table_Cindicator(Base):
    __tablename__ = 'Cindicator'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#MetaverseETP-(ETP)

class Table_MetaverseETP(Base):
    __tablename__ = 'MetaverseETP'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#UnikoinGold-(UKG)

class Table_UnikoinGold(Base):
    __tablename__ = 'UnikoinGold'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Decentraland-(MANA)

class Table_Decentraland(Base):
    __tablename__ = 'Decentraland'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Wagerr-(WGR)

class Table_Wagerr(Base):
    __tablename__ = 'Wagerr'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#WaBi-(WABI)

class Table_WaBi(Base):
    __tablename__ = 'WaBi'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Modum-(MOD)

class Table_Modum(Base):
    __tablename__ = 'Modum'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#ZenCash-(ZEN)

class Table_ZenCash(Base):
    __tablename__ = 'ZenCash'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#NAGA-(NGC)

class Table_NAGA(Base):
    __tablename__ = 'NAGA'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#AdEx-(ADX)

class Table_AdEx(Base):
    __tablename__ = 'AdEx'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Triggers-(TRIG)

class Table_Triggers(Base):
    __tablename__ = 'Triggers'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#CyberMiles-(CMT)

class Table_CyberMiles(Base):
    __tablename__ = 'CyberMiles'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#ATMChain-(ATM)

class Table_ATMChain(Base):
    __tablename__ = 'ATMChain'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Centra-(CTR)

class Table_Centra(Base):
    __tablename__ = 'Centra'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Viacoin-(VIA)

class Table_Viacoin(Base):
    __tablename__ = 'Viacoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#LBRYCredits-(LBC)

class Table_LBRYCredits(Base):
    __tablename__ = 'LBRYCredits'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#StreamrDATAcoin-(DATA)

class Table_StreamrDATAcoin(Base):
    __tablename__ = 'StreamrDATAcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#SuperNET-(UNITY)

class Table_SuperNET(Base):
    __tablename__ = 'SuperNET'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Counterparty-(XCP)

class Table_Counterparty(Base):
    __tablename__ = 'Counterparty'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#SONM-(SNM)

class Table_SONM(Base):
    __tablename__ = 'SONM'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Einsteinium-(EMC2)

class Table_Einsteinium(Base):
    __tablename__ = 'Einsteinium'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#DynamicTradingRights-(DTR)

class Table_DynamicTradingRights(Base):
    __tablename__ = 'DynamicTradingRights'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#SpankChain-(SPANK)

class Table_SpankChain(Base):
    __tablename__ = 'SpankChain'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#RipioCreditNetwork-(RCN)

class Table_RipioCreditNetwork(Base):
    __tablename__ = 'RipioCreditNetwork'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#XTRABYTES-(XBY)

class Table_XTRABYTES(Base):
    __tablename__ = 'XTRABYTES'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Achain-(ACT)

class Table_Achain(Base):
    __tablename__ = 'Achain'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#TimeNewBank-(TNB)

class Table_TimeNewBank(Base):
    __tablename__ = 'TimeNewBank'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#AirSwap-(AST)

class Table_AirSwap(Base):
    __tablename__ = 'AirSwap'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#DeepBrainChain-(DBC)

class Table_DeepBrainChain(Base):
    __tablename__ = 'DeepBrainChain'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#SimpleToken-(OST)

class Table_SimpleToken(Base):
    __tablename__ = 'SimpleToken'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Gulden-(NLG)

class Table_Gulden(Base):
    __tablename__ = 'Gulden'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#VIBE-(VIBE)

class Table_VIBE(Base):
    __tablename__ = 'VIBE'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Peercoin-(PPC)

class Table_Peercoin(Base):
    __tablename__ = 'Peercoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#QuantumResistantLedger-(QRL)

class Table_QuantumResistantLedger(Base):
    __tablename__ = 'QuantumResistantLedger'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BitBay-(BAY)

class Table_BitBay(Base):
    __tablename__ = 'BitBay'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#SingularDTV-(SNGLS)

class Table_SingularDTV(Base):
    __tablename__ = 'SingularDTV'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#ETHLend-(LEND)

class Table_ETHLend(Base):
    __tablename__ = 'ETHLend'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Aragon-(ANT)

class Table_Aragon(Base):
    __tablename__ = 'Aragon'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Ubiq-(UBQ)

class Table_Ubiq(Base):
    __tablename__ = 'Ubiq'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#AppCoins-(APPC)

class Table_AppCoins(Base):
    __tablename__ = 'AppCoins'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#SIRINLABSToken-(SRN)

class Table_SIRINLABSToken(Base):
    __tablename__ = 'SIRINLABSToken'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#RedPulse-(RPX)

class Table_RedPulse(Base):
    __tablename__ = 'RedPulse'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#EnjinCoin-(ENJ)

class Table_EnjinCoin(Base):
    __tablename__ = 'EnjinCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Edgeless-(EDG)

class Table_Edgeless(Base):
    __tablename__ = 'Edgeless'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Monaco-(MCO)

class Table_Monaco(Base):
    __tablename__ = 'Monaco'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BridgeCoin-(BCO)

class Table_BridgeCoin(Base):
    __tablename__ = 'BridgeCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Vertcoin-(VTC)

class Table_Vertcoin(Base):
    __tablename__ = 'Vertcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Revain-(R)

class Table_Revain(Base):
    __tablename__ = 'Revain'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Blocknet-(BLOCK)

class Table_Blocknet(Base):
    __tablename__ = 'Blocknet'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#iExecRLC-(RLC)

class Table_iExecRLC(Base):
    __tablename__ = 'iExecRLC'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Po.et-(POE)

class Table_Poet(Base):
    __tablename__ = 'Poet'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#DEW-(DEW)

class Table_DEW(Base):
    __tablename__ = 'DEW'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Storm-(STORM)

class Table_Storm(Base):
    __tablename__ = 'Storm'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#PayPie-(PPP)

class Table_PayPie(Base):
    __tablename__ = 'PayPie'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Storj-(STORJ)

class Table_Storj(Base):
    __tablename__ = 'Storj'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#SantimentNetworkToken-(SAN)

class Table_SantimentNetworkToken(Base):
    __tablename__ = 'SantimentNetworkToken'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#NAVCoin-(NAV)

class Table_NAVCoin(Base):
    __tablename__ = 'NAVCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Pillar-(PLR)

class Table_Pillar(Base):
    __tablename__ = 'Pillar'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Quantstamp-(QSP)

class Table_Quantstamp(Base):
    __tablename__ = 'Quantstamp'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Cobinhood-(COB)

class Table_Cobinhood(Base):
    __tablename__ = 'Cobinhood'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BLOCKv-(VEE)

class Table_BLOCKv(Base):
    __tablename__ = 'BLOCKv'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Skycoin-(SKY)

class Table_Skycoin(Base):
    __tablename__ = 'Skycoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#PACcoin-(PAC)

class Table_PACcoin(Base):
    __tablename__ = 'PACcoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#RaidenNetworkToken-(RDN)

class Table_RaidenNetworkToken(Base):
    __tablename__ = 'RaidenNetworkToken'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Cryptonex-(CNX)

class Table_Cryptonex(Base):
    __tablename__ = 'Cryptonex'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BitcoinDark-(BTCD)

class Table_BitcoinDark(Base):
    __tablename__ = 'BitcoinDark'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Bitcore-(BTX)

class Table_Bitcore(Base):
    __tablename__ = 'Bitcore'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#ChainLink-(LINK)

class Table_ChainLink(Base):
    __tablename__ = 'ChainLink'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Neblio-(NEBL)

class Table_Neblio(Base):
    __tablename__ = 'Neblio'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#XPlay-(XPA)

class Table_XPlay(Base):
    __tablename__ = 'XPlay'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Emercoin-(EMC)

class Table_Emercoin(Base):
    __tablename__ = 'Emercoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Civic-(CVC)

class Table_Civic(Base):
    __tablename__ = 'Civic'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Gnosis-(GNO)

class Table_Gnosis(Base):
    __tablename__ = 'Gnosis'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#DigitalNote-(XDN)

class Table_DigitalNote(Base):
    __tablename__ = 'DigitalNote'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Iconomi-(ICN)

class Table_Iconomi(Base):
    __tablename__ = 'Iconomi'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Nebulas-(NAS)

class Table_Nebulas(Base):
    __tablename__ = 'Nebulas'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#aelf-(ELF)

class Table_aelf(Base):
    __tablename__ = 'aelf'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#ZCoin-(XZC)

class Table_ZCoin(Base):
    __tablename__ = 'ZCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Bancor-(BNT)

class Table_Bancor(Base):
    __tablename__ = 'Bancor'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#TenX-(PAY)

class Table_TenX(Base):
    __tablename__ = 'TenX'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#DigixDAO-(DGD)

class Table_DigixDAO(Base):
    __tablename__ = 'DigixDAO'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Particl-(PART)

class Table_Particl(Base):
    __tablename__ = 'Particl'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Enigma-(ENG)

class Table_Enigma(Base):
    __tablename__ = 'Enigma'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#RequestNetwork-(REQ)

class Table_RequestNetwork(Base):
    __tablename__ = 'RequestNetwork'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#MediBloc-(MED)

class Table_MediBloc(Base):
    __tablename__ = 'MediBloc'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Nexus-(NXS)

class Table_Nexus(Base):
    __tablename__ = 'Nexus'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#GameCredits-(GAME)

class Table_GameCredits(Base):
    __tablename__ = 'GameCredits'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Kin-(KIN)

class Table_Kin(Base):
    __tablename__ = 'Kin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Nxt-(NXT)

class Table_Nxt(Base):
    __tablename__ = 'Nxt'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#GXShares-(GXS)

class Table_GXShares(Base):
    __tablename__ = 'GXShares'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#PowerLedger-(POWR)

class Table_PowerLedger(Base):
    __tablename__ = 'PowerLedger'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Substratum-(SUB)

class Table_Substratum(Base):
    __tablename__ = 'Substratum'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Syscoin-(SYS)

class Table_Syscoin(Base):
    __tablename__ = 'Syscoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Aeternity-(AE)

class Table_Aeternity(Base):
    __tablename__ = 'Aeternity'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Dent-(DENT)

class Table_Dent(Base):
    __tablename__ = 'Dent'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#MaidSafeCoin-(MAID)

class Table_MaidSafeCoin(Base):
    __tablename__ = 'MaidSafeCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#ExperiencePoints-(XP)

class Table_ExperiencePoints(Base):
    __tablename__ = 'ExperiencePoints'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#RChain-(RHOC)

class Table_RChain(Base):
    __tablename__ = 'RChain'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Ethos-(ETHOS)

class Table_Ethos(Base):
    __tablename__ = 'Ethos'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#MonaCoin-(MONA)

class Table_MonaCoin(Base):
    __tablename__ = 'MonaCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#FunFair-(FUN)

class Table_FunFair(Base):
    __tablename__ = 'FunFair'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Bytom-(BTM)

class Table_Bytom(Base):
    __tablename__ = 'Bytom'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#ReddCoin-(RDD)

class Table_ReddCoin(Base):
    __tablename__ = 'ReddCoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#ByteballBytes-(GBYTE)

class Table_ByteballBytes(Base):
    __tablename__ = 'ByteballBytes'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Aion-(AION)

class Table_Aion(Base):
    __tablename__ = 'Aion'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#KyberNetwork-(KNC)

class Table_KyberNetwork(Base):
    __tablename__ = 'KyberNetwork'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#ZClassic-(ZCL)

class Table_ZClassic(Base):
    __tablename__ = 'ZClassic'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Factom-(FCT)

class Table_Factom(Base):
    __tablename__ = 'Factom'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Walton-(WTC)

class Table_Walton(Base):
    __tablename__ = 'Walton'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#PIVX-(PIVX)

class Table_PIVX(Base):
    __tablename__ = 'PIVX'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#SmartCash-(SMART)

class Table_SmartCash(Base):
    __tablename__ = 'SmartCash'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BasicAttentionToken-(BAT)

class Table_BasicAttentionToken(Base):
    __tablename__ = 'BasicAttentionToken'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Loopring-(LRC)

class Table_Loopring(Base):
    __tablename__ = 'Loopring'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Dentacoin-(DCN)

class Table_Dentacoin(Base):
    __tablename__ = 'Dentacoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Hshare-(HSR)

class Table_Hshare(Base):
    __tablename__ = 'Hshare'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#SALT-(SALT)

class Table_SALT(Base):
    __tablename__ = 'SALT'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Decred-(DCR)

class Table_Decred(Base):
    __tablename__ = 'Decred'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Ark-(ARK)

class Table_Ark(Base):
    __tablename__ = 'Ark'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Electroneum-(ETN)

class Table_Electroneum(Base):
    __tablename__ = 'Electroneum'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#QASH-(QASH)

class Table_QASH(Base):
    __tablename__ = 'QASH'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Gas-(GAS)

class Table_Gas(Base):
    __tablename__ = 'Gas'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Dragonchain-(DRGN)

class Table_Dragonchain(Base):
    __tablename__ = 'Dragonchain'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Golem-(GNT)

class Table_Golem(Base):
    __tablename__ = 'Golem'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#WAX-(WAX)

class Table_WAX(Base):
    __tablename__ = 'WAX'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Veritaseum-(VERI)

class Table_Veritaseum(Base):
    __tablename__ = 'Veritaseum'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Komodo-(KMD)

class Table_Komodo(Base):
    __tablename__ = 'Komodo'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#0x-(ZRX)

class Table_0x(Base):
    __tablename__ = '0x'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Zcash-(ZEC)

class Table_Zcash(Base):
    __tablename__ = 'Zcash'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#OmiseGO-(OMG)

class Table_OmiseGO(Base):
    __tablename__ = 'OmiseGO'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#DigiByte-(DGB)

class Table_DigiByte(Base):
    __tablename__ = 'DigiByte'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#RaiBlocks-(XRB)

class Table_RaiBlocks(Base):
    __tablename__ = 'RaiBlocks'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Augur-(REP)

class Table_Augur(Base):
    __tablename__ = 'Augur'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Lisk-(LSK)

class Table_Lisk(Base):
    __tablename__ = 'Lisk'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Qtum-(QTUM)

class Table_Qtum(Base):
    __tablename__ = 'Qtum'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#ICON-(ICX)

class Table_ICON(Base):
    __tablename__ = 'ICON'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#EthereumClassic-(ETC)

class Table_EthereumClassic(Base):
    __tablename__ = 'EthereumClassic'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BitcoinGold-(BTG)

class Table_BitcoinGold(Base):
    __tablename__ = 'BitcoinGold'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#TRON-(TRX)

class Table_TRON(Base):
    __tablename__ = 'TRON'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Monero-(XMR)

class Table_Monero(Base):
    __tablename__ = 'Monero'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Stellar-(XLM)

class Table_Stellar(Base):
    __tablename__ = 'Stellar'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Cardano-(ADA)

class Table_Cardano(Base):
    __tablename__ = 'Cardano'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Dash-(DASH)

class Table_Dash(Base):
    __tablename__ = 'Dash'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Litecoin-(LTC)

class Table_Litecoin(Base):
    __tablename__ = 'Litecoin'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#IOTA-(MIOTA)

class Table_IOTA(Base):
    __tablename__ = 'IOTA'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#BitcoinCash-(BCH)

class Table_BitcoinCash(Base):
    __tablename__ = 'BitcoinCash'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#NEM-(XEM)

class Table_NEM(Base):
    __tablename__ = 'NEM'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Ripple-(XRP)

class Table_Ripple(Base):
    __tablename__ = 'Ripple'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

#Ethereum-(ETH)

class Table_Ethereum(Base):
    __tablename__ = 'Ethereum'
    date = Column('date', DATE,primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

class Table_LightChain(Base):
    __tablename__ = 'LightChain'
    date = Column('date', DATE, primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

class Table_Zilliqa(Base):
    __tablename__ = 'Zilliqa'
    date = Column('date', DATE, primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)

class Table_SingularityNET(Base):
    __tablename__ = 'SingularityNET'
    date = Column('date', DATE, primary_key=True)
    open = Column('open', FLOAT)
    high = Column('high', FLOAT)
    low = Column('low', FLOAT)
    close = Column('close', FLOAT)
    volume = Column('volume', FLOAT)
'''