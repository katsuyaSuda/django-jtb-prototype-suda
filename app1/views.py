from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, ListView, FormView

from .models import RequirementsInfometion
from .forms import RequirementsInfometionForm,CSVUploadForm

from django.http import HttpResponse
from django.shortcuts import render
import csv,urllib,io

from django.http import HttpResponseRedirect
from pathlib import Path
import boto3
from django.conf import settings

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

#region dbに登録した条件をcsvに全カラム出力
def csv_export(request):
    # requirementsInfometionモデルの情報をcsv出力
    response = HttpResponse(content_type='text/csv; charset=Shift-JIS')
    date_time = getDateTime()
    str_time = date_time.strftime('%Y%m%d%H%M')
    f = "条件一覧" + "_" + str_time + ".csv"
    filename = urllib.parse.quote((f).encode("utf8"))
    response['Content-Disposition'] = 'attachment; filename*=UTF-8\'\'{}'.format(filename)

    writer = csv.writer(response)

    #全ての条件リストを取得する
    requirementsInfometions_list = getRequirementsInfometions()

    # カラム列_論理名、カラム列_物理名の出力設定
    #True：カラム名を出力、False:カラム名を出力しない

    outPutcolLogicNameFlg = True
    outPutcolphysicsNameFlg = True

    # カラム列論理名flgがTrueの時出力
    #region カラム列_論理名
    if outPutcolLogicNameFlg==True:
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
            "直行便指定",
            "キャビンクラス（往路）",
            "キャビンクラス（複路）",
            "便名（往路）",
            "便名（複路）",
            "作成日時",
            "更新日時"
        ])
    #endregion カラム列_論理名

    # カラム列物理名flgがTrueの時出力
    #region カラム列_物理名
    if outPutcolphysicsNameFlg==True:
        writer.writerow([
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
            "firstCityHotelTariffCode1" + " " + "firstCityHotelTariffCode2",
            "firstCityLopCompanyCode",
            "firstCityPlanId",
            "secondtCity",
            "secondtCityDepartureDate",
            "secondtCityHotelTariffCode1" + " " + "secondtCityHotelTariffCode2",
            "thirdCity",
            "thirdCityDepartureDate",
            "thirdCityHotelTariffCode1" + " " + "thirdCityHotelTariffCode2",
            "airlinesSelectTxt",
            "useDirectFlightChackBox",
            "cabinClassOutboundTripRadioButton",
            "cabinClassRoundTripRadioButton",
            "flightNumberOutboundTripTxt",
            "flightNumberRoundTripTxt",        
            "created_at",
            "updated_at"])
    #endregion カラム列_物理名

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
           '{}{}'.format(requirementsInfometion.firstCityHotelTariffCode1, requirementsInfometion.firstCityHotelTariffCode2),
           requirementsInfometion.firstCityLopCompanyCode,
           requirementsInfometion.firstCityPlanId,
           requirementsInfometion.secondtCity,
           requirementsInfometion.secondtCityDepartureDate,
           '{}{}'.format(requirementsInfometion.secondtCityHotelTariffCode1, requirementsInfometion.secondtCityHotelTariffCode2),
           requirementsInfometion.thirdCity,
           requirementsInfometion.thirdCityDepartureDate,
           '{}{}'.format(requirementsInfometion.thirdCityHotelTariffCode1, requirementsInfometion.thirdCityHotelTariffCode2),
           requirementsInfometion.airlinesSelectTxt,
           requirementsInfometion.useDirectFlightChackBox,
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
#endregion dbに登録した条件をcsvに全カラム出力

#region dbに登録した条件をcsvに対象カラム出力
def csv_export_target(request):
    # requirementsInfometionモデルの情報をcsv出力
    response = HttpResponse(content_type='text/csv; charset=Shift-JIS')
    date_time = getDateTime()
    str_time = date_time.strftime('%Y%m%d%H%M')
    f = "条件一覧" + "_" + str_time + ".csv"
    filename = urllib.parse.quote((f).encode("utf8"))
    response['Content-Disposition'] = 'attachment; filename*=UTF-8\'\'{}'.format(filename)

    writer = csv.writer(response)

    #全ての条件リストを取得する
    requirementsInfometions_list = getRequirementsInfometions()

    # カラム列_論理名、カラム列_物理名の出力設定
    #True：カラム名を出力、False:カラム名を出力しない
    outPutcolLogicNameFlg = False
    outPutcolphysicsNameFlg = True

    # カラム列論理名flgがTrueの時出力
    #region カラム列_論理名
    if outPutcolLogicNameFlg==True:
        writer.writerow([
            "サービスパッケージID",
            "ルートパッケージID",
            "1都市目_都市コード",
            "1都市目_ホテルID",
            "出発地",
            "1都市目_現地出発日",
            "大人人数",
            "〇か月後の月初",
            "〇か月後の月末",
            "航空会社",
            "直行便指定",
            "キャビンクラス（往路）",
            "キャビンクラス（複路）",
            "便名（往路）",
            "便名（複路）",
        ])
    #endregion カラム列_論理名

    # カラム列物理名flgがTrueの時出力
    #region カラム列_物理名
    if outPutcolphysicsNameFlg==True:
        writer.writerow([
            "",
            "rootPackageId",
            "firstCity",
            "firstCityHotelTariffCode1" + " " + "firstCityHotelTariffCode2",
            "departurePoint",
            "firstCityDepartureDate",
            "adultNum",
            "",
            "",
            "airlinesSelectTxt",
            "useDirectFlightChackBox",
            "cabinClassOutboundTripRadioButton",
            "cabinClassRoundTripRadioButton",
            "flightNumberOutboundTripTxt",
            "flightNumberRoundTripTxt",        
        ])
    #endregion カラム列_物理名

    #region データ列
    for requirementsInfometion in requirementsInfometions_list:
        writer.writerow([ 
            "",
           requirementsInfometion.rootPackageId,
           requirementsInfometion.firstCity,
           '{}{}'.format(requirementsInfometion.firstCityHotelTariffCode1, requirementsInfometion.firstCityHotelTariffCode2),
           requirementsInfometion.departurePoint,
           requirementsInfometion.firstCityDepartureDate,
           requirementsInfometion.adultNum,
           "",
           "",
           requirementsInfometion.airlinesSelectTxt,
           requirementsInfometion.useDirectFlightChackBox,
           requirementsInfometion.cabinClassOutboundTripRadioButton,
           requirementsInfometion.cabinClassRoundTripRadioButton,
           requirementsInfometion.flightNumberOutboundTripTxt,
           requirementsInfometion.flightNumberRoundTripTxt,
        ])
    #endregion データ列  
    return response
#endregion dbに登録した条件をcsvに対象カラム出力



#region csvファイルをインポート
class CsvImport(FormView):
    form_class = CSVUploadForm
    template_name = 'app1/import.html'
    success_url = "/"

#endregion csvファイルをインポート

#region S3設定

s3 = boto3.resource('s3')
bucket_name = settings.AWS_STORAGE_BUCKET_NAME
bucket = s3.Bucket(bucket_name)

### ファイルパス名、パス ###
FILE = '対象ファイルCSV'
ORIGIN_PATH = Path(FILE)
SAVE_PATH = Path(FILE)

#region S3にCSVアップロード
def upload_file_to_s3(request):
    bucket.upload_file(str(ORIGIN_PATH), FILE)
    return render(request, 'app1/complete.html')
#endregion S3にCSVアップロード

#region S3内のファイルをローカルに持ってくる
def download_file_from_s3(request):
    bucket.download_file(FILE, str(SAVE_PATH))
    return render(request, 'app1/complete.html')
#endregion S3内のファイルをローカルに持ってくる

#region S3内のファイルをブラウザ上でダウンロードする
def download_file_from_s3_directly(request):
    url = boto3.client.generate_presigned_url(
        'get_object',
        Params = {
            'Bucket': bucket_name,
            'Key': str(SAVE_PATH),
        },
        ExpiresIn = 600,
    )
    return HttpResponseRedirect(url)
#endregion S3内のファイルをブラウザ上でダウンロードする

#endregion S3設定