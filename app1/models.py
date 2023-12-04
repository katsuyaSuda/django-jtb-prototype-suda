from django.db import models
import uuid
# from django.urls import reverse_lazy

#region 条件情報
#### 各条件設定 ####
# class ContentId(models.Model):
#     # contentId = models.UUIDField(
#     #     primary_key=True, 
#     #     default=uuid.uuid4, 
#     #     editable=False)

#     contentId = models.AutoField(
#         primary_key=True,
#         blank=True,
#         null=False,
#         unique=True)

#     def __str__(self):
#         return self.contentId

class RequirementsInfometion(models.Model):

    #### 登録形態 ####
    registrationFormRadioButton = models.CharField(
        verbose_name='登録形態',
        max_length=255,
        blank=False,
        null=False)

    #### 出力先 ####
    #JTB
    outputDestinationJtbChackBox = models.BooleanField(
        verbose_name='出力先_JTB',
        max_length=255,
        blank=False,
        null=False)
    #トラベルコ
    outputDestinationTravelChackBox = models.BooleanField(
        verbose_name='出力先_トラベルコ',
        max_length=255,
        blank=False,
        null=False)
    #パンフレット
    outputDestinationPamphletChackBox = models.BooleanField(
        verbose_name='出力先_パンフレット',
        max_length=255,
        blank=False,
        null=False)

    #### 出発地 ####
    departurePoint = models.CharField(
        verbose_name='出発地',
        max_length=255,
        blank=False,
        null=False)
    # 大人人数
    adultNum = models.IntegerField(
        verbose_name='大人人数',
        blank=True,
        null=True,
        default=0)

    #### 出発日設定時間 ####
    #出発日設定時間_ラジオボタン
    departureDateSettingRadio = models.CharField(
        verbose_name='',
        max_length=255,
        blank=False,
        null=False)

    #絶対設定_開始日付
    absoluteSettingStartDate = models.DateTimeField(
        verbose_name='',
        blank=True,
        null=True) 
    #絶対設定_終了日付
    absoluteSettingEndDate = models.DateTimeField(
        verbose_name='',
        blank=True,
        null=True) 
    
    #相対設定1_開始リスト
    relativeSettings1StartList = models.CharField(
        verbose_name='',
        max_length=255,
        blank=True,
        null=True) 
    #相対設定1_終了リスト
    relativeSettings1EndList = models.CharField(
        verbose_name='',
        max_length=255,
        blank=True,
        null=True) 
    
    #相対設定2_開始日エリア
    relativeSettings2StartDayTxt = models.CharField(
        verbose_name='',
        max_length=255,
        blank=True,
        null=True) 
    #相対設定2_終了日エリア
    relativeSettings2EndDayTxt = models.CharField(
        verbose_name='',
        max_length=255,
        blank=True,
        null=True) 
    
    # def get_absolute_url(self):
    #     # /detail/id番号/
    #     return reverse_lazy("detail", args=[self.id])
    
    # def __str__(self):
    #     return self.id
#endregion 条件情報
