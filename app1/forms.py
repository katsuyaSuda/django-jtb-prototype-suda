from django import forms

from .models import RequirementsInfometion

### 検索条件フォーム ###
### 現在index.htmlに直で記載している為、使用する場合、変更する必要あり
class RequirementsInfometionForm(forms.ModelForm):

    class Meta:
        model = RequirementsInfometion
        fields = ("registrationFormRadioButton", 
                  "outputDestinationJtbChackBox", 
                  "outputDestinationTravelChackBox",
                  "outputDestinationPamphletChackBox",
                  "departurePoint",
                  "adultNum",
                  "departureDateSettingRadio",
                  "absoluteSettingStartDate",
                  "absoluteSettingEndDate",
                  "relativeSettings1StartList",
                  "relativeSettings1EndList",
                  "relativeSettings2StartDayTxt",
                  "relativeSettings2EndDayTxt",
                  "rootPackageId",
                  "firstCity",
                  "firstCityDepartureDate",
                  "firstCityHotelTariffCode",
                  "firstCityLopCompanyCode",
                  "firstCityPlanId",
                  "secondtCity",
                  "secondtCityDepartureDate",
                  "secondtCityHotelTariffCode",
                  "thirdCity",
                  "thirdCityDepartureDate",
                  "thirdCityHotelTariffCode",
                  "airlinesSelectTxt",
                  "cabinClassOutboundTripRadioButton",
                  "cabinClassRoundTripRadioButton",
                  "flightNumberOutboundTripTxt",
                  "flightNumberRoundTripTxt",
                  )

#アップロード用フォーム
class CSVUploadForm(forms.Form):
    file = forms.FileField(label='CSVファイル', help_text='※拡張子csvのファイルをアップロードしてください。')