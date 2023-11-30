from django.db import models

#### 各条件設定 ####
class ContentId(models.Model):
    contentId = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        unique=True)
    
    def __str__(self):
        return self.contentId

#Create your models here.
#### 条件情報 ####
class RequirementsInfometion(models.Model):
    #### 登録形態 ####
    registrationFormRadioButton = models.CharField(
        max_length=255,
        blank=False,
        null=False)
    
    #### 出力先 ####
    #JTB
    outputDestinationJtbChackBox = models.CharField(
        max_length=255,
        blank=False,
        null=False)
    #トラベルコ
    outputDestinationTravelChackBox = models.CharField(
        max_length=255,
        blank=False,
        null=False)
    #パンフレット
    outputDestinationPamphletChackBox = models.CharField(
        max_length=255,
        blank=False,
        null=False)

    #### 出発地 ####
    departurePoint = models.CharField(
        max_length=255,
        blank=False,
        null=False)
    # 大人人数
    adultNum = models.CharField(
        max_length=255,
        blank=False,
        null=False)

    #### 出発美設定時間 ####
    #絶対設定
    departureDateSettingRadio = models.CharField(
        max_length=255,
        blank=False,
        null=False)     
    #絶対設定_開始日付
    absoluteSettingStartDate = models.CharField(
        max_length=255,
        blank=False,
        null=False) 
    #絶対設定_終了日付
    absoluteSettingEndDate = models.CharField(
        max_length=255,
        blank=False,
        null=False) 
    
    #絶対設定_開始リスト
    relativeSettings1StartList = models.CharField(
        max_length=255,
        blank=False,
        null=False) 
    #絶対設定_終了リスト
    relativeSettings1EndList = models.CharField(
        max_length=255,
        blank=False,
        null=False) 
    
    #絶対設定_開始日エリア
    relativeSettings2StartDayTxt = models.CharField(
        max_length=255,
        blank=False,
        null=False) 
    #絶対設定_終了日エリア
    relativeSettings2EndDayTxt = models.CharField(
        max_length=255,
        blank=False,
        null=False) 
    
    contentId = models.ForeignKey(
        ContentId,
        on_delete=models.CASCADE)
    
    def __str__(self):
        return self.contentId
