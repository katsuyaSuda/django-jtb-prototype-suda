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
    registrationFormRadioButton = models.TextField(
        verbose_name='登録形態',
        choices=[('1', 'エスコート'), 
                 ('2', 'MySTYLE(UAH含む)'), 
                 ('3', '航空券 '), 
                 ('4', 'ホテル')
                 ],
        blank=False,
        null=False
        )

    #### 出力先 ####
    #JTB
    outputDestinationJtbChackBox = models.BooleanField(
        verbose_name='出力先_JTB',
    )
    #トラベルコ
    outputDestinationTravelChackBox = models.BooleanField(
        verbose_name='出力先_トラベルコ',
    )
    #パンフレット
    outputDestinationPamphletChackBox = models.BooleanField(
        verbose_name='出力先_パンフレット',
    )
    
    #### 出発地 ####
    departurePoint = models.CharField(
        verbose_name='出発地',
        choices=[('HND', '東京(羽田)'), 
                 ('NRT', '東京(成田)'), 
                 ('ITM', '大阪(伊丹)'),
                 ('CTS', '札幌(新千歳)'),
                 ('NGO', '名古屋(中部)'),
                 ('FUK', '福岡'),
                 ],
        max_length=255,
        blank=False,
        null=False)
    
    # #### 出発地 ####
    # departurePointChk = models.TextField(
    #     verbose_name='出発地',
    #     choices=[('HND', '東京(羽田)'), 
    #              ('NRT', '東京(成田)'), 
    #              ('ITM', '大阪(伊丹)'),
    #              ('CTS', '札幌(新千歳)'),
    #              ('NGO', '名古屋(中部)'),
    #              ('FUK', '福岡'),
    #              ],
    #     max_length=255,
    #     blank=False,
    #     null=False)
    
    # 大人人数
    adultNum = models.IntegerField(
        verbose_name='大人人数',
        blank=True,
        null=True,
        default=0)

    #### 出発日設定時間 ####
    #出発日設定時間_ラジオボタン
    departureDateSettingRadio = models.TextField(
        verbose_name='出発日設定時間',
        choices=[('1', '絶対設定'), 
                 ('2', '相対設定1'), 
                 ('3', '相対設定2'),
                 ],
        blank=False,
        null=False)

    #絶対設定_開始日付
    absoluteSettingStartDate = models.DateTimeField(
        verbose_name='絶対設定_開始日付',
        blank=True,
        null=True) 
    #絶対設定_終了日付
    absoluteSettingEndDate = models.DateTimeField(
        verbose_name='絶対設定_終了日付',
        blank=True,
        null=True) 
    
    #相対設定1_開始リスト
    relativeSettings1StartList = models.CharField(
        verbose_name='相対設定1_開始リスト',
        max_length=255,
        blank=True,
        null=True) 
    #相対設定1_終了リスト
    relativeSettings1EndList = models.CharField(
        verbose_name='相対設定1_終了リスト',
        max_length=255,
        blank=True,
        null=True) 
    
    #相対設定2_開始日
    relativeSettings2StartDayTxt = models.CharField(
        verbose_name='相対設定2_開始日',
        max_length=255,
        blank=True,
        null=True) 
    #相対設定2_終了日
    relativeSettings2EndDayTxt = models.CharField(
        verbose_name='相対設定2_終了日',
        max_length=255,
        blank=True,
        null=True) 

    #### ルートパッケージID ####    
    rootPackageId = models.CharField(
        verbose_name='ルートパッケージID',
        max_length=255,
        blank=True,
        null=True) 
    
    #### サービスパッケージID #### 
    #1都市目
    firstCity = models.CharField(
        verbose_name='1都市目',
        max_length=255,
        blank=False,
        null=False)
    
    #1都市目_現地出発日
    firstCityDepartureDate = models.CharField(
        verbose_name='1都市目_現地出発日',
        max_length=255,
        blank=True,
        null=True)
    
    #1都市目_ホテルタリフコード1
    firstCityHotelTariffCode1 = models.CharField(
        verbose_name='1都市目_ホテルタリフコード1',
        max_length=255,
        blank=True,
        null=True)
    
    #1都市目_ホテルタリフコード2
    firstCityHotelTariffCode2 = models.CharField(
        verbose_name='1都市目_ホテルタリフコード2',
        max_length=255,
        blank=True,
        null=True)
    
    #1都市目_LOP会社コード
    firstCityLopCompanyCode = models.CharField(
        verbose_name='1都市目_LOP会社コード',
        max_length=255,
        blank=True,
        null=True)
    
    #1都市目_プランID
    firstCityPlanId = models.CharField(
        verbose_name='1都市目_プランID',
        max_length=255,
        blank=True,
        null=True)

    #2都市目
    secondtCity = models.CharField(
        verbose_name='2都市目',
        max_length=255,
        blank=True,
        null=True)
    
    #2都市目_現地出発日
    secondtCityDepartureDate = models.CharField(
        verbose_name='2都市目_現地出発日',
        max_length=255,
        blank=True,
        null=True)
    
    #2都市目_ホテルタリフコード1
    secondtCityHotelTariffCode1 = models.CharField(
        verbose_name='2都市目_ホテルタリフコード1',
        max_length=255,
        blank=True,
        null=True)
    
    #2都市目_ホテルタリフコード2
    secondtCityHotelTariffCode2 = models.CharField(
        verbose_name='2都市目_ホテルタリフコード2',
        max_length=255,
        blank=True,
        null=True)
    
    #3都市目
    thirdCity = models.CharField(
        verbose_name='3都市目',
        max_length=255,
        blank=True,
        null=True)
    
    #3都市目_現地出発日
    thirdCityDepartureDate = models.CharField(
        verbose_name='3都市目_現地出発日',
        max_length=255,
        blank=True,
        null=True)
    
    #3都市目_ホテルタリフコード1
    thirdCityHotelTariffCode1 = models.CharField(
        verbose_name='3都市目_ホテルタリフコード1',
        max_length=255,
        blank=True,
        null=True)
    
    #3都市目_ホテルタリフコード2
    thirdCityHotelTariffCode2 = models.CharField(
        verbose_name='3都市目_ホテルタリフコード2',
        max_length=255,
        blank=True,
        null=True)
    
    #### 航空会社 ####
    #航空会社
    airlinesSelectTxt = models.CharField(
        verbose_name='航空会社',
        max_length=255,
        blank=True,
        null=True) 

    #直行便指定
    useDirectFlightChackBox = models.BooleanField(
        verbose_name='直行便指定',
        # choices=[(False, '直行便利用なし'), 
        #          (True, '直行便利用')
        #     ],
    )

    #### キャビンクラス（往路） ####
    #キャビンクラス（往路）
    cabinClassOutboundTripRadioButton = models.TextField(
        verbose_name='キャビンクラス（往路）',
        choices=[('1', 'エコノミー'), 
                 ('2', 'プレミアムエコノミー'), 
                 ('3', 'ビジネス '), 
                 ('4', 'ファースト')
                 ],
        blank=True,
        null=True) 
    
    #キャビンクラス（複路）
    cabinClassRoundTripRadioButton = models.TextField(
        verbose_name='キャビンクラス（複路）',
        choices=[('1', 'エコノミー'), 
                 ('2', 'プレミアムエコノミー'), 
                 ('3', 'ビジネス '), 
                 ('4', 'ファースト')
                 ],
        blank=True,
        null=True) 

    #便名（往路）
    flightNumberOutboundTripTxt = models.CharField(
        verbose_name='便名（往路）',
        max_length=255,
        blank=True,
        null=True) 
    
    #便名（複路）
    flightNumberRoundTripTxt = models.CharField(
        verbose_name='便名（複路）',
        max_length=255,
        blank=True,
        null=True) 
    
    #作成日時
    created_at = models.DateTimeField(
        verbose_name='作成日時',
        auto_now_add=True)
    
    #更新日時
    updated_at = models.DateTimeField(
        verbose_name='更新日時',
        auto_now=True)

    # def get_absolute_url(self):
    #     # /detail/id番号/
    #     return reverse_lazy("detail", args=[self.id])
    
    # def __str__(self):
    #     return self.id
#endregion 条件情報
