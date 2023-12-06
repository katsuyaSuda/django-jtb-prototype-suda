from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, ListView

from .models import RequirementsInfometion
from .forms import RequirementsInfometionForm

from django.http import HttpResponse
from django.shortcuts import render
import csv,urllib

# # Create your views here.
class List(ListView):
    # 一覧するモデルを指定 -> `object_list`で取得可能
    model = RequirementsInfometion
    template_name = "app1/requirementsinfometion_list.html"

class Create(CreateView):
    # 一覧するモデルを指定 -> `object_list`で取得可能
    model = RequirementsInfometion
    form_class = RequirementsInfometionForm
    template_name = "app1/requirementsinfometion_form.html"
    success_url = "/"

def csv_export(request):
    # requirementsInfometionモデルの情報をcsv出力
    response = HttpResponse(content_type='text/csv; charset=Shift-JIS')
    date_time = getDateTime()
    str_time = date_time.strftime('%Y%m%d%H%M')
    f = "条件一覧" + "_" + str_time + ".csv"
    filename = urllib.parse.quote((f).encode("utf8"))
    response['Content-Disposition'] = 'attachment; filename*=UTF-8\'\'{}'.format(filename)

    writer = csv.writer(response)
    requirementsInfometions_list = getRequirementsInfometions()

    #region カラム列
    writer.writerow([
        "登録形態",
        "出力先_JTB",
        "出力先_トラベルコ",
        "出力先_パンフレット",
        "出発地",
        "大人人数",
        "出発日設定時間",
        "絶対設定_開始日付",
        "絶対設定_終了日付",
        "相対設定1_開始日付",
        "相対設定1_終了日付",
        "相対設定2_開始日付",
        "相対設定2_終了日付",
        "ルートパッケージID",
        "1都市目",
        "1都市目_現地出発日",
        "1都市目_ホテルタリフコード",
        "1都市目_LOP会社コード",
        "1都市目_プランID",
        "2都市目",
        "2都市目_現地出発日",
        "2都市目_ホテルタリフコード",
        "3都市目",
        "3都市目_現地出発日",
        "3都市目_ホテルタリフコード",
        "航空会社",
        "キャビンクラス（往路）",
        "キャビンクラス（複路）",
        "便名（往路）",
        "便名（複路）",
        "作成日時",
        "更新日時"
    ])
    #endregion カラム列

    #region データ列
    for requirementsInfometion in requirementsInfometions_list:
        writer.writerow([
           requirementsInfometion.registrationFormRadioButton, 
           requirementsInfometion.outputDestinationJtbChackBox,
           requirementsInfometion.outputDestinationTravelChackBox,
           requirementsInfometion.outputDestinationPamphletChackBox,
           requirementsInfometion.departurePoint,
           requirementsInfometion.adultNum,
           requirementsInfometion.departureDateSettingRadio,
           requirementsInfometion.absoluteSettingStartDate.strftime('%Y/%m/%d %H:%M:%S'),
           requirementsInfometion.absoluteSettingEndDate.strftime('%Y/%m/%d %H:%M:%S'),
           requirementsInfometion.relativeSettings1StartList,
           requirementsInfometion.relativeSettings1EndList,
           requirementsInfometion.relativeSettings2StartDayTxt,
           requirementsInfometion.relativeSettings2EndDayTxt,
           requirementsInfometion.rootPackageId,
           requirementsInfometion.firstCity,
           requirementsInfometion.firstCityDepartureDate,
           requirementsInfometion.firstCityHotelTariffCode,
           requirementsInfometion.firstCityLopCompanyCode,
           requirementsInfometion.firstCityPlanId,
           requirementsInfometion.secondtCity,
           requirementsInfometion.secondtCityDepartureDate,
           requirementsInfometion.secondtCityHotelTariffCode,
           requirementsInfometion.thirdCity,
           requirementsInfometion.thirdCityDepartureDate,
           requirementsInfometion.thirdCityHotelTariffCode,
           requirementsInfometion.airlinesSelectTxt,
           requirementsInfometion.cabinClassOutboundTripRadioButton,
           requirementsInfometion.cabinClassRoundTripRadioButton,
           requirementsInfometion.flightNumberOutboundTripTxt,
           requirementsInfometion.flightNumberRoundTripTxt,        
           requirementsInfometion.created_at.strftime('%Y/%m/%d %H:%M:%S'),
           requirementsInfometion.updated_at.strftime('%Y/%m/%d %H:%M:%S')])
    #endregion データ列
    
    return response

def getRequirementsInfometions():
  requirementsInfometion_list = RequirementsInfometion.objects.all()
  return requirementsInfometion_list

def getDateTime():
  latest_time = RequirementsInfometion.objects.latest("updated_at")
  latest_time = latest_time.updated_at
  return latest_time