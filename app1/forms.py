from django import forms

from .models import RequirementsInfometion

### 検索条件フォーム ###
### 現在index.htmlに直で記載している為、使用する場合、変更する必要あり
class RequirementsInfometionForm(forms.ModelForm):

    class Meta:
        model = RequirementsInfometion
        fields = (
                  "registrationFormRadioButton", 
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
                  "firstCityHotelTariffCode1",
                  "firstCityHotelTariffCode2",
                  "firstCityLopCompanyCode",
                  "firstCityPlanId",
                  "secondtCity",
                  "secondtCityDepartureDate",
                  "secondtCityHotelTariffCode1",
                  "secondtCityHotelTariffCode2",
                  "thirdCity",
                  "thirdCityDepartureDate",
                  "thirdCityHotelTariffCode1",
                  "thirdCityHotelTariffCode2",
                  "airlinesSelectTxt",
                  "useDirectFlightChackBox",
                  "cabinClassOutboundTripRadioButton",
                  "cabinClassRoundTripRadioButton",
                  "flightNumberOutboundTripTxt",
                  "flightNumberRoundTripTxt",
                  )

#アップロード用フォーム
class CSVUploadForm(forms.Form):
    file = forms.FileField(label='CSVファイル', help_text='※拡張子csvのファイルをアップロードしてください。')