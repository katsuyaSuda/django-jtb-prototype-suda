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
                  "relativeSettings2EndDayTxt"
                  )


    # ##出発日設定時間_ラジオボタン
    # departureDateSettingRadioChoice = [('0', '絶対設定'), ('1', '相対設定1'), ('2', '相対設定2')]
    # departureDateSettingRadio = forms.fields.ChoiceField(
    #     label='出発日設定時間_ラジオボタン',
    #     required=False,
    #     disabled=False,
    #     choices= departureDateSettingRadioChoice,
    #     widget=forms.RadioSelect(attrs={
    #            'id': ' ','class': 'form-check-input'})
    # )