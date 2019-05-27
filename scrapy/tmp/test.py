

# 初始化公司名称，用于记录异常
from bs4 import BeautifulSoup

from scrapy import getClassName
from scrapy.detailStructureScrapy.detailStructureScrapy import *

html = """<html>
 <head></head>
 <body>
  <div class="container m-t"> 
   <div class="company-certinfo risk-qingbao"> 
    <div class="risk-panel b-a"> 
     <a data-trigger="hover" class="pull-right" data-html="true" data-toggle="tooltip" data-placement="bottom" data-delay="500" title="" data-original-title="自身风险，聚合该公司自身存在的风险信息，其中包含：&lt;br&gt; 警示信息：裁判文书，严重违法，经营异常，行政处罚，税务行政处罚，环保处罚，动产抵押，土地抵押，税收违法，股权冻结，司法拍卖，股权出质，开庭公告；&lt;br&gt; 高风险信息：失信被执行人，被执行人。&lt;br&gt;&lt;br&gt; 关联风险，挖掘企业的关联人（如法定代表人，自然人股东，主要人员）和关联公司（如企业股东，投资公司，分公司）风险。其中包含：&lt;br&gt; 关联人风险：失信被执行人和被执行人信息；&lt;br&gt; 关联公司风险：同企业自身风险信息。&lt;br&gt;&lt;br&gt;  提示信息，法定代表人变更，大股东变更；&lt;br&gt;&lt;br&gt;说明：风险扫描中的数据是基于公开信息通过风险模型大数据分析后的结果，仅供用户参考，并不代表企查查的任何明示、暗示之观点或保证。若因参考、使用该信息造成损失的，由用户自行负责，企查查不承担任何责任。"><i class="m_question"></i></a> 
     <img src="/material/theme/chacha/cms/v2/images/risk_title@2x.png" /> 
     <span class="tl"> <a onclick="zhugeTrack('企业主页-风险扫描',{'企业名称':'上海盒马网络科技有限公司'});" href="/risk?obj=1&amp;unique=e45ee37279ffb3f2ce9bbbcfa39d8133&amp;property=1">自身风险 <span class="text-danger">65</span></a> <a onclick="zhugeTrack('企业主页-风险扫描',{'企业名称':'上海盒马网络科技有限公司'});" href="/risk?obj=1&amp;unique=e45ee37279ffb3f2ce9bbbcfa39d8133&amp;property=2">关联风险 <span class="text-danger">82</span></a> <a onclick="zhugeTrack('企业主页-风险扫描',{'企业名称':'上海盒马网络科技有限公司'});" href="/risk?obj=1&amp;unique=e45ee37279ffb3f2ce9bbbcfa39d8133&amp;property=3">提示信息 <span class="text-gray">2</span></a> </span> 
     <a onclick="zhugeTrack('企业主页-风险扫描',{'企业名称':'上海盒马网络科技有限公司'});" href="/risk?obj=1&amp;unique=e45ee37279ffb3f2ce9bbbcfa39d8133&amp;property=1" class="btn btn-danger pull-right">查看风险</a> 
    </div> 
    <div class="qingbao-panel b-a"> 
     <img src="/material/theme/chacha/cms/v2/images/qingbao_title@2x.png" /> 
     <div class="qingbao-scrollinfo" id="qingbaoScrollinfo"> 
      <a class="item" onclick="zhugeTrack('企业主页-情报动态',{'企业名称':'上海盒马网络科技有限公司'});" href="/company_intelligence?keyno=e45ee37279ffb3f2ce9bbbcfa39d8133&amp;companyname=%E4%B8%8A%E6%B5%B7%E7%9B%92%E9%A9%AC%E7%BD%91%E7%BB%9C%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8" style="transform: translateY(100%); display: block;"> <span class="m-r">2019-05-13</span> 新增 <span class="text-primary">开庭公告</span> </a> 
      <a class="item" onclick="zhugeTrack('企业主页-情报动态',{'企业名称':'上海盒马网络科技有限公司'});" href="/company_intelligence?keyno=e45ee37279ffb3f2ce9bbbcfa39d8133&amp;companyname=%E4%B8%8A%E6%B5%B7%E7%9B%92%E9%A9%AC%E7%BD%91%E7%BB%9C%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8" style="transform: translateY(100%); display: block;"> <span class="m-r">2019-05-07</span> 新增 <span class="text-danger">裁判文书</span> </a> 
      <a class="item" onclick="zhugeTrack('企业主页-情报动态',{'企业名称':'上海盒马网络科技有限公司'});" href="/company_intelligence?keyno=e45ee37279ffb3f2ce9bbbcfa39d8133&amp;companyname=%E4%B8%8A%E6%B5%B7%E7%9B%92%E9%A9%AC%E7%BD%91%E7%BB%9C%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8" style="transform: translateY(100%); display: block;"> <span class="m-r">2019-04-03</span> 新增 <span class="text-primary">开庭公告</span> </a> 
      <a class="item" onclick="zhugeTrack('企业主页-情报动态',{'企业名称':'上海盒马网络科技有限公司'});" href="/company_intelligence?keyno=e45ee37279ffb3f2ce9bbbcfa39d8133&amp;companyname=%E4%B8%8A%E6%B5%B7%E7%9B%92%E9%A9%AC%E7%BD%91%E7%BB%9C%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8" style="transform: translateY(100%); display: block;"> <span class="m-r">2019-03-30</span> 新增 <span class="text-danger">裁判文书</span> </a> 
      <a class="item" onclick="zhugeTrack('企业主页-情报动态',{'企业名称':'上海盒马网络科技有限公司'});" href="/company_intelligence?keyno=e45ee37279ffb3f2ce9bbbcfa39d8133&amp;companyname=%E4%B8%8A%E6%B5%B7%E7%9B%92%E9%A9%AC%E7%BD%91%E7%BB%9C%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8" style="transform: translateY(0px); display: block;"> <span class="m-r">2019-03-17</span> 新增 <span class="text-primary">开庭公告</span> </a> 
     </div> 
     <a onclick="zhugeTrack('企业主页-情报动态',{'企业名称':'上海盒马网络科技有限公司'});" href="/company_intelligence?keyno=e45ee37279ffb3f2ce9bbbcfa39d8133&amp;companyname=上海盒马网络科技有限公司" class="btn btn-primary pull-right">查看情报</a> 
    </div> 
   </div> 
   <script type="text/javascript">
    $(function() {
        qingbaoCarousel();
    })
    
</script> 
   <div class="row"> 
    <div class="col-sm-9 no-padding-right"> 
     <header style="height: 44px;position: relative;"> 
      <div class="own-switch fixed" style="display: block;"> 
       <a class="own-switchback active" href="/firm_e45ee37279ffb3f2ce9bbbcfa39d8133.html" onclick="zhugeTrack('企业主页-企业主页tab',{'企业名称':'上海盒马网络科技有限公司'});">
        <div class="zi">
         企业主页
        </div></a> 
       <a class="own-switchto " href="https://pinpai.qichacha.com/own_e45ee37279ffb3f2ce9bbbcfa39d8133.html" onclick="zhugeTrack('企业主页-品牌主页tab',{'企业名称':'上海盒马网络科技有限公司'});">
        <div class="zi">
         品牌主页
        </div> <span class="count">1</span> </a> 
      </div> 
      <div class="company-nav"> 
       <div class="company-nav-tab current"> 
        <a class="company-nav-head " onclick="" href="#base" id="base_title" tabid="base"><h2>基本信息</h2> <span>112</span></a> 
        <div class="company-nav-items"> 
         <a data-pos="Cominfo" onclick="zhugeTrack('企业主页-基本信息-工商信息',{'企业名称':'上海盒马网络科技有限公司'});">工商信息 <span class="text-primary"></span> </a> 
         <a data-pos="partnerslist" onclick="zhugeTrack('企业主页-基本信息-股东信息',{'企业名称':'上海盒马网络科技有限公司'});">股东信息 <span class="text-primary">1</span> </a> 
         <a data-pos="guquan" onclick="zhugeTrack('企业主页-基本信息-股权穿透图',{'企业名称':'上海盒马网络科技有限公司'});">股权穿透图 <span class="text-primary"></span> </a> 
         <a data-pos="touzilist" onclick="zhugeTrack('企业主页-基本信息-对外投资',{'企业名称':'上海盒马网络科技有限公司'});">对外投资 <span class="text-primary">2</span> </a> 
         <a data-pos="syrlist" onclick="zhugeTrack('企业主页-基本信息-最终受益人',{'企业名称':'上海盒马网络科技有限公司'});">最终受益人 <span class="text-primary">2</span> </a> 
         <a data-pos="kzrtupu" onclick="zhugeTrack('企业主页-基本信息-实际控制人',{'企业名称':'上海盒马网络科技有限公司'});">实际控制人 <span class="text-primary"></span> </a> 
         <a data-pos="holdcolist" onclick="zhugeTrack('企业主页-基本信息-控股企业',{'企业名称':'上海盒马网络科技有限公司'});">控股企业 <span class="text-primary">2</span> </a> 
         <a data-pos="Mainmember" onclick="zhugeTrack('企业主页-基本信息-主要成员',{'企业名称':'上海盒马网络科技有限公司'});">主要成员 <span class="text-primary">4</span> </a> 
         <span>总公司 <span>0</span></span> 
         <a data-pos="Subcom" onclick="zhugeTrack('企业主页-基本信息-分支机构',{'企业名称':'上海盒马网络科技有限公司'});">分支机构 <span class="text-primary">72</span> </a> 
         <span>企业公示 <span>0</span></span> 
         <a data-pos="muhou" onclick="zhugeTrack('企业主页-基本信息-关联图谱',{'企业名称':'上海盒马网络科技有限公司'});">关联图谱 <span class="text-primary"></span> </a> 
         <a data-pos="cwjx" onclick="zhugeTrack('企业主页-基本信息-财务简析',{'企业名称':'上海盒马网络科技有限公司'});">财务简析 <span class="text-primary"></span> </a> 
         <a data-pos="thyfx" onclick="zhugeTrack('企业主页-基本信息-同业分析',{'企业名称':'上海盒马网络科技有限公司'});">同业分析 <span class="text-primary"></span> </a> 
         <span>建筑资质 <span>0</span></span> 
         <a data-pos="Changelist" onclick="zhugeTrack('企业主页-基本信息-变更记录',{'企业名称':'上海盒马网络科技有限公司'});">变更记录 <span class="text-primary">25</span> </a> 
        </div> 
       </div> 
       <div class="company-nav-tab"> 
        <a class="company-nav-head " onclick="" href="#susong" id="susong_title" tabid="susong"><h2>法律诉讼</h2> <span>73</span></a> 
        <div class="company-nav-items"> 
         <span>被执行人 <span>0</span></span> 
         <span>失信信息 <span>0</span></span> 
         <a data-pos="wenshulist" onclick="zhugeTrack('企业主页-法律诉讼-裁判文书',{'企业名称':'上海盒马网络科技有限公司'});">裁判文书 <span class="text-danger">30</span> </a> 
         <span>法院公告 <span>0</span></span> 
         <a data-pos="noticelist" onclick="zhugeTrack('企业主页-法律诉讼-开庭公告',{'企业名称':'上海盒马网络科技有限公司'});">开庭公告 <span class="text-danger">43</span> </a> 
         <span>送达公告 <span>0</span></span> 
         <span>司法协助 <span>0</span></span> 
         <span>立案信息 <span>0</span></span> 
        </div> 
       </div> 
       <div class="company-nav-tab"> 
        <a class="company-nav-head " onclick="" href="#run" id="run_title" tabid="run"><h2>经营状况</h2> <span>999+</span></a> 
        <div class="company-nav-items"> 
         <a data-pos="licenslist" onclick="zhugeTrack('企业主页-经营状况-行政许可',{'企业名称':'上海盒马网络科技有限公司'});">行政许可 <span class="text-primary">53</span> </a> 
         <a data-pos="taxCreditList" onclick="zhugeTrack('企业主页-经营状况-税务信用',{'企业名称':'上海盒马网络科技有限公司'});">税务信用 <span class="text-primary">1</span> </a> 
         <a data-pos="tenderlist" onclick="zhugeTrack('企业主页-经营状况-招投标',{'企业名称':'上海盒马网络科技有限公司'});">招投标 <span class="text-primary">1</span> </a> 
         <a data-pos="joblist" onclick="zhugeTrack('企业主页-经营状况-招聘',{'企业名称':'上海盒马网络科技有限公司'});">招聘 <span class="text-primary">999+</span> </a> 
         <span>财务总览 <span>0</span></span> 
         <span>进出口信用 <span>0</span></span> 
         <span>微信公众号 <span>0</span></span> 
         <a data-pos="weibolist" onclick="zhugeTrack('企业主页-经营状况-微博',{'企业名称':'上海盒马网络科技有限公司'});">微博 <span class="text-primary">2</span> </a> 
         <a data-pos="newslist" onclick="zhugeTrack('企业主页-经营状况-新闻舆情',{'企业名称':'上海盒马网络科技有限公司'});">新闻舆情 <span class="text-primary">999+</span> </a> 
         <a data-pos="yblist" onclick="zhugeTrack('企业主页-经营状况-公告研报',{'企业名称':'上海盒马网络科技有限公司'});">公告研报 <span class="text-primary">17</span> </a> 
         <span>地块公示 <span>0</span></span> 
         <span>购地信息 <span>0</span></span> 
         <span>土地转让 <span>0</span></span> 
         <span>债券信息 <span>0</span></span> 
         <a data-pos="spotCheckList" onclick="zhugeTrack('企业主页-经营状况-抽查检查',{'企业名称':'上海盒马网络科技有限公司'});">抽查检查 <span class="text-primary">2</span> </a> 
         <span>电信许可 <span>0</span></span> 
         <a data-pos="supplierlist" onclick="zhugeTrack('企业主页-经营状况-供应商',{'企业名称':'上海盒马网络科技有限公司'});">供应商 <span class="text-primary">1</span> </a> 
         <a data-pos="customerlist" onclick="zhugeTrack('企业主页-经营状况-客户',{'企业名称':'上海盒马网络科技有限公司'});">客户 <span class="text-primary">1</span> </a> 
         <span>信用评级 <span>0</span></span> 
        </div> 
       </div> 
       <div class="company-nav-tab"> 
        <a class="company-nav-head " onclick="" href="#fengxian" id="fengxian_title" tabid="fengxian"><h2>经营风险</h2> <span>6</span></a> 
        <div class="company-nav-items"> 
         <a data-pos="Exceptions" onclick="zhugeTrack('企业主页-经营风险-经营异常',{'企业名称':'上海盒马网络科技有限公司'});">经营异常 <span class="text-danger">1</span> </a> 
         <span>严重违法 <span>0</span></span> 
         <a data-pos="pledgeList" onclick="zhugeTrack('企业主页-经营风险-股权出质',{'企业名称':'上海盒马网络科技有限公司'});">股权出质 <span class="text-danger">2</span> </a> 
         <span>股权质押 <span>0</span></span> 
         <a data-pos="penaltylist" onclick="zhugeTrack('企业主页-经营风险-行政处罚',{'企业名称':'上海盒马网络科技有限公司'});">行政处罚 <span class="text-danger">3</span> </a> 
         <span>税收违法 <span>0</span></span> 
         <span>动产抵押 <span>0</span></span> 
         <span>环保处罚 <span>0</span></span> 
         <span>清算信息 <span>0</span></span> 
         <span>司法拍卖 <span>0</span></span> 
         <span>土地抵押 <span>0</span></span> 
         <span>简易注销 <span></span></span> 
         <span>公示催告 <span>0</span></span> 
         <span>欠税公告 <span>0</span></span> 
        </div> 
       </div> 
       <div class="company-nav-tab"> 
        <a class="company-nav-head " onclick="" href="#report" id="report_title" tabid="report"><h2>企业发展</h2> <span>19</span></a> 
        <div class="company-nav-items"> 
         <a data-pos="report" onclick="zhugeTrack('企业主页-企业发展-企业年报',{'企业名称':'上海盒马网络科技有限公司'});">企业年报 <span class="text-primary">3</span> </a> 
         <a data-pos="financingInfo" onclick="zhugeTrack('企业主页-企业发展-融资信息',{'企业名称':'上海盒马网络科技有限公司'});">融资信息 <span class="text-primary">1</span> </a> 
         <span>投资机构 <span>0</span></span> 
         <a data-pos="memberInfo" onclick="zhugeTrack('企业主页-企业发展-核心人员',{'企业名称':'上海盒马网络科技有限公司'});">核心人员 <span class="text-primary">1</span> </a> 
         <a data-pos="productInfo" onclick="zhugeTrack('企业主页-企业发展-企业业务',{'企业名称':'上海盒马网络科技有限公司'});">企业业务 <span class="text-primary">1</span> </a> 
         <a data-pos="compatProductInfo" onclick="zhugeTrack('企业主页-企业发展-竞品信息',{'企业名称':'上海盒马网络科技有限公司'});">竞品信息 <span class="text-primary">13</span> </a> 
         <span>私募基金 <span></span></span> 
        </div> 
       </div> 
       <div class="company-nav-tab"> 
        <a class="company-nav-head " onclick="" href="#assets" id="assets_title" tabid="assets"><h2>知识产权</h2> <span>21</span></a> 
        <div class="company-nav-items"> 
         <span>商标信息 <span>0</span></span> 
         <span>专利信息 <span>0</span></span> 
         <a data-pos="zhengshulist" onclick="zhugeTrack('企业主页-知识产权-证书信息',{'企业名称':'上海盒马网络科技有限公司'});">证书信息 <span class="text-primary">2</span> </a> 
         <a data-pos="zzqlist" onclick="zhugeTrack('企业主页-知识产权-作品著作权',{'企业名称':'上海盒马网络科技有限公司'});">作品著作权 <span class="text-primary">17</span> </a> 
         <span>软件著作权 <span>0</span></span> 
         <a data-pos="websitelist" onclick="zhugeTrack('企业主页-知识产权-网站信息',{'企业名称':'上海盒马网络科技有限公司'});">网站信息 <span class="text-primary">2</span> </a> 
        </div> 
       </div> 
       <div class="company-nav-tab"> 
        <a class="company-nav-head viptab" onclick="" href="#history" id="history_title" tabid="history"><h2>历史信息</h2> <span>16</span></a> 
        <div class="company-nav-items"> 
         <a data-pos="hiscominfo" onclick="zhugeTrack('企业主页-历史信息-工商信息',{'企业名称':'上海盒马网络科技有限公司'});">工商信息 <span class="text-primary"></span> </a> 
         <span>对外投资 <span>0</span></span> 
         <a data-pos="hispartnerlist" onclick="zhugeTrack('企业主页-历史信息-历史股东',{'企业名称':'上海盒马网络科技有限公司'});">历史股东 <span class="text-primary">1</span> </a> 
         <span>失信信息 <span>0</span></span> 
         <a data-pos="hiszhixinglist" onclick="zhugeTrack('企业主页-历史信息-被执行人',{'企业名称':'上海盒马网络科技有限公司'});">被执行人 <span class="text-danger">3</span> </a> 
         <span>法院公告 <span>0</span></span> 
         <span>裁判文书 <span>0</span></span> 
         <a data-pos="hisxzcf" onclick="zhugeTrack('企业主页-历史信息-行政处罚',{'企业名称':'上海盒马网络科技有限公司'});">行政处罚 <span class="text-danger">1</span> </a> 
         <span>动产抵押 <span>0</span></span> 
         <span>开庭公告 <span>0</span></span> 
         <span>股权出质 <span>0</span></span> 
         <a data-pos="hisxzxk" onclick="zhugeTrack('企业主页-历史信息-行政许可',{'企业名称':'上海盒马网络科技有限公司'});">行政许可 <span class="text-primary">10</span> </a> 
        </div> 
       </div> 
      </div> 
     </header> 
     <div id="load_data" style="display: none;"> 
      <section class="panel text-center" style="padding:100px 0;"> 
       <img src="/material/theme/chacha/cms/v2/images/preloader.gif" style="width:70px;margin-top:50px;" /> 
      </section> 
     </div> 
     <div class="data_div" id="base_div" style="display: block;"> 
      <div class="base_info"></div> 
      <section class="panel b-a clear m_dataTab"> 
       <div class="panel-body" style="padding-top: 5px;"> 
        <a href="javascript:;" onclick="boxScrollNew('#Cominfo');zhugeTrack('企业主页-基本信息-工商信息',{'企业名称':'上海盒马网络科技有限公司'});" class="btn btn-sm btn-default m-t-sm  m-r-sm" style="white-space:nowrap;"> 工商信息 </a> 
        <a href="javascript:;" onclick="boxScrollNew('#partnerslist');zhugeTrack('企业主页-基本信息-股东信息',{'企业名称':'上海盒马网络科技有限公司'});" class="btn btn-sm btn-default m-t-sm  m-r-sm" style="white-space:nowrap;"> 股东信息&nbsp;1 </a> 
        <a href="javascript:;" onclick="boxScrollNew('#guquan');zhugeTrack('企业主页-基本信息-股权穿透图')" class="btn btn-sm btn-default m-t-sm  m-r-sm" style="white-space:nowrap;"> 股权穿透图 </a> 
        <a href="javascript:;" onclick="boxScrollNew('#touzilist');zhugeTrack('企业主页-基本信息-对外投资',{'企业名称':'上海盒马网络科技有限公司'});" class="btn btn-sm btn-default m-t-sm  m-r-sm" style="white-space:nowrap;"> 对外投资&nbsp;2 </a> 
        <a href="javascript:;" onclick="boxScrollNew('#syrlist');zhugeTrack('企业主页-基本信息-最终受益人',{'企业名称':'上海盒马网络科技有限公司'});" class="btn btn-sm btn-default m-t-sm  m-r-sm" style="white-space:nowrap;"> 最终受益人&nbsp;2 </a> 
        <a href="javascript:;" onclick="boxScrollNew('#kzrtupu');zhugeTrack('企业主页-基本信息-最终受益人',{'企业名称':'上海盒马网络科技有限公司'});" class="btn btn-sm btn-default m-t-sm   m-r-sm" style="white-space:nowrap;"> 实际控制人 <span class="icon-new"></span> </a> 
        <a href="javascript:;" onclick="boxScrollNew('#holdcolist');zhugeTrack('企业主页-基本信息-控股企业',{'企业名称':'上海盒马网络科技有限公司'});" class="btn btn-sm btn-default m-t-sm  m-r-sm" style="white-space:nowrap;"> 控股企业&nbsp;2 </a> 
        <a href="javascript:;" onclick="boxScrollNew('#Mainmember');zhugeTrack('企业主页-基本信息-主要成员',{'企业名称':'上海盒马网络科技有限公司'});" class="btn btn-sm btn-default m-t-sm  m-r-sm" style="white-space:nowrap;"> 主要成员&nbsp;4 </a> 
        <a href="javascript:;" class="btn btn-sm btn-default m-t-sm  m-r-sm c_disable" style="white-space:nowrap;cursor: default"> 总公司&nbsp;0 </a> 
        <a href="javascript:;" onclick="boxScrollNew('#Subcom');zhugeTrack('企业主页-基本信息-分支机构',{'企业名称':'上海盒马网络科技有限公司'});" class="btn btn-sm btn-default m-t-sm  m-r-sm" style="white-space:nowrap;"> 分支机构&nbsp;72 </a> 
        <a href="javascript:;" class="btn btn-sm btn-default m-t-sm  m-r-sm c_disable" style="white-space:nowrap;cursor: default"> 企业公示&nbsp;0 </a> 
        <a href="javascript:;" onclick="boxScrollNew('#muhou');zhugeTrack('企业主页-基本信息-企业关联图谱',{'企业名称':'上海盒马网络科技有限公司'})" class="btn btn-sm btn-default m-t-sm m-r-sm" style="white-space:nowrap;"> 企业关联图谱&nbsp; </a> 
        <a href="javascript:;" onclick="boxScrollNew('#cwjx');zhugeTrack('企业主页-基本信息-财务简析',{'企业名称':'上海盒马网络科技有限公司'});" class="btn btn-sm btn-default m-t-sm  m-r-sm" style="white-space:nowrap;"> 财务简析 </a> 
        <a href="javascript:;" onclick="boxScrollNew('#thyfx');zhugeTrack('企业主页-基本信息-同业分析',{'企业名称':'上海盒马网络科技有限公司'});" class="btn btn-sm btn-default m-t-sm  m-r-sm" style="white-space:nowrap;"> 同业分析 </a> 
        <a href="javascript:;" class="btn btn-sm btn-default m-t-sm  m-r-sm c_disable" style="white-space:nowrap;cursor: default"> 建筑资质&nbsp;0 <span class="icon-new"></span> </a> 
        <a href="javascript:;" onclick="boxScrollNew('#Changelist');zhugeTrack('企业主页-基本信息-变更记录',{'企业名称':'上海盒马网络科技有限公司'});" class="btn btn-sm btn-default m-t-sm  m-r-sm" style="white-space:nowrap;"> 变更记录&nbsp;25 </a> 
       </div> 
      </section> 
      <section class="panel b-a" id="Cominfo"> 
       <div class="tcaption"> 
        <h3 class="title">工商信息</h3> 
        <a onclick="zhugeTrack('企业主页-工商信息-查看工商官网快照',{'企业名称':'上海盒马网络科技有限公司'});" class="text-primary kz_anim" href="/snapshoot_e45ee37279ffb3f2ce9bbbcfa39d8133.html" target="_blank"> 查看工商官网快照 </a> 
        <span class="watermark"></span> 
       </div> 
       <div class="prot-gltu" id="protGltu"></div> 
       <table class="ntable" style="margin-bottom: -1px;"> 
        <tbody>
         <tr> 
          <td width="297" class="tb text-center"> 法定代表人信息 </td> 
          <td width="253" class="tb text-center">企业关联图谱<img class="m-l-sm" style="width: 30px;margin-top: -2px" src="/material/theme/chacha/cms/v2/images/icon_hot@2x.png" /></td> 
          <td class="tb text-center">股权结构图</td> 
         </tr> 
         <tr> 
          <td height="180" class="ma_left"> 
           <div class="boss-td"> 
            <div class="clearfix" style="min-height: 76px;padding-top: 8px;overflow: hidden;"> 
             <div class="pull-left bheadimgkuang"> 
              <img class="bheadimg" onerror="this.src='/material/theme/chacha/cms/v2/images/boss_head.png'" src="https://co-image.qichacha.com/PersonImage/p73ac1d107d8235907d5087e3b3abe6b.jpg" /> 
             </div> 
             <div class="pull-left" style="max-width: 218px;"> 
              <a href="/pl_p73ac1d107d8235907d5087e3b3abe6b.html" class="bname"><h2 class="seo font-20">侯毅</h2></a> 
              <span class="brenzhi">共任职 <span class="text-danger">28</span> 家企业，主要分布：</span> 
             </div> 
            </div> 
            <div onclick="location.href='/pl_p73ac1d107d8235907d5087e3b3abe6b.html'" class="ba-table-base" style="cursor: pointer;"> 
             <div class="province-info"> 
              <div class="clearfix"> 
               <div class="col-xs-4"> 
                <div class="m-t-xs">
                 <span class="icon-place"></span>上海 (共
                 <span class="text-danger">11</span>家)
                </div> 
               </div> 
               <div class="col-xs-8 text-right"> 
                <div class="m-t-xs">
                  上海盒马网络科技有限…等 
                </div> 
               </div> 
              </div> 
              <div class="clearfix"> 
               <div class="col-xs-4"> 
                <div class="m-t-xs">
                 <span class="icon-place"></span>广东 (共
                 <span class="text-danger">3</span>家)
                </div> 
               </div> 
               <div class="col-xs-8 text-right"> 
                <div class="m-t-xs">
                  广州盒马鲜生网络科技…等 
                </div> 
               </div> 
              </div> 
              <div class="clearfix"> 
               <div class="col-xs-4"> 
                <div class="m-t-xs">
                 <span class="icon-place"></span>其他 (共
                 <span class="text-danger">14</span>家)
                </div> 
               </div> 
               <div class="col-xs-8 text-right"> 
                <div class="m-t-xs">
                  杭州盒马网络科技有限…等 
                </div> 
               </div> 
              </div> 
             </div> 
            </div> 
           </div> </td> 
          <td class=""> 
           <div style="height: 108px;text-align: center;cursor:pointer;"> 
            <a onclick="zhugeTrack('企业主页-工商信息-查看企业关联图谱',{'企业名称':'上海盒马网络科技有限公司'});" href="/company_muhou3?keyNo=e45ee37279ffb3f2ce9bbbcfa39d8133&amp;name=%E4%B8%8A%E6%B5%B7%E7%9B%92%E9%A9%AC%E7%BD%91%E7%BB%9C%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8"><img style="width: 246px;" src="/material/theme/chacha/cms/v2/images/icon_gltp@2x.png" /></a> 
           </div> 
           <div class="ba-table-base">
            <a onclick="zhugeTrack('企业主页-工商信息-查看企业关联图谱',{'企业名称':'上海盒马网络科技有限公司'});" href="/company_muhou3?keyNo=e45ee37279ffb3f2ce9bbbcfa39d8133&amp;name=%E4%B8%8A%E6%B5%B7%E7%9B%92%E9%A9%AC%E7%BD%91%E7%BB%9C%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8" class="btn btn-primary basePageBt">查看详情</a>
           </div> </td> 
          <td class="guquan-static-td"> 
           <div style="height: 108px;overflow: hidden;"> 
            <img src="/material/theme/chacha/cms/v2/images/base_guquan_bg.png" /> 
            <div class="text1">
             上海盒马网络科技有限公司
            </div> 
            <div class="text2">
             Hema (Hong Kong) Limited
            </div> 
            <div class="text3">
              股权比例：
             <span class="text-warning m-r">100%</span> 认缴金额：
             <span class="text-warning">64,913.00万元</span> 
            </div> 
           </div> 
           <div onclick="guquanDetail('e45ee37279ffb3f2ce9bbbcfa39d8133','上海盒马网络科技有限公司');zhugeTrack('企业主页-工商信息-查看股权结构图',{'企业名称':'上海盒马网络科技有限公司'});" class="mengban"></div> 
           <div class="ba-table-base">
            <a href="javascript:;" onclick="guquanDetail('e45ee37279ffb3f2ce9bbbcfa39d8133','上海盒马网络科技有限公司');zhugeTrack('企业主页-工商信息-查看股权结构图',{'企业名称':'上海盒马网络科技有限公司'});" class="btn btn-primary basePageBt">查看详情</a>
           </div> </td> 
         </tr> 
        </tbody>
       </table> 
       <table class="ntable"> 
        <tbody>
         <tr> 
          <td width="20%" class="tb">注册资本</td> 
          <td width="30%" class=""> 64913万元人民币 </td> 
          <td width="20%" class="tb">实缴资本</td> 
          <td width="30%" class=""> - </td> 
         </tr> 
         <tr> 
          <td class="tb">经营状态</td> 
          <td class=""> 存续（在营、开业、在册） </td> 
          <td class="tb" width="18%">成立日期</td> 
          <td class=""> 2015-06-02 </td> 
         </tr> 
         <tr> 
          <td class="tb">统一社会信用代码</td> 
          <td class=""> 91310115342050446K </td> 
          <td class="tb">纳税人识别号</td> 
          <td class=""> 91310115342050446K </td> 
         </tr> 
         <tr> 
          <td class="tb">注册号</td> 
          <td class=""> 310141000157096 </td> 
          <td class="tb" width="15%">组织机构代码</td> 
          <td class=""> 34205044-6 </td> 
         </tr> 
         <tr> 
          <td class="tb">企业类型</td> 
          <td class=""> 有限责任公司(台港澳法人独资) </td> 
          <td class="tb">所属行业</td> 
          <td class=""> 信息传输、软件和信息技术服务业 </td> 
         </tr> 
         <tr> 
          <td class="tb">核准日期</td> 
          <td class="" style="max-width:301px;"> 2015-06-02 </td> 
          <td class="tb">登记机关</td> 
          <td class=""> 自由贸易试验区市场监管局 </td> 
         </tr> 
         <tr> 
          <td class="tb">所属地区</td> 
          <td class="" style="max-width:301px;"> 上海市 </td> 
          <td class="tb">英文名</td> 
          <td class=""> Shanghai Yi Heng Network Technology Co., Ltd. </td> 
         </tr> 
         <tr> 
          <td class="tb"> 曾用名 </td> 
          <td class=""> <span>上海翌恒网络科技有限公司&nbsp;&nbsp;</span> </td> 
          <td class="tb"> 参保人数 </td> 
          <td class=""> 337 </td> 
         </tr> 
         <tr> 
          <td class="tb"> 人员规模 </td> 
          <td class=""> 500-999人 </td> 
          <td class="tb"> 营业期限 </td> 
          <td class=""> 2015-06-02 至 2046-09-18 </td> 
         </tr> 
         <tr> 
          <td class="tb">企业地址</td> 
          <td class="" colspan="3"> 中国(上海)自由贸易试验区浦东大道2123号3层3E-1842室 <a onclick="showMapModal('中国(上海)自由贸易试验区浦东大道2123号3层3E-1842室','上海市');zhugeTrack('企业主页-查看地址',{'企业名称':'上海盒马网络科技有限公司'});" class="m-l c_a"> 查看地图</a> <a onclick="zhugeTrack('企业主页-附近公司',{'企业名称':'上海盒马网络科技有限公司'});" href="/map?keyNo=e45ee37279ffb3f2ce9bbbcfa39d8133" class="m-l c_a"> 附近企业</a> </td> 
         </tr> 
         <tr> 
          <td class="tb">经营范围</td> 
          <td class="" colspan="3"> 计算机网络专业领域内的技术开发并提供相关技术咨询及技术服务,计算机系统集成的设计、安装、调试、维护,通信设备维修;房地产经纪;第三方物流服务;家政服务;保洁服务;物业管理;病虫害防治服务;搬运装卸;绿化养护;自有设备出租;摄影摄像服务(测绘航空摄影除外);票务代理(航空票务代理除外);餐饮企业管理;创意服务;设计、制作、代理各类广告;图文设计、制作;市场营销策划;食品、宠物用品、服装、成人保健用品、日用百货、家用电器、食用农产品、粮食(中央储备粮食除外)、家居用品、电子产品及配件、甘油、香料香精(除危险化学品、监控化学品、民用爆炸物品)、照相器材、家具、针纺织品、化妆品、办公用品、体育用品及器材、玩具、汽车用品、汽摩配件、珠宝首饰(毛钻、裸钻除外)、工艺品(文物、象牙及其制品除外)、五金交电、计算机软硬件及配件(音像制品除外)、机械设备、化工产品(危险化学品除外)、消防器材、建筑装饰材料(钢材、水泥除外)、一类医疗器械、二类医疗器械、母婴用品、乳制品(含婴幼儿配方乳粉)、花卉、酒类的批发、零售(店铺零售限分支机构)、网上零售、进出口、佣金代理(拍卖除外),并提供上述商品相关售后配套服务;以自动售货机销售方式进行预包装食品的零售,仓储服务(除危险品,限分公司经营);餐饮服务;洗衣服务;家电、家具维修服务;净水器清洗服务;服装、皮具、鞋包的修补及维护;美容、美发、美甲、健身服务;犬只美容、寄养、销售;儿童游乐设施经营(游艺机、危险项目除外)(以上项目均限分支机构经营)。【依法须经批准的项目,经相关部门批准后方可开展经营活动】。 </td> 
         </tr> 
        </tbody>
       </table> 
      </section> 
      <section class="panel b-a clear" id="partnerslist"> 
       <div class="tcaption"> 
        <h3 class="title">股东信息</h3> 
        <span class="tbadge">1</span> 
        <span class="thist">（查看更多1条 <a onclick="jumpHistory('hispartnerlist')">历史股东</a>）</span> 
        <span class="watermark"></span> 
       </div> 
       <table class="ntable ntable-odd "> 
        <tbody>
         <tr> 
          <th class="tx">序号</th> 
          <th width="">股东（发起人） <a onclick="boxScrollNew('#syrlist')">查看最终受益人&gt;</a> </th> 
          <th width="105">持股比例</th> 
          <th width="185">认缴出资额(万元)</th> 
          <th width="130">认缴出资日期</th> 
         </tr> 
         <tr> 
          <td class="tx">1</td> 
          <td> 
           <table class="insert-table"> 
            <tbody>
             <tr> 
              <td width="50"> <span class="headimg"> <img src="https://qccdata.qichacha.com/AutoImage/hcb57b19bc9cd13855cfb774959b8730.jpg?x-oss-process=image/resize,w_120" /> </span> </td> 
              <td> <a href="/firm_hcb57b19bc9cd13855cfb774959b8730.html" target="_blank"><h3 class="seo font-14"> Hema (Hong Kong) Limited</h3></a> 
               <div class="m-t-xs"> 
                <span class="ntag sm text-danger m-r-xs" style="margin-bottom: 2px;">大股东</span> 
                <span class="ntag sm text-warning m-r-xs" style="margin-bottom: 2px;">实际控制人</span> 
                <span class="ntag sm text-primary" style="margin-bottom: 2px;">最终受益人</span> 
                <span class="ntag sm text-pl" style="margin-bottom: 2px;">香港</span> 
               </div> </td> 
              <td width="130" class="text-right"> <a class="btn-touzi" href="/firm_hcb57b19bc9cd13855cfb774959b8730.html">他投资11家公司 &gt; </a> </td> 
             </tr> 
            </tbody>
           </table> </td> 
          <td class="text-center"> 100% </td> 
          <td class="text-center"> 64913 <br /> </td> 
          <td class="text-center"> - </td> 
         </tr> 
        </tbody>
       </table> 
       <div> 
       </div> 
      </section> 
      <section class="panel b-a clear guquan-section" id="guquan"> 
       <div class="tcaption"> 
        <h3 class="title">股权穿透图</h3> 
        <span class="watermark"></span> 
       </div> 
       <table class="ntable"> 
        <tbody>
         <tr> 
          <th style="text-align: left;position: relative;"> 上海盒马网络科技有限公司 
           <div id="guquanIframeTool" class="guquan-tool" style="display: block;"> 
            <a href="/company_guquan?keyNo=e45ee37279ffb3f2ce9bbbcfa39d8133&amp;name=%E4%B8%8A%E6%B5%B7%E7%9B%92%E9%A9%AC%E7%BD%91%E7%BB%9C%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8" onclick="zhugeTrack('企业主页-基本信息-股权穿透图内嵌-全屏查看',{'企业名称':''})" target="_blank"><span class="screen">&nbsp;</span><span>全屏查看</span></a> 
            <a class="m-l" onclick="$('#guquanIframe')[0].contentWindow.saveImg();zhugeTrack('企业主页-基本信息-股权穿透图内嵌-下载图片',{'企业名称':''})"><span class="save">&nbsp;</span><span>下载图谱</span></a> 
           </div> </th> 
         </tr> 
         <tr> 
          <td style="padding: 0px;"> <iframe id="guquanIframe" scrolling="no" src="company_guquan?keyNo=e45ee37279ffb3f2ce9bbbcfa39d8133&amp;iframe=1" frameborder="0"></iframe> </td> 
         </tr> 
        </tbody>
       </table> 
      </section> 
      <section class="panel b-a" id="touzilist"> 
       <div class="tcaption"> 
        <span class="title"> 对外投资</span> 
        <span class="tbadge">2</span> 
        <div class="chooseBase" data-box="touzi" style="float: right"> 
         <div class="tdrop"> 
          <span class="btn" data-toggle="dropdown"> <span class="touzistatus">全部状态</span> <span class="caret m-l"></span> </span> 
          <ul class="dropdown-menu dropdown-menu-right"> 
           <li><a href="javascript:;" data-option="status" data-value="">不限</a></li> 
           <li><a href="javascript:;" data-option="status" data-value="存续">存续(2)</a></li> 
          </ul> 
         </div> 
        </div> 
        <span class="watermark"></span> 
       </div> 
       <table class="ntable ntable-odd"> 
        <tbody> 
         <tr> 
          <th class="">被投资企业名称</th> 
          <th class="">被投资法定代表人</th> 
          <th class="">注册资本</th> 
          <th class="">出资比例</th> 
          <th class="">成立日期</th> 
          <th class="">状态</th> 
         </tr> 
         <tr> 
          <td width="30%"> <span class="headimg"> <img src="https://qccdata.qichacha.com/AutoImage/fc045a13d86149f7aaa5966adc6979f9.jpg?x-oss-process=image/resize,w_120" /> </span> 
           <div class="whead-text"> 
            <a href="/firm_fc045a13d86149f7aaa5966adc6979f9.html" target="_blank"><h3 class="seo font-14">上海涓牛电子商务有限公司</h3></a> 
           </div> </td> 
          <td> 
           <table class="insert-table"> 
            <tbody>
             <tr> 
              <td> <a href="/pl_pr0c48da0410bfe8770867b9cb924376.html"><h3 class="seo font-14">胡秋根</h3></a> </td> 
              <td width="130" class="text-right"> <a class="btn-touzi" href="/pl_pr0c48da0410bfe8770867b9cb924376.html">他关联3家公司 &gt; </a> </td> 
             </tr> 
            </tbody>
           </table> </td> 
          <td width="120" class="text-center"> 100万元人民币 </td> 
          <td width="94" class="text-center"> 100% </td> 
          <td width="104" class="text-center"> 2018-09-20 </td> 
          <td width="58" class="text-center"><span class="text-success">存续</span></td> 
         </tr> 
         <tr> 
          <td width="30%"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/5e268f8c7d81e05111ca533013056813.jpg?x-oss-process=style/qcc_cmp" /> </span> 
           <div class="whead-text"> 
            <a href="/firm_5e268f8c7d81e05111ca533013056813.html" target="_blank"><h3 class="seo font-14">深圳盒马鲜生物流有限公司</h3></a> 
           </div> </td> 
          <td> 
           <table class="insert-table"> 
            <tbody>
             <tr> 
              <td> <a href="/pl_p73ac1d107d8235907d5087e3b3abe6b.html"><h3 class="seo font-14">侯毅</h3></a> </td> 
              <td width="130" class="text-right"> <a class="btn-touzi" href="/pl_p73ac1d107d8235907d5087e3b3abe6b.html">他关联28家公司 &gt; </a> </td> 
             </tr> 
            </tbody>
           </table> </td> 
          <td width="120" class="text-center"> 500万元人民币 </td> 
          <td width="94" class="text-center"> 100% </td> 
          <td width="104" class="text-center"> 2017-08-16 </td> 
          <td width="58" class="text-center"><span class="text-success">存续</span></td> 
         </tr> 
        </tbody> 
       </table> 
       <div> 
       </div> 
       <script type="text/javascript">
        var optionArr = ['touzistatus'];
        var descArr = ['全部状态'];
        var hiddenName = '';
        var hiddenValue = '';
        var hiddenDesc = '';
        for(var i=0;i<optionArr.length;i++){
            hiddenName = optionArr[i];
            hiddenValue = $("input[name=" + hiddenName + "]").val();
            hiddenDesc = $("input[name=" + hiddenName + "]").attr('data-desc');
            var text = '.' + hiddenName;
            if(hiddenValue != '' && hiddenValue != '0'){
                $(text).text(hiddenDesc);
            }else{
                $(text).text(descArr[i]);
            }
        }
        $(function () {
            $('#touzilist .chooseBase').find('a').on('click',function(){
                var targetDiv = $(this).parent().parent().parent().parent();
                var target = targetDiv.attr('data-box');
                var optionArr = [];
                var hiddenName = '';
                var hiddenValue = '';
                var ajaxData = {};
                switch(target){
                    case 'touzi':
                        optionArr = ['touzistatus'];
                        ajaxData['box'] = 'touzi';
                        break;
                    default :
                        break;
                }
                var option = $(this).attr('data-option');
                option = target + option;
                var value = $(this).attr('data-value');
                var text = $(this).text();
                var textArr = text.split('(');
                $("input[name=" + option + "]").val(value);
                $("input[name=" + option + "]").attr('data-desc',textArr[0]);
                //取所有筛选条件的值
                for(var i=0;i<optionArr.length;i++){
                    hiddenName = optionArr[i];
                    hiddenValue = $("input[name=" + hiddenName + "]").val();
                    ajaxData[hiddenName] = hiddenValue;
                }
                //拼接其他参数
                ajaxData['unique'] = $("#unique").val();
                ajaxData['companyname'] = $("#companyname").val();
                ajaxData['tab'] = 'base';
                ajaxData['p'] = '1';
                getTabListNew(ajaxData);
            });
        });
    </script> 
      </section> 
      <div style="position: absolute;width: 50px;opacity: 0;margin-top: -50px;" id="syrlistpos">
       &nbsp;
      </div> 
      <section class="panel b-a" id="syrlist"> 
       <div class="tcaption"> 
        <h3 class="title">最终受益人</h3> 
        <span class="tbadge">2</span> 
        <a data-trigger="hover" data-html="true" data-toggle="tooltip" data-placement="bottom" data-delay="500" title="" data-original-title="公司的受益所有人为直接或间接拥有疑似超过25%公司股权的自然人或企业。仅供用户参考，该成果并不代表企查查的任何明示、暗示之观点或保证。"><i class="m_question"></i></a> 
        <span class="watermark"></span> 
        <span class="ntag vip m-l-sm" data-trigger="hover" data-html="true" data-toggle="tooltip" data-placement="bottom" data-delay="500" title="" data-original-title="尊敬的会员，您正在使用高级特权">功能</span> 
       </div> 
       <table class="ntable ntable-odd"> 
        <tbody>
         <tr> 
          <th class="tx">序号</th> 
          <th width="280">最终受益人名称</th> 
          <th width="85">持股比例</th> 
          <th class="">股权链</th> 
         </tr> 
         <tr> 
          <td class="tx">1</td> 
          <td> <span class="headimg"> <img src="https://co-image.qichacha.com/PersonImage/p73ac1d107d8235907d5087e3b3abe6b.jpg" /> </span> 
           <div class="whead-text"> 
            <a href="/pl_p73ac1d107d8235907d5087e3b3abe6b.html">侯毅</a> 
            <a class="btn-touzi" href="/pl_p73ac1d107d8235907d5087e3b3abe6b.html">他关联28家公司 &gt; </a> 
           </div> </td> 
          <td class="text-center"> - </td> 
          <td> 
           <div class="tdpath" style="margin-bottom: 0px"> 
            <div>
             决定路径
            </div> 
            <a href="/pl_p73ac1d107d8235907d5087e3b3abe6b.html">侯毅</a> 
            <span>法定代表人</span> 
            <a href="/firm_e45ee37279ffb3f2ce9bbbcfa39d8133.html">上海盒马网络科技有限公司</a> 
           </div> 
           <div class="syrtips">
            注：未识别出股比&gt;25%的自然人，因此决定以最终法定代表人作为受益所有人结果
           </div> </td> 
         </tr> 
         <tr> 
          <td class="tx">2</td> 
          <td> <span class="headimg"> <img src="https://qccdata.qichacha.com/AutoImage/hcb57b19bc9cd13855cfb774959b8730.jpg?x-oss-process=image/resize,w_120" /> </span> 
           <div class="whead-text"> 
            <a href="/firm_hcb57b19bc9cd13855cfb774959b8730.html">Hema (Hong Kong) Limited</a> 
           </div> </td> 
          <td class="text-center"> 100% </td> 
          <td> 
           <div class="tdpath"> 
            <div>
             股权路径 1（占比约 100%）
            </div> 
            <a href="/firm_hcb57b19bc9cd13855cfb774959b8730.html">Hema (Hong Kong) Limited</a> 
            <span>100%</span> 
            <a href="/firm_e45ee37279ffb3f2ce9bbbcfa39d8133.html">上海盒马网络科技有限公司</a> 
           </div> </td> 
         </tr> 
        </tbody>
       </table> 
      </section> 
      <section class="panel b-a clear guquan-section" id="kzrtupu"> 
       <div class="tcaption"> 
        <h3 class="title">实际控制人</h3> 
        <span class="watermark"></span> 
        <span class="ntag vip m-l-sm" data-trigger="hover" data-html="true" data-toggle="tooltip" data-placement="bottom" data-delay="500" title="" data-original-title="尊敬的会员，您正在使用高级特权">功能</span> 
       </div> 
       <table class="ntable"> 
        <tbody>
         <tr> 
          <th style="text-align: left;position: relative;"> 上海盒马网络科技有限公司 
           <div id="kzrIframeTool" class="guquan-tool" style="display: block;"> 
            <a href="/company_kzr?keyNo=e45ee37279ffb3f2ce9bbbcfa39d8133&amp;name=%E4%B8%8A%E6%B5%B7%E7%9B%92%E9%A9%AC%E7%BD%91%E7%BB%9C%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8" onclick="zhugeTrack('企业主页-基本信息-实际控制人内嵌-全屏查看',{'企业名称':''})" target="_blank"><span class="screen">&nbsp;</span><span>全屏查看</span></a> 
            <a class="m-l" onclick="$('#kzrIframe')[0].contentWindow.saveImg();zhugeTrack('企业主页-基本信息-实际控制人内嵌-下载图片',{'企业名称':''})"><span class="save">&nbsp;</span><span>下载图谱</span></a> 
           </div> </th> 
         </tr> 
         <tr> 
          <td style="padding: 0px;"> <iframe id="kzrIframe" scrolling="no" src="company_kzr?keyNo=e45ee37279ffb3f2ce9bbbcfa39d8133&amp;name=上海盒马网络科技有限公司&amp;iframe=1" frameborder="0"></iframe> </td> 
         </tr> 
        </tbody>
       </table> 
      </section> 
      <div style="position: absolute;width: 50px;opacity: 0;margin-top: -50px;" id="holdcolistpos">
       &nbsp;
      </div> 
      <section class="panel b-a" id="holdcolist"> 
       <div class="tcaption"> 
        <h3 class="title">控股企业</h3> 
        <span class="tbadge">2</span> 
        <a data-trigger="hover" data-html="true" data-toggle="tooltip" data-placement="bottom" data-delay="500" title="" data-original-title="控股企业为公司或自然人直接或间接拥有其疑似实际控制权的企业。仅供用户参考，该成果并不代表企查查的任何明示、暗示之观点或保证。(最多显示300家控股企业)"><i class="m_question"></i></a> 
        <span class="watermark"></span> 
        <span class="ntag vip m-l-sm" data-trigger="hover" data-html="true" data-toggle="tooltip" data-placement="bottom" data-delay="500" title="" data-original-title="尊敬的会员，您正在使用高级特权">功能</span> 
       </div> 
       <table class="ntable ntable-odd"> 
        <tbody>
         <tr> 
          <th class="tx">序号</th> 
          <th width="280">控股企业名称</th> 
          <th width="90">投资比例</th> 
          <th class="">投资链</th> 
         </tr> 
         <tr> 
          <td class="tx">1</td> 
          <td> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/5e268f8c7d81e05111ca533013056813.jpg?x-oss-process=image/resize,w_160" /> </span> 
           <div class="whead-text"> 
            <a href="/firm_5e268f8c7d81e05111ca533013056813.html">深圳盒马鲜生物流有限公司</a> 
           </div> </td> 
          <td class="text-center">100%</td> 
          <td> 
           <div class="tdpath"> 
            <div>
             路径 1（占比约 100%）
            </div> 
            <a href="/firm_e45ee37279ffb3f2ce9bbbcfa39d8133.html">上海盒马网络科技有限公司</a> 
            <span>100%</span> 
            <a href="/firm_5e268f8c7d81e05111ca533013056813.html">深圳盒马鲜生物流有限公司</a> 
           </div> </td> 
         </tr> 
         <tr> 
          <td class="tx">2</td> 
          <td> <span class="headimg"> <img src="https://qccdata.qichacha.com/AutoImage/fc045a13d86149f7aaa5966adc6979f9.jpg?x-oss-process=image/resize,w_120" /> </span> 
           <div class="whead-text"> 
            <a href="/firm_fc045a13d86149f7aaa5966adc6979f9.html">上海涓牛电子商务有限公司</a> 
           </div> </td> 
          <td class="text-center">100%</td> 
          <td> 
           <div class="tdpath"> 
            <div>
             路径 1（占比约 100%）
            </div> 
            <a href="/firm_e45ee37279ffb3f2ce9bbbcfa39d8133.html">上海盒马网络科技有限公司</a> 
            <span>100%</span> 
            <a href="/firm_fc045a13d86149f7aaa5966adc6979f9.html">上海涓牛电子商务有限公司</a> 
           </div> </td> 
         </tr> 
        </tbody>
       </table> 
       <div> 
       </div> 
       <script type="text/javascript">
    
    $('[data-toggle="tooltip"]').tooltip();
    
</script> 
      </section> 
      <section class="panel b-a clear" id="Mainmember"> 
       <div class="tcaption"> 
        <h3 class="title">主要人员</h3> 
        <span class="tbadge">4</span> 
        <span class="watermark"></span> 
       </div> 
       <table class="ntable ntable-odd"> 
        <tbody>
         <tr> 
          <th class=""> 序号</th> 
          <th class=""> 姓名</th> 
          <th class="">职务</th> 
         </tr> 
         <tr> 
          <td class="tx">1</td> 
          <td width="50%"> <span class="headimg"> <img src="https://co-image.qichacha.com/PersonImage/pa14da0de0e32e960da96e985c4f5e5e.jpg" /> </span> 
           <div class="whead-text" style="width: 365px;"> 
            <a href="/pl_pa14da0de0e32e960da96e985c4f5e5e.html" class="c_a" title="徐殿勇"><h3 class="seo font-14">徐殿勇</h3></a> 
            <a class="btn-touzi pull-right" href="/pl_pa14da0de0e32e960da96e985c4f5e5e.html">他关联 11 家公司 &gt; </a> 
           </div> </td> 
          <td class="text-center"> 董事 </td> 
         </tr> 
         <tr> 
          <td class="tx">2</td> 
          <td width="50%"> <span class="usericon headn color-8" first-letter="冯"></span> 
           <div class="whead-text" style="width: 365px;"> 
            <a href="/pl_pd569a04b441a1ad875c43e236d98a8a.html" class="c_a" title="冯云乐"><h3 class="seo font-14">冯云乐</h3></a> 
            <a class="btn-touzi pull-right" href="/pl_pd569a04b441a1ad875c43e236d98a8a.html">他关联 105 家公司 &gt; </a> 
           </div> </td> 
          <td class="text-center"> 监事 </td> 
         </tr> 
         <tr> 
          <td class="tx">3</td> 
          <td width="50%"> <span class="headimg"> <img src="https://co-image.qichacha.com/PersonImage/p580cd17d9f541702a808e95feee7bc6.jpg" /> </span> 
           <div class="whead-text" style="width: 365px;"> 
            <a href="/pl_p580cd17d9f541702a808e95feee7bc6.html" class="c_a" title="俞思瑛"><h3 class="seo font-14">俞思瑛</h3></a> 
            <a class="btn-touzi pull-right" href="/pl_p580cd17d9f541702a808e95feee7bc6.html">他关联 39 家公司 &gt; </a> 
           </div> </td> 
          <td class="text-center"> 董事 </td> 
         </tr> 
         <tr> 
          <td class="tx">4</td> 
          <td width="50%"> <span class="headimg"> <img src="https://co-image.qichacha.com/PersonImage/p73ac1d107d8235907d5087e3b3abe6b.jpg" /> </span> 
           <div class="whead-text" style="width: 365px;"> 
            <a href="/pl_p73ac1d107d8235907d5087e3b3abe6b.html" class="c_a" title="侯毅"><h3 class="seo font-14">侯毅</h3></a> 
            <a class="btn-touzi pull-right" href="/pl_p73ac1d107d8235907d5087e3b3abe6b.html">他关联 28 家公司 &gt; </a> 
           </div> </td> 
          <td class="text-center"> 董事长兼总经理 </td> 
         </tr> 
        </tbody>
       </table> 
      </section> 
      <section class="panel b-a clear" id="Subcom"> 
       <div class="tcaption"> 
        <h3 class="title">分支机构</h3> 
        <span class="tbadge">72</span> 
        <span class="watermark"></span> 
       </div> 
       <table class="ntable"> 
        <tbody>
         <tr> 
          <td class="tx tb"> 1 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/00adf3b000850b6e3a8383690d65e4ca.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_00adf3b000850b6e3a8383690d65e4ca"><span>上海盒马网络科技有限公司长宁第二分公司</span></a> 
           </div> </td> 
          <td class="tx tb"> 2 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/00ec38d51ad482b99ca5c77531534abc.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_00ec38d51ad482b99ca5c77531534abc"><span>上海盒马网络科技有限公司杨浦第三分公司</span></a> 
           </div> </td> 
         </tr> 
         <tr> 
          <td class="tx tb"> 3 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/01bef5b5d31c3311dd4dfe8c70bb572e.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_01bef5b5d31c3311dd4dfe8c70bb572e"><span>上海盒马网络科技有限公司苏州高新分公司</span></a> 
           </div> </td> 
          <td class="tx tb"> 4 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/026b23ef46dd64ce5451f215fb2d2f1e.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_026b23ef46dd64ce5451f215fb2d2f1e"><span>上海盒马网络科技有限公司浦东第五分公司</span></a> 
           </div> </td> 
         </tr> 
         <tr> 
          <td class="tx tb"> 5 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/0616d4bffd1d73f34824337a13197b8c.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_0616d4bffd1d73f34824337a13197b8c"><span>上海盒马网络科技有限公司杭州分公司</span></a> 
           </div> </td> 
          <td class="tx tb"> 6 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/13c877376e2f30b579a8d61b4fb3c7d0.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_13c877376e2f30b579a8d61b4fb3c7d0"><span>上海盒马网络科技有限公司黄浦第二分公司</span></a> 
           </div> </td> 
         </tr> 
         <tr> 
          <td class="tx tb"> 7 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/1baa208c8e26303ffdf796b50ac2ee01.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_1baa208c8e26303ffdf796b50ac2ee01"><span>上海盒马网络科技有限公司徐汇第三分公司</span></a> 
           </div> </td> 
          <td class="tx tb"> 8 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/1c8cbf5904bd7227366df06e22ed6c80.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_1c8cbf5904bd7227366df06e22ed6c80"><span>上海盒马网络科技有限公司杨浦分公司</span></a> 
           </div> </td> 
         </tr> 
         <tr> 
          <td class="tx tb"> 9 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/2621a5b6045214e199be94f503f361a5.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_2621a5b6045214e199be94f503f361a5"><span>上海盒马网络科技有限公司无锡第一分公司</span></a> 
           </div> </td> 
          <td class="tx tb"> 10 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/26f3ef460fa292d210529039f73939cd.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_26f3ef460fa292d210529039f73939cd"><span>上海盒马网络科技有限公司徐汇第四分公司</span></a> 
           </div> </td> 
         </tr> 
         <tr> 
          <td class="tx tb"> 11 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/3048508c3b72fe26f669975cc5f608c4.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_3048508c3b72fe26f669975cc5f608c4"><span>上海盒马网络科技有限公司昆明第二分公司</span></a> 
           </div> </td> 
          <td class="tx tb"> 12 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/31e3eacbbc9e02c39f3a50da224c42d6.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_31e3eacbbc9e02c39f3a50da224c42d6"><span>上海盒马网络科技有限公司南京第三分公司</span></a> 
           </div> </td> 
         </tr> 
         <tr> 
          <td class="tx tb"> 13 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/33f21276e30f462049f0a7106f99b900.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_33f21276e30f462049f0a7106f99b900"><span>上海盒马网络科技有限公司青岛第一分公司</span></a> 
           </div> </td> 
          <td class="tx tb"> 14 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/364fe514cab6b374df955f6d7d9ca251.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_364fe514cab6b374df955f6d7d9ca251"><span>上海盒马网络科技有限公司黄浦第二分公司</span></a> 
           </div> </td> 
         </tr> 
         <tr> 
          <td class="tx tb"> 15 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/36813c1a78d09f23e727d39cc1b17d89.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_36813c1a78d09f23e727d39cc1b17d89"><span>上海盒马网络科技有限公司南通第三分公司</span></a> 
           </div> </td> 
          <td class="tx tb"> 16 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/38fc22d05d3a773276ec844a015b8f03.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_38fc22d05d3a773276ec844a015b8f03"><span>上海盒马网络科技有限公司新大陆广场分公司</span></a> 
           </div> </td> 
         </tr> 
         <tr> 
          <td class="tx tb"> 17 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/39515020b3567cb653ef5b27bce82444.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_39515020b3567cb653ef5b27bce82444"><span>上海盒马网络科技有限公司杭州萧山分公司</span></a> 
           </div> </td> 
          <td class="tx tb"> 18 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/39b9eb265d0d05199de4f6a21f873821.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_39b9eb265d0d05199de4f6a21f873821"><span>上海盒马网络科技有限公司黄浦分公司</span></a> 
           </div> </td> 
         </tr> 
         <tr> 
          <td class="tx tb"> 19 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/3d8a34ddab65286d41d278981142023f.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_3d8a34ddab65286d41d278981142023f"><span>上海盒马网络科技有限公司武汉第一分公司</span></a> 
           </div> </td> 
          <td class="tx tb"> 20 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/4191d20c0948969dc0d433deaf615010.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_4191d20c0948969dc0d433deaf615010"><span>上海盒马网络科技有限公司普陀第二分公司</span></a> 
           </div> </td> 
         </tr> 
         <tr> 
          <td class="tx tb"> 21 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/4473580cfe6a0c4ee88cba09559e19d8.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_4473580cfe6a0c4ee88cba09559e19d8"><span>上海盒马网络科技有限公司成都温江德昆分公司</span></a> 
           </div> </td> 
          <td class="tx tb"> 22 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/448744dbbdedc53051d71896b10eff10.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_448744dbbdedc53051d71896b10eff10"><span>上海盒马网络科技有限公司成都莱蒙分公司</span></a> 
           </div> </td> 
         </tr> 
         <tr> 
          <td class="tx tb"> 23 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/4b212cae4c8a2c995f64611f7504398b.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_4b212cae4c8a2c995f64611f7504398b"><span>上海盒马网络科技有限公司虹口第二分公司</span></a> 
           </div> </td> 
          <td class="tx tb"> 24 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/51f908e6f64a380a5eca344e05cc1aef.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_51f908e6f64a380a5eca344e05cc1aef"><span>上海盒马网络科技有限公司西安曲江银泰分公司</span></a> 
           </div> </td> 
         </tr> 
         <tr> 
          <td class="tx tb"> 25 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/521712712a7d1c58261dfaa00b53a5e0.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_521712712a7d1c58261dfaa00b53a5e0"><span>上海盒马网络科技有限公司虹口第三分公司</span></a> 
           </div> </td> 
          <td class="tx tb"> 26 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/54b2b9e968d5c36a331dbbc129bc2ede.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_54b2b9e968d5c36a331dbbc129bc2ede"><span>上海盒马网络科技有限公司徐汇第二分公司</span></a> 
           </div> </td> 
         </tr> 
         <tr> 
          <td class="tx tb"> 27 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/558514176f576ece73a36969951aeee8.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_558514176f576ece73a36969951aeee8"><span>上海盒马网络科技有限公司长宁第一分公司</span></a> 
           </div> </td> 
          <td class="tx tb"> 28 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/5aa06dc2c767981996beafef98f41798.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_5aa06dc2c767981996beafef98f41798"><span>上海盒马网络科技有限公司静安第二分公司</span></a> 
           </div> </td> 
         </tr> 
         <tr> 
          <td class="tx tb"> 29 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/5b9d74c44ec7ce1260ff8bd645216ba9.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_5b9d74c44ec7ce1260ff8bd645216ba9"><span>上海盒马网络科技有限公司普陀第一分公司</span></a> 
           </div> </td> 
          <td class="tx tb"> 30 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/5e9b1b2e7e981f335af9eab67f264b8f.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_5e9b1b2e7e981f335af9eab67f264b8f"><span>上海盒马网络科技有限公司杭州滨江分公司</span></a> 
           </div> </td> 
         </tr> 
         <tr> 
          <td class="tx tb"> 31 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/64965311942bfbd7e6672f3cfebf426c.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_64965311942bfbd7e6672f3cfebf426c"><span>上海盒马网络科技有限公司昆山第一分公司</span></a> 
           </div> </td> 
          <td class="tx tb"> 32 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/6836e233b5019a72b71efeaacc63587b.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_6836e233b5019a72b71efeaacc63587b"><span>上海盒马网络科技有限公司昆明第一分公司</span></a> 
           </div> </td> 
         </tr> 
         <tr> 
          <td class="tx tb"> 33 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/6a79947e3b32095b273ab79c43206bdc.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_6a79947e3b32095b273ab79c43206bdc"><span>上海盒马网络科技有限公司闵行分公司</span></a> 
           </div> </td> 
          <td class="tx tb"> 34 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/6eb28f5216e5e02d222dc627ff7856f1.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_6eb28f5216e5e02d222dc627ff7856f1"><span>上海盒马网络科技有限公司南京第四分公司</span></a> 
           </div> </td> 
         </tr> 
         <tr> 
          <td class="tx tb"> 35 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/7830611d23fca85f095cba163ef13cbb.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_7830611d23fca85f095cba163ef13cbb"><span>上海盒马网络科技有限公司苏州吴中分公司</span></a> 
           </div> </td> 
          <td class="tx tb"> 36 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/7fbbdd821a551fc5883eafbf89a18476.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_7fbbdd821a551fc5883eafbf89a18476"><span>上海盒马网络科技有限公司南京第一分公司</span></a> 
           </div> </td> 
         </tr> 
         <tr> 
          <td class="tx tb"> 37 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/80170824df2e4b9d9203c993151be13c.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_80170824df2e4b9d9203c993151be13c"><span>上海盒马网络科技有限公司嘉定第一分公司</span></a> 
           </div> </td> 
          <td class="tx tb"> 38 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/955c51b34ab499b442b7bbddac9c4da2.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_955c51b34ab499b442b7bbddac9c4da2"><span>上海盒马网络科技有限公司闵行第三分公司</span></a> 
           </div> </td> 
         </tr> 
         <tr> 
          <td class="tx tb"> 39 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/970035d5d5d52554b5d52eb37d62a461.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_970035d5d5d52554b5d52eb37d62a461"><span>上海盒马网络科技有限公司浦东第七分公司</span></a> 
           </div> </td> 
          <td class="tx tb"> 40 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/9b56f310bc7147bccd06b808c3ef64ed.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_9b56f310bc7147bccd06b808c3ef64ed"><span>上海盒马网络科技有限公司南通第二分公司</span></a> 
           </div> </td> 
         </tr> 
         <tr> 
          <td class="tx tb"> 41 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/9b9789f9e5fdf9b7ba425eb7d5daa619.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_9b9789f9e5fdf9b7ba425eb7d5daa619"><span>上海盒马网络科技有限公司南通第一分公司</span></a> 
           </div> </td> 
          <td class="tx tb"> 42 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/a190468c33eb3d158bcfd472490437ae.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_a190468c33eb3d158bcfd472490437ae"><span>上海盒马网络科技有限公司苏州工业园区分公司</span></a> 
           </div> </td> 
         </tr> 
         <tr> 
          <td class="tx tb"> 43 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/ad389950d80c931b770cff956a0aa9dc.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_ad389950d80c931b770cff956a0aa9dc"><span>上海盒马网络科技有限公司浦东第三分公司</span></a> 
           </div> </td> 
          <td class="tx tb"> 44 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/b1577d7a76f1f671ff1a39ebe80a0564.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_b1577d7a76f1f671ff1a39ebe80a0564"><span>上海盒马网络科技有限公司青浦第一分公司</span></a> 
           </div> </td> 
         </tr> 
         <tr> 
          <td class="tx tb"> 45 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/b2f31ba4a94a71b880cfd1e7024ee3e9.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_b2f31ba4a94a71b880cfd1e7024ee3e9"><span>上海盒马网络科技有限公司嘉定第二分公司</span></a> 
           </div> </td> 
          <td class="tx tb"> 46 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/bdd2d6636ef94bdd7b81a199bd852cc3.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_bdd2d6636ef94bdd7b81a199bd852cc3"><span>上海盒马网络科技有限公司徐汇分公司</span></a> 
           </div> </td> 
         </tr> 
         <tr> 
          <td class="tx tb"> 47 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/c2a70d00ea59c7da0090809650795306.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_c2a70d00ea59c7da0090809650795306"><span>上海盒马网络科技有限公司黄浦第一分公司</span></a> 
           </div> </td> 
          <td class="tx tb"> 48 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/c3afcfd32f7823e4287b9904ebe247ab.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_c3afcfd32f7823e4287b9904ebe247ab"><span>上海盒马网络科技有限公司浦东第六分公司</span></a> 
           </div> </td> 
         </tr> 
         <tr> 
          <td class="tx tb"> 49 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/c6c58b0363d7fcac0d6ce37138002676.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_c6c58b0363d7fcac0d6ce37138002676"><span>上海盒马网络科技有限公司松江第一分公司</span></a> 
           </div> </td> 
          <td class="tx tb"> 50 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/c7d8a690fc19fe182d8f4ccb19dde171.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_c7d8a690fc19fe182d8f4ccb19dde171"><span>上海盒马网络科技有限公司静安第三分公司</span></a> 
           </div> </td> 
         </tr> 
         <tr> 
          <td class="tx tb"> 51 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/c8f2ea8cb5fcd91f31814bae4d7a9aff.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_c8f2ea8cb5fcd91f31814bae4d7a9aff"><span>上海盒马网络科技有限公司虹口第一分公司</span></a> 
           </div> </td> 
          <td class="tx tb"> 52 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/c92ae48693f9ddc8797405e2366a4b8f.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_c92ae48693f9ddc8797405e2366a4b8f"><span>上海盒马网络科技有限公司闵行莘北路分公司</span></a> 
           </div> </td> 
         </tr> 
         <tr> 
          <td class="tx tb"> 53 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/ca325d9322807eab0a3a95a861e5f5c7.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_ca325d9322807eab0a3a95a861e5f5c7"><span>上海盒马网络科技有限公司南京第二分公司</span></a> 
           </div> </td> 
          <td class="tx tb"> 54 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/caaa42d016129e4453c4c47746e1e9a5.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_caaa42d016129e4453c4c47746e1e9a5"><span>上海盒马网络科技有限公司徐汇第一分公司</span></a> 
           </div> </td> 
         </tr> 
         <tr> 
          <td class="tx tb"> 55 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/ceb1d54ecadde3837c56aff1d11f135c.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_ceb1d54ecadde3837c56aff1d11f135c"><span>上海翌恒网络科技有限公司静安分公司</span></a> 
           </div> </td> 
          <td class="tx tb"> 56 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/cf42c08e0e7d9e4b1633e8a66606065b.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_cf42c08e0e7d9e4b1633e8a66606065b"><span>上海盒马网络科技有限公司宝山第二分公司</span></a> 
           </div> </td> 
         </tr> 
         <tr> 
          <td class="tx tb"> 57 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/d3802143dc6dbfe4c79e57ac4ae48fd9.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_d3802143dc6dbfe4c79e57ac4ae48fd9"><span>上海盒马网络科技有限公司杨浦第四分公司</span></a> 
           </div> </td> 
          <td class="tx tb"> 58 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/d38ba458983e28c37843ffbc2097533f.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_d38ba458983e28c37843ffbc2097533f"><span>上海盒马网络科技有限公司浦东第八分公司</span></a> 
           </div> </td> 
         </tr> 
         <tr> 
          <td class="tx tb"> 59 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/d55c70f966339320812fc9e5a3da0162.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_d55c70f966339320812fc9e5a3da0162"><span>上海盒马网络科技有限公司长宁分公司</span></a> 
           </div> </td> 
          <td class="tx tb"> 60 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/d5c6a9d2b743133ec5abdf780548ccea.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_d5c6a9d2b743133ec5abdf780548ccea"><span>上海盒马网络科技有限公司成都青羊西村分公司</span></a> 
           </div> </td> 
         </tr> 
         <tr> 
          <td class="tx tb"> 61 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/d7129702118593bcfb7f916b5756715c.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_d7129702118593bcfb7f916b5756715c"><span>上海盒马网络科技有限公司浦东第一分公司</span></a> 
           </div> </td> 
          <td class="tx tb"> 62 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/e05ab44aac22153ee4288afe969c0969.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_e05ab44aac22153ee4288afe969c0969"><span>上海盒马网络科技有限公司普陀分公司</span></a> 
           </div> </td> 
         </tr> 
         <tr> 
          <td class="tx tb"> 63 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/e196a07106101316320bf7c3ad522ce7.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_e196a07106101316320bf7c3ad522ce7"><span>上海盒马网络科技有限公司长沙第一分公司</span></a> 
           </div> </td> 
          <td class="tx tb"> 64 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/e33a0a8547e091c103515a8d85422408.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_e33a0a8547e091c103515a8d85422408"><span>上海盒马网络科技有限公司相第一分公司</span></a> 
           </div> </td> 
         </tr> 
         <tr> 
          <td class="tx tb"> 65 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/e9a38c021bb9a59444a7976e484a6538.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_e9a38c021bb9a59444a7976e484a6538"><span>上海盒马网络科技有限公司青岛第二分公司</span></a> 
           </div> </td> 
          <td class="tx tb"> 66 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/eccd9d05e7a498e35d831a2ff551de83.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_eccd9d05e7a498e35d831a2ff551de83"><span>上海盒马网络科技有限公司苏州昆山分公司</span></a> 
           </div> </td> 
         </tr> 
         <tr> 
          <td class="tx tb"> 67 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/f07cd52b73837721a6f2ba2a238b6f19.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_f07cd52b73837721a6f2ba2a238b6f19"><span>上海盒马网络科技有限公司浦东第四分公司</span></a> 
           </div> </td> 
          <td class="tx tb"> 68 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/f2c7056ea6ee51b6ee59252f05a3cd7a.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_f2c7056ea6ee51b6ee59252f05a3cd7a"><span>上海盒马网络科技有限公司宝山第一分公司</span></a> 
           </div> </td> 
         </tr> 
         <tr> 
          <td class="tx tb"> 69 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/f3f74daf9cb44794a6ec28b7d51fbea3.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_f3f74daf9cb44794a6ec28b7d51fbea3"><span>上海盒马网络科技有限公司浦东第二分公司</span></a> 
           </div> </td> 
          <td class="tx tb"> 70 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/f5ed9b9b5d01ded08b664f0dd65ba6d8.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_f5ed9b9b5d01ded08b664f0dd65ba6d8"><span>上海盒马网络科技有限公司闵行第一分公司</span></a> 
           </div> </td> 
         </tr> 
         <tr> 
          <td class="tx tb"> 71 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/f8fe38c5e8e54aa6a9ebd43d6ccbf68d.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_f8fe38c5e8e54aa6a9ebd43d6ccbf68d"><span>上海盒马网络科技有限公司闵行第二分公司</span></a> 
           </div> </td> 
          <td class="tx tb"> 72 </td> 
          <td width="375"> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/fcbf9e8789874bd695a4883aebfc37c7.jpg" /> </span> 
           <div class="whead-text"> 
            <a class="c_a" target="_blank" href="/firm_fcbf9e8789874bd695a4883aebfc37c7"><span>上海盒马网络科技有限公司西安太白分公司</span></a> 
           </div> </td> 
         </tr> 
        </tbody>
       </table> 
      </section> 
      <section class="panel b-a clear guquan-section" id="muhou"> 
       <div class="tcaption"> 
        <h3 class="title">企业关联图谱</h3> 
        <span class="watermark"></span> 
       </div> 
       <table class="ntable"> 
        <tbody>
         <tr> 
          <th style="text-align: left;position: relative;"> 上海盒马网络科技有限公司 
           <div id="muhouIframeTool" class="guquan-tool"> 
            <a href="/company_muhou3?keyNo=e45ee37279ffb3f2ce9bbbcfa39d8133&amp;name=%E4%B8%8A%E6%B5%B7%E7%9B%92%E9%A9%AC%E7%BD%91%E7%BB%9C%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8" onclick="zhugeTrack('企业主页-基本信息-企业关联图谱-全屏查看',{'企业名称':'上海盒马网络科技有限公司'})" target="_blank"><span class="screen">&nbsp;</span><span>全屏查看</span></a> 
            <a id="muhouDownload" class="m-l" onclick="$('#muhouIframe')[0].contentWindow.saveImg(this);zhugeTrack('企业主页-基本信息-企业关联图谱-下载图片',{'企业名称':'上海盒马网络科技有限公司'})"><span class="save">&nbsp;</span><span id="DownImgTip">下载图谱</span></a> 
           </div> </th> 
         </tr> 
         <tr> 
          <td style="padding: 0px;"> <iframe id="muhouIframe" scrolling="no" data-src="company_muhouinsertqiye?keyNo=e45ee37279ffb3f2ce9bbbcfa39d8133&amp;iframe=1" src="" frameborder="0"></iframe> </td> 
         </tr> 
        </tbody>
       </table> 
       <script type="text/javascript">
        var isIE = (!!window.ActiveXObject || "ActiveXObject" in window);
        if(isIE){
            $('#guquanDownload').hide();
        }
    </script> 
      </section> 
      <div style="position: absolute;width: 50px;opacity: 0;margin-top: -50px;" id="cwjxtpos">
       &nbsp;
      </div> 
      <section class="panel b-a clear" id="cwjx"> 
       <div class="tcaption"> 
        <h3 class="title">财务简析</h3> 
        <span class="ntag vip m-l-sm" data-trigger="hover" data-html="true" data-toggle="tooltip" data-placement="bottom" data-delay="500" title="" data-original-title="尊敬的会员，您正在使用高级特权">功能</span> 
        <span class="watermark"></span> 
       </div> 
       <div class="clearfix" style="position: relative;"> 
        <table id="financialAnalysisTable" class="ntable pull-left" style="width: 178px;"> 
         <tbody>
          <tr data-option="operationRevenueOption" class="active"> 
           <td class="ch">营业收入</td> 
          </tr> 
          <tr data-option="netMarginOption"> 
           <td class="ch">净利润</td> 
          </tr> 
          <tr data-option="totalAssetsOption"> 
           <td class="ch">总资产</td> 
          </tr> 
          <tr data-option="netAssetsOption"> 
           <td class="ch">净资产</td> 
          </tr> 
          <tr data-option="netProfitOption"> 
           <td class="ch">净利率</td> 
          </tr> 
          <tr data-option="grossProfitOption"> 
           <td class="ch">毛利率</td> 
          </tr> 
         </tbody>
        </table> 
        <div id="financialAnalysisChart" class="b-na pull-left m-l-xs" style="width: 702px; height: 265px; padding: 40px 50px 15px; -webkit-tap-highlight-color: transparent; user-select: none;" _echarts_instance_="ec_1557911544870">
         <div style="position: relative; overflow: hidden; width: 600px; height: 208px; padding: 0px; margin: 0px; border-width: 0px;">
          <canvas data-zr-dom-id="zr_0" width="720" height="249" style="position: absolute; left: 0px; top: 0px; width: 600px; height: 208px; user-select: none; -webkit-tap-highlight-color: rgba(0, 0, 0, 0); padding: 0px; margin: 0px; border-width: 0px;"></canvas>
         </div>
        </div> 
        <div id="financialAnalysisTitle" style="position: absolute;top: 10px;left: 196px;right: 15px;font-size: 13px;">
         营业区间：0亿 ~ 30亿
        </div> 
        <div id="financialAnalysisNodata" class="pnodata" style="position: absolute;left: 450px;top: 16px;display: none;"> 
         <img src="/material/theme/chacha/cms/v2/images/nno_image.png" />
         <p>暂无数据</p>
        </div> 
       </div> 
      </section> 
      <div style="position: absolute;width: 50px;opacity: 0;margin-top: -50px;" id="thyfxtpos">
       &nbsp;
      </div> 
      <section class="panel b-a clear" id="thyfx"> 
       <div class="tcaption"> 
        <h3 class="title">同业分析</h3> 
        <span class="ntag vip m-l-sm" data-trigger="hover" data-html="true" data-toggle="tooltip" data-placement="bottom" data-delay="500" title="" data-original-title="尊敬的会员，您正在使用高级特权">功能</span> 
        <span class="watermark"></span> 
       </div> 
       <div class="clearfix" style="position: relative;"> 
        <table id="industryAnalysisTable" class="ntable pull-left" style="width: 178px;"> 
         <tbody>
          <tr data-option="registCountryOption" class="active"> 
           <td class="ch">注册资本（全国）</td> 
          </tr> 
          <tr data-option="registProvinceOption"> 
           <td class="ch">注册资本（本省）</td> 
          </tr> 
          <tr data-option="industryGradeCountryOption"> 
           <td class="ch">同业地位（全国）</td> 
          </tr> 
          <tr data-option="industryGradeProvinceOption"> 
           <td class="ch">同业地位（本省）</td> 
          </tr> 
          <tr data-option="dateCountryChartOption"> 
           <td class="ch">进入市场时期（全国）</td> 
          </tr> 
          <tr data-option="dateProvinceChart"> 
           <td class="ch">进入市场时期（本省）</td> 
          </tr> 
          <tr data-option="areaMapOption"> 
           <td class="ch">同业企业所在地地域分布</td> 
          </tr> 
          <tr data-option="capiMapOption"> 
           <td class="ch">同行业资金地域分布</td> 
          </tr> 
         </tbody>
        </table> 
        <div id="industryAnalysisChart" class="b-na pull-left m-l-xs" style="width: 702px; height: 353px; padding-top: 50px; -webkit-tap-highlight-color: transparent; user-select: none;" _echarts_instance_="ec_1557911544871">
         <div style="position: relative; overflow: hidden; width: 700px; height: 301px; padding: 0px; margin: 0px; border-width: 0px;">
          <canvas data-zr-dom-id="zr_0" width="840" height="361" style="position: absolute; left: 0px; top: 0px; width: 700px; height: 301px; user-select: none; -webkit-tap-highlight-color: rgba(0, 0, 0, 0); padding: 0px; margin: 0px; border-width: 0px;"></canvas>
         </div>
        </div> 
        <div id="industryAnalysisTitle" style="position: absolute;top: 10px;left: 196px;right: 15px;font-size: 13px;">
         该企业注册资本64913万元人民币(元)，属于软件和信息技术服务业。注册资金方面，在全国同行企业中，表现优秀。
        </div> 
       </div> 
      </section> 
      <section class="panel b-a" id="Changelist"> 
       <div class="tcaption"> 
        <h3 class="title">变更记录</h3> 
        <span class="tbadge changelistcount">25</span> 
        <div class="tdrop pull-right"> 
         <span class="btn" data-toggle="dropdown"> <span class="changelisttype">全部类型</span> <span class="caret m-l"></span> </span> 
         <ul class="dropdown-menu dropdown-menu-right"> 
          <li><a onclick="changeRecordsFilter('',this)">全部类型</a></li> 
          <li><a onclick="changeRecordsFilter('章程修正案备案',this)">章程修正案备案</a></li> 
          <li><a onclick="changeRecordsFilter('经营范围变更',this)">经营范围变更</a></li> 
          <li><a onclick="changeRecordsFilter('其他事项',this)">其他事项</a></li> 
          <li><a onclick="changeRecordsFilter('经营期限(营业期限)变',this)">经营期限(营业期限)变</a></li> 
          <li><a onclick="changeRecordsFilter('法定代表人变更',this)">法定代表人变更</a></li> 
          <li><a onclick="changeRecordsFilter('名称变更',this)">名称变更</a></li> 
          <li><a onclick="changeRecordsFilter('企业类型变更',this)">企业类型变更</a></li> 
          <li><a onclick="changeRecordsFilter('境外股东发起人的境内',this)">境外股东发起人的境内</a></li> 
          <li><a onclick="changeRecordsFilter('投资人(股权)变更',this)">投资人(股权)变更</a></li> 
          <li><a onclick="changeRecordsFilter('注册资本(金)变更',this)">注册资本(金)变更</a></li> 
          <li><a onclick="changeRecordsFilter('监事备案',this)">监事备案</a></li> 
          <li><a onclick="changeRecordsFilter('章程备案',this)">章程备案</a></li> 
          <li><a onclick="changeRecordsFilter('董事备案',this)">董事备案</a></li> 
         </ul> 
        </div> 
        <span class="watermark"></span> 
       </div> 
       <table class="ntable"> 
        <tbody>
         <tr> 
          <th class="tx">序号</th> 
          <th>变更日期</th> 
          <th>变更项目</th> 
          <th>变更前</th> 
          <th>变更后</th> 
         </tr> 
         <tr data-pname="章程修正案备案"> 
          <td class="tx">1</td> 
          <td width="103" class="text-center">2018-09-07</td> 
          <td width="" class="text-center"> 章程修正案备案 </td> 
          <td width="30%"> 
           <div style="max-width: 300px;">
             2018-0
            <em>3</em>-
            <em>10</em>章程
            <em>备</em>案 
            <br /> 
           </div> </td> 
          <td width="30%"> 
           <div style="max-width: 300px;">
             2018-0
            <em>8</em>-
            <em>23</em>章程
            <em>修正</em>案 
            <br /> 
           </div> </td> 
         </tr> 
         <tr data-pname="经营范围变更"> 
          <td class="tx">2</td> 
          <td width="103" class="text-center">2018-09-07</td> 
          <td width="" class="text-center"> 经营范围变更 </td> 
          <td width="30%"> 
           <div style="max-width: 300px;">
             计算机网络专业领域内的技术开发并提供相关技术咨询及技术服务,计算机系统集成的设计、安装、调试、维护,通信设备维修
            <em>,食品、宠物用品、服装、成人保健用品、日用百货、家用电器、食用农</em>产品、粮食(中央储备粮食除外)、家居用品、电子产品及配件、甘油、香料香精(除危险化学品、监控化学品、民用爆炸物品)、
            <em>数码产品</em>及配件
            <em>、照相</em>器材、
            <em>针纺织品、化妆品、办公</em>用品、
            <em>体育用品及器材、玩具、汽车用品、汽摩配件、珠宝首饰(毛钻、裸钻</em>除外)
            <em>、工艺品(文物、象牙及其制品</em>除外)
            <em>、五金交电、计算机软硬件及配件</em>(
            <em>音像制品除外)、机械设备、化工产品(危险化学品除外)、消防器材、建筑装饰材料(钢材、水泥除外)、一类医疗器械、二类医疗器械、母婴用品、乳制品(含婴幼儿配方乳粉)、花卉、酒类的批发、零售(店铺零售</em>限分支机构
            <em>)、网上零售、进出口、佣金代理(拍卖除外),票务代理(航空票务代理除外),餐饮管理。餐饮服务、洗衣服务、净水器清洗服务、美容、美发、美甲、健身服务、犬只美容、寄养、销售、儿童游乐设施</em>经营
            <em>(游艺机、危险项目除外</em>)
            <em>(以上项目均限分支机构经营)</em>。【依法须经批准的项目,经相关部门批准后方可开展经营活动】 
            <br /> 
           </div> </td> 
          <td width="30%"> 
           <div style="max-width: 300px;">
             计算机网络专业领域内的技术开发并提供相关技术咨询及技术服务,计算机系统集成的设计、安装、调试、维护,通信设备维修 
            <br /> 
            <em>房地产经纪</em> 
            <br /> 
            <em>第三方物流服务</em> 
            <br /> 
            <em>家政服务</em> 
            <br /> 
            <em>保洁服务</em> 
            <br /> 
            <em>物业管理</em> 
            <br /> 
            <em>病虫害防治服务</em> 
            <br /> 
            <em>搬运装卸</em> 
            <br /> 
            <em>绿化养护</em> 
            <br /> 
            <em>自有设备出租</em> 
            <br /> 
            <em>摄影摄像服务(测绘航空摄影</em>除外) 
            <br /> 
            <em>票务代理(航空票务代理</em>除外) 
            <br /> 
            <em>餐饮企业管理</em> 
            <br /> 
            <em>创意服务</em> 
            <br /> 
            <em>设计</em>、
            <em>制作、代理各类广告</em> 
            <br /> 
            <em>图文设计、制作</em> 
            <br /> 
            <em>市场营销策划</em> 
            <br /> 
            <em>食品、宠物</em>用品、
            <em>服装、成人保健用品、日用百货、家用电器、食用农产品、粮食(中央储备粮食</em>除外)
            <em>、家居用品、电子产品及配件、甘油、香料香精(除危险化学品、监控化学品、民用爆炸物品)、照相器材、家具、针纺织品、化妆品、办公用品、体育用品及器材、玩具、汽车用品、汽摩配件、珠宝首饰(毛钻、裸钻</em>除外)
            <em>、工艺品(文物、象牙及其制品</em>除外)
            <em>、五金交电、计算机软硬件及配件</em>(
            <em>音像制品除外)、机械设备、化工产品(危险化学品除外)、消防器材、建筑装饰材料(钢材、水泥除外)、一类医疗器械、二类医疗器械、母婴用品、乳制品(含婴幼儿配方乳粉)、花卉、酒类的批发、零售(店铺零售</em>限分支机构
            <em>)、网上零售、进出口、佣金代理(拍卖除外),并提供上述商品相关售后配套服务</em> 
            <br /> 
            <em>以自动售货机销售方式进行预包装食品的零售,仓储服务(除危险品,限分公司</em>经营) 
            <br /> 
            <em>餐饮服务</em> 
            <br /> 
            <em>洗衣服务</em> 
            <br /> 
            <em>家电、家具维修服务</em> 
            <br /> 
            <em>净水器清洗服务</em> 
            <br /> 
            <em>服装、皮具、鞋包的修补及维护</em> 
            <br /> 
            <em>美容、美发、美甲、健身服务</em> 
            <br /> 
            <em>犬只美容、寄养、销售</em> 
            <br /> 
            <em>儿童游乐设施经营(游艺机、危险项目除外)(以上项目均限分支机构经营)</em>。【依法须经批准的项目,经相关部门批准后方可开展经营活动】
            <em>。</em> 
            <br /> 
           </div> </td> 
         </tr> 
         <tr data-pname="经营范围变更"> 
          <td class="tx">3</td> 
          <td width="103" class="text-center">2018-05-28</td> 
          <td width="" class="text-center"> 经营范围变更 </td> 
          <td width="30%"> 
           <div style="max-width: 300px;">
             计算机网络专业领域内的技术开发并提供相关技术咨询及技术服务,计算机系统集成的设计、安装、调试、维护,通信设备维修,食品、宠物用品、服装、成人保健用品、日用百货、家用电器、食用农产品、粮食(中央储备粮食除外)、家居用品、数码产品及配件、照相器材、针纺织品、化妆品、办公用品、体育用品及器材、玩具、汽车用品、汽摩配件、珠宝首饰(毛钻、裸钻除外)、工艺品(文物、象牙及其制品除外)、五金交电、计算机软硬件及配件(音像制品除外)、机械设备、化工产品(危险化学品除外)、消防器材、建筑装饰材料(钢材、水泥除外)、一类医疗器械、二类医疗器械、母婴用品、乳制品(含婴幼儿配方乳粉)、花卉、酒类的批发、零售(店铺零售限分支机构)、网上零售、进出口、佣金代理(拍卖除外),票务代理(航空票务代理除外),餐饮管理。餐饮服务、洗衣服务、净水器清洗服务、美容、美发、美甲、健身服务、犬只美容、寄养、销售、儿童游乐设施经营(游艺机、危险项目除外)(以上项目均限分支机构经营)。【依法须经批准的项目,经相关部门批准后方可开展经营活动】
            <em>。</em> 
            <br /> 
           </div> </td> 
          <td width="30%"> 
           <div style="max-width: 300px;">
             计算机网络专业领域内的技术开发并提供相关技术咨询及技术服务,计算机系统集成的设计、安装、调试、维护,通信设备维修,食品、宠物用品、服装、成人保健用品、日用百货、家用电器、食用农产品、粮食(中央储备粮食除外)、家居用品、
            <em>电子</em>产品及配件、
            <em>甘油、香料香精(除</em>危险化学品
            <em>、监控化学品、民用爆炸物品)、数码产品及配件、照相</em>器材、
            <em>针纺织品、化妆品、办公</em>用品、
            <em>体育用品及器材、玩具、汽车用品、汽摩配件、珠宝首饰(毛钻、裸钻</em>除外)
            <em>、工艺品(文物、象牙及其制品</em>除外)
            <em>、五金交电、计算机软硬件及配件(音像制品</em>除外)
            <em>、机械设备、化工产品</em>(
            <em>危险化学品除外)、消防器材、建筑装饰材料(钢材、水泥除外)、一类医疗器械、二类医疗器械、母婴用品、乳制品(含婴幼儿配方乳粉)、花卉、酒类的批发、零售(店铺零售</em>限分支机构
            <em>)、网上零售、进出口、佣金代理(拍卖除外),票务代理(航空票务代理除外),餐饮管理。餐饮服务、洗衣服务、净水器清洗服务、美容、美发、美甲、健身服务、犬只美容、寄养、销售、儿童游乐设施</em>经营
            <em>(游艺机、危险项目除外</em>)
            <em>(以上项目均限分支机构经营)</em>。【依法须经批准的项目,经相关部门批准后方可开展经营活动】 
            <br /> 
           </div> </td> 
         </tr> 
         <tr data-pname="章程修正案备案"> 
          <td class="tx">4</td> 
          <td width="103" class="text-center">2017-10-19</td> 
          <td width="" class="text-center"> 章程修正案备案 </td> 
          <td width="30%"> 
           <div style="max-width: 300px;">
             2017-0
            <em>8</em>-
            <em>04</em>章程
            <em>备</em>案 
            <br /> 
           </div> </td> 
          <td width="30%"> 
           <div style="max-width: 300px;">
             2017-0
            <em>9</em>-
            <em>28</em>章程
            <em>修正</em>案 
            <br /> 
           </div> </td> 
         </tr> 
         <tr data-pname="经营范围变更"> 
          <td class="tx">5</td> 
          <td width="103" class="text-center">2017-10-19</td> 
          <td width="" class="text-center"> 经营范围变更 </td> 
          <td width="30%"> 
           <div style="max-width: 300px;">
             计算机网络专业领域内的技术开发并提供相关技术咨询及技术服务,计算机系统集成的设计、安装、调试、维护,食品、服装、日用百货、家用电器、食用农产品、粮食(中央储备粮食除外)、家居用品、数码产品及配件、照相器材、针纺织品、化妆品、办公用品、体育用品及器材、玩具、汽车用品、汽摩配件、珠宝首饰(毛钻、裸钻除外)、工艺品(文物除外)、五金交电、计算机软硬件及配件(音像制品除外)、机械设备、化工产品(危险化学品除外)、消防器材、建筑装饰材料(钢材、水泥除外)、一类医疗器械、二类医疗器械、母婴用品、乳制品(含婴幼儿配方乳粉)、花卉、酒类的批发、零售(店铺零售限分支机构)、网上零售,票务代理(航空票务代理除外),餐饮管理
            <em>,</em>餐饮服务
            <em>(</em>限分支机构经营)。【依法须经批准的项目,经相关部门批准后方可开展经营活动】 
            <br /> 
           </div> </td> 
          <td width="30%"> 
           <div style="max-width: 300px;">
             计算机网络专业领域内的技术开发并提供相关技术咨询及技术服务,计算机系统集成的设计、安装、调试、维护,
            <em>通信设备维修,</em>食品、
            <em>宠物</em>用品、
            <em>服装、成人保健</em>用品、
            <em>日用百货、家用电器、食用农产品、粮食(中央储备粮食</em>除外)、
            <em>家居</em>用品、
            <em>数码产品及配件、照相器材、针纺织品、化妆品、办公用品、体育用品及器材、玩具、汽车用品、汽摩配件、珠宝首饰(毛钻、裸钻</em>除外)
            <em>、工艺品(文物、象牙及其制品除外)、五金交电、计算机软硬件及配件(音像制品除外)、机械设备、化工产品(危险化学品除外)、消防器材、建筑装饰材料(钢材、水泥除外)、一类医疗器械、二类医疗器械、母婴用品、乳制品(含婴幼儿配方乳粉)、花卉、酒类的批发、零售(店铺零售</em>限分支机构
            <em>)、网上零售、进出口、佣金代理(拍卖除外),票务代理(航空票务代理除外),餐饮管理。餐饮服务、洗衣服务、净水器清洗服务、美容、美发、美甲、健身服务、犬只美容、寄养、销售、儿童游乐设施</em>经营
            <em>(游艺机、危险项目除外</em>)
            <em>(以上项目均限分支机构经营)</em>。【依法须经批准的项目,经相关部门批准后方可开展经营活动】
            <em>。</em> 
            <br /> 
           </div> </td> 
         </tr> 
         <tr data-pname="章程修正案备案"> 
          <td class="tx">6</td> 
          <td width="103" class="text-center">2017-08-17</td> 
          <td width="" class="text-center"> 章程修正案备案 </td> 
          <td width="30%"> 
           <div style="max-width: 300px;">
             2017-0
            <em>1</em>-0
            <em>3</em>章程
            <em>备</em>案 
            <br /> 
           </div> </td> 
          <td width="30%"> 
           <div style="max-width: 300px;">
             2017-0
            <em>8</em>-0
            <em>4</em>章程
            <em>修正</em>案 
            <br /> 
           </div> </td> 
         </tr> 
         <tr data-pname="经营范围变更"> 
          <td class="tx">7</td> 
          <td width="103" class="text-center">2017-08-17</td> 
          <td width="" class="text-center"> 经营范围变更 </td> 
          <td width="30%"> 
           <div style="max-width: 300px;">
             计算机网络专业领域内的技术开发并提供相关技术咨询及技术服务,计算机系统集成的设计、安装、调试、维护,食品、服装、日用百货、家用电器、食用农产品、粮食(中央储备粮食除外)、家居用品、数码产品及配件、照相器材、针纺织品、化妆品、办公用品、体育用品及器材、玩具、汽车用品、汽摩配件、珠宝首饰(毛钻、裸钻除外)、工艺品(文物除外)、五金交电、计算机软硬件及配件(音像制品除外)、机械设备、化工产品(危险化学品除外)、消防器材、建筑装饰材料(钢材、水泥除外)、一类医疗器械、二类医疗器械、母婴用品、乳制品(含婴幼儿配方乳粉)、花卉、酒类的批发、零售(店铺零售限分支机构),票务代理(航空票务代理除外),餐饮管理,餐饮服务(限分支机构经营)。【依法须经批准的项目,经相关部门批准后方可开展经营活动】 
            <br /> 
           </div> </td> 
          <td width="30%"> 
           <div style="max-width: 300px;">
             计算机网络专业领域内的技术开发并提供相关技术咨询及技术服务,计算机系统集成的设计、安装、调试、维护,食品、服装、日用百货、家用电器、食用农产品、粮食(中央储备粮食除外)、家居用品、数码产品及配件、照相器材、针纺织品、化妆品、办公用品、体育用品及器材、玩具、汽车用品、汽摩配件、珠宝首饰(毛钻、裸钻除外)、工艺品(文物除外)、五金交电、计算机软硬件及配件(音像制品除外)、机械设备、化工产品(危险化学品除外)、消防器材、建筑装饰材料(钢材、水泥除外)、一类医疗器械、二类医疗器械、母婴用品、乳制品(含婴幼儿配方乳粉)、花卉、酒类的批发、零售(店铺零售限分支机构)
            <em>、网上零售</em>,票务代理(航空票务代理除外),餐饮管理,餐饮服务(限分支机构经营)。【依法须经批准的项目,经相关部门批准后方可开展经营活动】 
            <br /> 
           </div> </td> 
         </tr> 
         <tr data-pname="其他事项"> 
          <td class="tx">8</td> 
          <td width="103" class="text-center">2017-06-29</td> 
          <td width="" class="text-center"> 其他事项 </td> 
          <td width="30%"> 
           <div style="max-width: 300px;">
             2017-0
            <em>5</em>-
            <em>11</em>~ 
            <br /> 
           </div> </td> 
          <td width="30%"> 
           <div style="max-width: 300px;">
             2017-0
            <em>6</em>-
            <em>29</em>~ 
            <br /> 
           </div> </td> 
         </tr> 
         <tr data-pname="经营期限(营业期限)变"> 
          <td class="tx">9</td> 
          <td width="103" class="text-center">2017-06-29</td> 
          <td width="" class="text-center"> 经营期限(营业期限)变 </td> 
          <td width="30%"> 
           <div style="max-width: 300px;">
             2015-06-02~ 
            <br /> 
           </div> </td> 
          <td width="30%"> 
           <div style="max-width: 300px;">
             2015-06-02~
            <em>2046-09-18</em> 
            <br /> 
           </div> </td> 
         </tr> 
         <tr data-pname="法定代表人变更"> 
          <td class="tx">10</td> 
          <td width="103" class="text-center">2017-05-11</td> 
          <td width="" class="text-center"> 法定代表人变更 <br /><span class="text-gray" style="font-size: 12px">带有*标记的为法定代表人</span> </td> 
          <td width="30%"> 
           <div style="max-width: 300px;"> 
            <em><a href="pl_p2c4af03fd352ef1ffb597fa6331f71c.html">郑俊芳</a></em> 
            <br /> 
           </div> </td> 
          <td width="30%"> 
           <div style="max-width: 300px;"> 
            <em><a href="pl_p73ac1d107d8235907d5087e3b3abe6b.html">侯毅</a>*</em> 
            <br /> 
           </div> </td> 
         </tr> 
         <tr data-pname="名称变更"> 
          <td class="tx">11</td> 
          <td width="103" class="text-center">2017-03-03</td> 
          <td width="" class="text-center"> 名称变更 </td> 
          <td width="30%"> 
           <div style="max-width: 300px;">
             上海
            <em>翌恒</em>网络科技有限公司 
            <br /> 
           </div> </td> 
          <td width="30%"> 
           <div style="max-width: 300px;">
             上海
            <em>盒马</em>网络科技有限公司 
            <br /> 
           </div> </td> 
         </tr> 
         <tr data-pname="章程修正案备案"> 
          <td class="tx">12</td> 
          <td width="103" class="text-center">2017-03-03</td> 
          <td width="" class="text-center"> 章程修正案备案 </td> 
          <td width="30%"> 
           <div style="max-width: 300px;">
             201
            <em>6</em>-0
            <em>7</em>-
            <em>12</em>章程
            <em>备</em>案 
            <br /> 
           </div> </td> 
          <td width="30%"> 
           <div style="max-width: 300px;">
             201
            <em>7</em>-0
            <em>1</em>-
            <em>03</em>章程
            <em>修正</em>案 
            <br /> 
           </div> </td> 
         </tr> 
         <tr data-pname="经营范围变更"> 
          <td class="tx">13</td> 
          <td width="103" class="text-center">2017-03-03</td> 
          <td width="" class="text-center"> 经营范围变更 </td> 
          <td width="30%"> 
           <div style="max-width: 300px;">
             计算机网络专业领域内的技术开发并提供相关技术咨询及技术服务,计算机系统集成的设计、安装、调试、维护,食品
            <em>流通</em>、服装、日用百货、家用电器、食用农产品、粮食、家居用品、数码产品及配件、照相器材、针纺织品、化妆品、办公用品、体育用品及器材、玩具、汽车用品、汽摩配件、珠宝首饰(毛钻、裸钻除外)、工艺品(文物除外)、五金交电、计算机软硬件及配件(音像制品除外)、机械设备、化工产品(危险化学品除外)、消防器材、建筑装饰材料(钢材、水泥除外)、一类医疗器械、
            <em>花卉</em>的批发、零售(店铺零售限分支机构),票务代理(航空票务代理除外),餐饮管理,餐饮服务(限分支机构经营)。【依法须经批准的项目,经相关部门批准后方可开展经营活动】 
            <br /> 
           </div> </td> 
          <td width="30%"> 
           <div style="max-width: 300px;">
             计算机网络专业领域内的技术开发并提供相关技术咨询及技术服务,计算机系统集成的设计、安装、调试、维护,食品、服装、日用百货、家用电器、食用农产品、粮食
            <em>(中央储备粮食</em>除外)、
            <em>家居用品、数码产品</em>及配件
            <em>、照相</em>器材、
            <em>针纺织品、化妆品、办公用品、体育用品及器材、玩具、汽车用品、汽摩配件、珠宝首饰(毛钻、裸钻</em>除外)、
            <em>工艺品(文物</em>除外)
            <em>、五金交电、计算机软硬件及配件(音像制品除外)、机械设备、化工产品(危险化学品除外)、消防器材、建筑装饰材料(钢材、水泥除外)、一类医疗器械、二类医疗器械、母婴用品、乳制品(含婴幼儿配方乳粉)、花卉、酒类的批发、零售(店铺零售</em>限分支机构
            <em>),票务代理(航空票务代理除外),餐饮管理,餐饮服务(限分支机构</em>经营)。【依法须经批准的项目,经相关部门批准后方可开展经营活动】 
            <br /> 
           </div> </td> 
         </tr> 
         <tr data-pname="企业类型变更"> 
          <td class="tx">14</td> 
          <td width="103" class="text-center">2016-09-19</td> 
          <td width="" class="text-center"> 企业类型变更 </td> 
          <td width="30%"> 
           <div style="max-width: 300px;"> 
            <em>一人</em>有限责任公司(
            <em>自然人投资或控股的</em>法人独资) 
            <br /> 
           </div> </td> 
          <td width="30%"> 
           <div style="max-width: 300px;">
             有限责任公司(
            <em>台港澳</em>法人独资) 
            <br /> 
           </div> </td> 
         </tr> 
         <tr data-pname="境外股东发起人的境内"> 
          <td class="tx">15</td> 
          <td width="103" class="text-center">2016-09-19</td> 
          <td width="" class="text-center"> 境外股东发起人的境内 </td> 
          <td width="30%"> 
           <div style="max-width: 300px;">
             无 
            <br /> 
           </div> </td> 
          <td width="30%"> 
           <div style="max-width: 300px;"> 
            <em>龚汤仙【新增】</em> 
            <br /> 
           </div> </td> 
         </tr> 
         <tr data-pname="投资人(股权)变更"> 
          <td class="tx">16</td> 
          <td width="103" class="text-center">2016-09-19</td> 
          <td width="" class="text-center"> 投资人(股权)变更 </td> 
          <td width="30%"> 
           <div style="max-width: 300px;"> 
            <em><a href="firm_a8e7e2067e33b36274e99cf223943016.html">象翌微链科技发展有限公司</a>【退出】</em> 
            <br /> 
           </div> </td> 
          <td width="30%"> 
           <div style="max-width: 300px;"> 
            <em>Hema(HongKong)Limited【新增】</em> 
            <br /> 
           </div> </td> 
         </tr> 
         <tr data-pname="法定代表人变更"> 
          <td class="tx">17</td> 
          <td width="103" class="text-center">2016-09-19</td> 
          <td width="" class="text-center"> 法定代表人变更 </td> 
          <td width="30%"> 
           <div style="max-width: 300px;"> 
            <em><a href="pl_p46782e8db0409a515876b2361290b37.html">陶国谦</a></em> 
            <br /> 
           </div> </td> 
          <td width="30%"> 
           <div style="max-width: 300px;"> 
            <em><a href="pl_p2c4af03fd352ef1ffb597fa6331f71c.html">郑俊芳</a></em> 
            <br /> 
           </div> </td> 
         </tr> 
         <tr data-pname="注册资本(金)变更"> 
          <td class="tx">18</td> 
          <td width="103" class="text-center">2016-09-19</td> 
          <td width="" class="text-center"> 注册资本(金)变更 </td> 
          <td width="30%"> 
           <div style="max-width: 300px;"> 
            <em>1000.0000</em>万人民币 
            <br /> 
           </div> </td> 
          <td width="30%"> 
           <div style="max-width: 300px;"> 
            <em>64913.0000</em>万人民币
            <em>(+6391.3%)</em> 
            <br /> 
           </div> </td> 
         </tr> 
         <tr data-pname="监事备案"> 
          <td class="tx">19</td> 
          <td width="103" class="text-center">2016-09-19</td> 
          <td width="" class="text-center"> 监事备案 </td> 
          <td width="30%"> 
           <div style="max-width: 300px;">
             无 
            <br /> 
           </div> </td> 
          <td width="30%"> 
           <div style="max-width: 300px;"> 
            <em><a href="pl_pd569a04b441a1ad875c43e236d98a8a.html">冯云乐</a>【新增】</em> 
            <br /> 
           </div> </td> 
         </tr> 
         <tr data-pname="章程备案"> 
          <td class="tx">20</td> 
          <td width="103" class="text-center">2016-09-19</td> 
          <td width="" class="text-center"> 章程备案 </td> 
          <td width="30%"> 
           <div style="max-width: 300px;">
             2016-0
            <em>3</em>-
            <em>0</em>1章程备案 
            <br /> 
           </div> </td> 
          <td width="30%"> 
           <div style="max-width: 300px;">
             2016-0
            <em>7</em>-1
            <em>2</em>章程备案 
            <br /> 
           </div> </td> 
         </tr> 
         <tr data-pname="经营范围变更"> 
          <td class="tx">21</td> 
          <td width="103" class="text-center">2016-09-19</td> 
          <td width="" class="text-center"> 经营范围变更 </td> 
          <td width="30%"> 
           <div style="max-width: 300px;">
             计算机网络专业领域内的技术开发
            <em>、</em>技术咨询
            <em>、</em>技术
            <em>转让、技术</em>服务,计算机系统集成
            <em>,</em>服装、日用百货、家用电器、食用农产品、家居用品、数码产品及配件、照相器材、针纺织品、化妆品、办公用品、体育用品及器材、玩具、汽车用品、汽摩配件、珠宝首饰、工艺品、五金交电、计算机软硬件及配件、机械设备、化工产品(
            <em>除</em>危险化学品
            <em>、监控化学品、民用爆炸物品、易制毒化学品</em>)、消防器材、建筑装饰材料
            <em>、</em>医疗器械、花卉的
            <em>销售</em>,票务代理,餐饮
            <em>企业</em>管理,餐饮服务(限分支机构经营)
            <em>,食品流通,烟草专卖零售(取得许可证件</em>后方可
            <em>从事是</em>经营活动
            <em>)。【依法须经批准的项目,经相关部门批准后方可开展经营活动</em>】 
            <br /> 
           </div> </td> 
          <td width="30%"> 
           <div style="max-width: 300px;">
             计算机网络专业领域内的技术开发
            <em>并提供相关</em>技术咨询
            <em>及</em>技术服务,计算机系统集成
            <em>的设计、安装、调试、维护</em>,食品流通
            <em>、服装、日用百货、家用电器、食用农产品、粮食、家居用品、数码产品及配件、照相器材、针纺织品、化妆品、办公用品、体育用品及器材、玩具、汽车用品、汽摩配件、珠宝首饰(毛钻、裸钻除外)、工艺品(文物除外)、五金交电、计算机软硬件及配件(音像制品除外)、机械设备、化工产品(危险化学品除外)、消防器材、建筑装饰材料(钢材、水泥除外)、一类医疗器械、花卉的批发、</em>零售(
            <em>店铺零售限分支机构),票务代理(航空票务代理除外),餐饮管理,餐饮服务(限分支机构经营</em>)。【依法须经批准的项目,经相关部门批准后方可开展经营活动】 
            <br /> 
           </div> </td> 
         </tr> 
         <tr data-pname="董事备案"> 
          <td class="tx">22</td> 
          <td width="103" class="text-center">2016-09-19</td> 
          <td width="" class="text-center"> 董事备案 </td> 
          <td width="30%"> 
           <div style="max-width: 300px;">
             无 
            <br /> 
           </div> </td> 
          <td width="30%"> 
           <div style="max-width: 300px;"> 
            <em><a href="pl_pa14da0de0e32e960da96e985c4f5e5e.html">徐殿勇</a>【新增】</em> 
            <br /> 
            <em><a href="pl_p580cd17d9f541702a808e95feee7bc6.html">俞思瑛</a>;【新增】</em> 
            <br /> 
           </div> </td> 
         </tr> 
         <tr data-pname="章程修正案备案"> 
          <td class="tx">23</td> 
          <td width="103" class="text-center">2016-03-03</td> 
          <td width="" class="text-center"> 章程修正案备案 </td> 
          <td width="30%"> 
           <div style="max-width: 300px;"> 
            <em>无</em> 
            <br /> 
           </div> </td> 
          <td width="30%"> 
           <div style="max-width: 300px;"> 
            <em>2016-03-01章程修正案</em> 
            <br /> 
           </div> </td> 
         </tr> 
         <tr data-pname="经营范围变更"> 
          <td class="tx">24</td> 
          <td width="103" class="text-center">2016-03-03</td> 
          <td width="" class="text-center"> 经营范围变更 </td> 
          <td width="30%"> 
           <div style="max-width: 300px;">
             计算机网络专业领域内的技术开发、技术咨询、技术转让、技术服务,计算机系统集成,服装、日用百货、家用电器、食用农产品、家居用品、数码产品及配件、照相器材、针纺织品、化妆品、办公用品、体育用品及器材、玩具、汽车用品、汽摩配件、珠宝首饰、工艺品、五金交电、计算机软硬件及配件、机械设备、化工产品(除危险化学品、监控化学品、
            <em>烟花爆竹、</em>民用爆炸物品、易制毒化学品)、消防器材、建筑装饰材料、医疗器械的销售,票务代理,餐饮企业管理,餐饮服务(限分支机构经营)。【依法须经批准的项目,经相关部门批准后方可开展经营活动】 
            <br /> 
           </div> </td> 
          <td width="30%"> 
           <div style="max-width: 300px;">
             计算机网络专业领域内的技术开发、技术咨询、技术转让、技术服务,计算机系统集成,服装、日用百货、家用电器、食用农产品、家居用品、数码产品及配件、照相器材、针纺织品、化妆品、办公用品、体育用品及器材、玩具、汽车用品、汽摩配件、珠宝首饰、工艺品、五金交电、计算机软硬件及配件、机械设备、化工产品(除危险化学品、监控化学品、民用爆炸物品、易制毒化学品)、消防器材、建筑装饰材料、医疗器械
            <em>、花卉</em>的销售,票务代理,餐饮企业管理,餐饮服务(限分支机构经营)
            <em>,食品流通,烟草专卖零售(取得许可证件</em>后方可
            <em>从事是</em>经营活动
            <em>)。【依法须经批准的项目,经相关部门批准后方可开展经营活动</em>】 
            <br /> 
           </div> </td> 
         </tr> 
         <tr data-pname="经营范围变更"> 
          <td class="tx">25</td> 
          <td width="103" class="text-center">2015-07-02</td> 
          <td width="" class="text-center"> 经营范围变更 </td> 
          <td width="30%"> 
           <div style="max-width: 300px;">
             计算机网络专业领域内的技术咨询、技术
            <em>服务</em>、技术
            <em>转让、技术</em>服务,计算机系统集成,服装、日用百货、家用电器、食用农产品、家居用品、数码产品及配件、照相器材、针纺织品、化妆品、办公用品、体育用品及器材、玩具、汽车用品、汽摩配件、珠宝首饰、工艺品、五金交电、计算机软硬件及配件、机械设备、化工产品(除危险化学品、监控化学品、烟花爆竹、民用爆炸物品、易制毒化学品)、消防器材、建筑装饰材料、医疗器械的销售,票务代理,餐饮企业管理。【依法须经批准的项目,经相关部门批准后方可开展经营活动】 
            <br /> 
           </div> </td> 
          <td width="30%"> 
           <div style="max-width: 300px;">
             计算机网络专业领域内的技术
            <em>开发</em>、技术
            <em>咨询</em>、技术转让、技术服务,计算机系统集成,服装、日用百货、家用电器、食用农产品、家居用品、数码产品及配件、照相器材、针纺织品、化妆品、办公用品、体育用品及器材、玩具、汽车用品、汽摩配件、珠宝首饰、工艺品、五金交电、计算机软硬件及配件、机械设备、化工产品(除危险化学品、监控化学品、烟花爆竹、民用爆炸物品、易制毒化学品)、消防器材、建筑装饰材料、医疗器械的销售,票务代理,餐饮企业管理
            <em>,餐饮服务(限分支机构经营)</em>。【依法须经批准的项目,经相关部门批准后方可开展经营活动】 
            <br /> 
           </div> </td> 
         </tr> 
        </tbody>
       </table> 
      </section> 
      <section class="panel b-a clear"> 
       <div class="m_ptsc" style="padding:20px 0;">
        数据来源：国家企业信用信息公示系统。
       </div> 
      </section> 
      <script type="text/javascript" src="/material/theme/chacha/cms/v2/js/baseChart.js?time=1557743995"></script> 
      <script type="text/javascript">

    $(function(){
        var touziIndustry = JSON.parse('[{"value":"F","desc":"\u6279\u53d1\u548c\u96f6\u552e\u4e1a","count":1},{"value":"G","desc":"\u4ea4\u901a\u8fd0\u8f93\u3001\u4ed3\u50a8\u548c\u90ae\u653f\u4e1a","count":1}]');
        var touziProvince = JSON.parse('[{"value":"GD","count":1,"desc":"\u5e7f\u4e1c"},{"value":"SH","count":1,"desc":"\u4e0a\u6d77"}]');
        
        showHistoryTip();
        
         //低于5个隐藏图表

        industryAnalysis('e45ee37279ffb3f2ce9bbbcfa39d8133');
        financialAnalysis('e45ee37279ffb3f2ce9bbbcfa39d8133');
        muhouIframe();
    })

    function baseDrawGuquanStatic(){
        if(!$('#guquanStatic').html()){
            drawGuquanStatic('上海盒马网络科技有限公司',[{"Org":3,"KeyNo":"hcb57b19bc9cd13855cfb774959b8730","HasImage":false,"CompanyCount":11,"StockName":"Hema (Hong Kong) Limited","StockType":"\u5916\u56fd(\u5730\u533a)\u4f01\u4e1a","StockPercent":"100%","IdentifyType":"\u5176\u4ed6","IdentifyNo":"2337110","ShouldCapi":"64913","ShoudDate":null,"InvestType":null,"InvestName":null,"RealCapi":null,"CapiDate":null,"StockPercentValue":100,"ShouldCapiAmount":64913,"ImageUrl":"https:\/\/qccdata.qichacha.com\/AutoImage\/hcb57b19bc9cd13855cfb774959b8730.jpg?x-oss-process=image\/resize,w_120","HasStockDetail":false,"HasPledgeInfo":false,"StockPercentNew":"100","bigPartner":true,"kzr":true,"syr":true,"hwqy":"\u9999\u6e2f"}]);
        }
        if(isFirefox=navigator.userAgent.indexOf("Firefox")>0){  
          $('#guquanIframe').attr('src','company_guquan?keyNo=e45ee37279ffb3f2ce9bbbcfa39d8133&iframe=1');
        }  
    }



</script> 
     </div> 
     <div class="data_div" id="susong_div" style="display: none;"> 
      <div class="susong_info"></div> 
      <section class="panel b-a clear m_dataTab"> 
       <div class="panel-body" style="padding-top: 5px;"> 
        <a href="javascript:;" class="btn btn-sm btn-default m-t-sm m-r-sm c_disable" style="white-space:nowrap;cursor: default"> 被执行人信息&nbsp;0 </a> 
        <a href="javascript:;" class="btn btn-sm btn-default m-t-sm m-r-sm c_disable" style="white-space:nowrap;cursor: default"> 失信被执行人&nbsp;0 </a> 
        <a href="javascript:;" onclick="boxScrollNew('#wenshulist');zhugeTrack('企业主页-法律诉讼-裁判文书',{'企业名称':'上海盒马网络科技有限公司'});" class="btn btn-sm btn-default m-t-sm m-r-sm" style="white-space:nowrap;"> 裁判文书&nbsp;30 </a> 
        <a href="javascript:;" class="btn btn-sm btn-default m-t-sm  m-r-sm c_disable" style="white-space:nowrap;cursor: default"> 法院公告&nbsp;0 </a> 
        <a href="javascript:;" onclick="boxScrollNew('#noticelist');zhugeTrack('企业主页-法律诉讼-开庭公告',{'企业名称':'上海盒马网络科技有限公司'});" class="btn m-t-sm btn-sm btn-default  m-r-sm" style="white-space:nowrap;"> 开庭公告&nbsp;43 </a> 
        <a href="javascript:;" class="btn btn-sm btn-default m-t-sm  m-r-sm c_disable" style="white-space:nowrap;cursor: default"> 送达公告&nbsp;0 </a> 
        <a href="javascript:;" class="btn btn-sm btn-default m-t-sm   m-r-sm c_disable" style="white-space:nowrap;cursor: default"> 司法协助&nbsp;0 </a> 
        <a href="javascript:;" class="btn btn-sm btn-default m-t-sm  m-r-sm c_disable" style="white-space:nowrap;cursor: default"> 立案信息&nbsp;0 </a> 
       </div> 
      </section> 
      <section class="panel b-a clear"> 
       <div class="tcaption"> 
        <h3 class="title"> 统计分析</h3> 
        <a class="hchart" onclick="hideChart(this)" href="javascript:;"> <span>收起</span> <i class="i i-arrow-up4"></i> </a> 
       </div> 
       <div class="float-wrap"> 
        <div class="col-sm-6 col-xs-12 no-padding rb">
         <div id="susong-province" class="nchart-item hmd" _echarts_instance_="ec_1557911544287" style="-webkit-tap-highlight-color: transparent; user-select: none; position: relative; background: rgb(255, 255, 255);">
          <div style="position: relative; overflow: hidden; width: 436px; height: 298px;">
           <canvas width="523" height="357" data-zr-dom-id="zr_0" style="position: absolute; left: 0px; top: 0px; width: 436px; height: 298px; user-select: none; -webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></canvas>
          </div>
          <div></div>
         </div>
        </div> 
        <div class="col-sm-6 col-xs-12 no-padding" style="padding-left: 7px;">
         <div id="susong-year" class="nchart-item hmd" _echarts_instance_="ec_1557911544288" style="-webkit-tap-highlight-color: transparent; user-select: none; position: relative; background: transparent;">
          <div style="position: relative; overflow: hidden; width: 436px; height: 298px;">
           <canvas width="523" height="357" data-zr-dom-id="zr_0" style="position: absolute; left: 0px; top: 0px; width: 436px; height: 298px; user-select: none; -webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></canvas>
          </div>
          <div></div>
         </div>
        </div> 
       </div> 
      </section> 
      <section class="panel b-a clear"> 
       <div class="tcaption"> 
        <h3 class="title">裁判文书统计分析</h3> 
        <span class="watermark"></span> 
       </div> 
       <div class="clearfix" style="position: relative;"> 
        <table id="wenshuAnaTable" class="ntable pull-left" style="width: 150px;"> 
         <tbody>
          <tr data-option="reasonOption" class="active"> 
           <td class="ch">案由统计 TOP10</td> 
          </tr> 
          <tr data-option="participantOption"> 
           <td class="ch">原告/被告统计</td> 
          </tr> 
          <tr data-option="courtlevelOption"> 
           <td class="ch">法院层级统计</td> 
          </tr> 
          <tr data-option="provinceOption"> 
           <td class="ch">涉案地区分布</td> 
          </tr> 
          <tr data-option="casetypeOption"> 
           <td class="ch">涉案文书类型统计</td> 
          </tr> 
          <tr data-option="submityearOption"> 
           <td class="ch">年度涉案信息统计</td> 
          </tr> 
          <tr data-option="courtmonthOption"> 
           <td class="ch">近1年涉案信息统计</td> 
          </tr> 
         </tbody>
        </table> 
        <div id="wenshuAnaChart" class="b-na pull-left m-l-xs" style="width: 730px; height: 309px; -webkit-tap-highlight-color: transparent; user-select: none;" _echarts_instance_="ec_1557911544872">
         <div style="position: relative; overflow: hidden; width: 728px; height: 308px; padding: 0px; margin: 0px; border-width: 0px;">
          <canvas data-zr-dom-id="zr_0" width="873" height="369" style="position: absolute; left: 0px; top: 0px; width: 728px; height: 308px; user-select: none; -webkit-tap-highlight-color: rgba(0, 0, 0, 0); padding: 0px; margin: 0px; border-width: 0px;"></canvas>
         </div>
        </div> 
        <div id="wenshuAnaTitle" style="position: absolute;top: 10px;left: 172px;right: 50px;font-size: 13px;">
         案由统计 TOP10
        </div> 
        <div id="wenshuAnaNodata" class="pnodata" style="position: absolute;left: 450px;top: 30px;display: none;"> 
         <img src="/material/theme/chacha/cms/v2/images/nno_image.png" />
         <p>暂无数据</p>
        </div> 
       </div> 
      </section> 
      <section class="panel  b-a" id="wenshulist"> 
       <div class="tcaption"> 
        <h3 class="title"> 裁判文书</h3> 
        <span class="tbadger">30</span> 
        <div class="chooseSusong" data-box="wenshu" style="float: right"> 
         <div class="tdrop"> 
          <span class="btn" data-toggle="dropdown"> <span>案由不限</span> <span class="caret m-l"></span> </span> 
          <ul class="dropdown-menu dropdown-menu-right"> 
           <li><a href="javascript:;" data-option="casereason" data-value="0">不限</a></li> 
           <li><a href="javascript:;" data-option="casereason" data-value="0418">买卖合同纠纷(16)</a></li> 
           <li><a href="javascript:;" data-option="casereason" data-value="0016">生命权、健康权、身体权纠纷(4)</a></li> 
           <li><a href="javascript:;" data-option="casereason" data-value="0029">财产损害赔偿纠纷(3)</a></li> 
           <li><a href="javascript:;" data-option="casereason" data-value="0124">网络购物纠纷(3)</a></li> 
           <li><a href="javascript:;" data-option="casereason" data-value="0001">民间借贷纠纷(2)</a></li> 
           <li><a href="javascript:;" data-option="casereason" data-value="0003">机动车交通事故责任纠纷(1)</a></li> 
           <li><a href="javascript:;" data-option="casereason" data-value="0028">提供劳务受害者责任纠纷(1)</a></li> 
          </ul> 
         </div> 
        </div> 
        <span class="watermark"></span> 
       </div> 
       <table class="ntable ntable-odd"> 
        <tbody>
         <tr>
          <th class="tx">序号</th>
          <th>案件名称</th>
          <th>案由</th>
          <th>案件金额</th>
          <th>发布时间</th>
          <th>案件编号</th>
          <th>案件身份</th>
          <th>执行法院</th>
         </tr> 
         <tr> 
          <td class="tx">1</td> 
          <td width=""><a target="_blank" href="/wenshuDetail_com_946015472db8d3027ede650e97238ad1.html"><h3 class="seo font-14">宁波上嘉人力资源服务有限公司与洪小年、刘振彪生命权、健康权、身体权纠纷二审民事判决书</h3></a></td> 
          <td width="103">生命权、健康权、身体权纠纷</td> 
          <td width="103" class="text-center">-</td> 
          <td width="103">2019-05-06</td> 
          <td width="12%">（2018）沪02民终10760号</td> 
          <td width="16%"> 
           <div class="m-b-xs">
            上诉人（原审第三人） - 
            <a href="/search?key=%E5%AE%81%E6%B3%A2%E4%B8%8A%E5%98%89%E4%BA%BA%E5%8A%9B%E8%B5%84%E6%BA%90%E6%9C%8D%E5%8A%A1%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8" class="c_a" target="_blank">宁波上嘉人力资源服务有限公司</a>
           </div> 
           <div class="m-b-xs">
            代理律师事务所 - 
            <a href="/search?key=%E5%8C%97%E4%BA%AC%E5%A4%A7%E6%88%90%EF%BC%88%E4%B8%8A%E6%B5%B7%EF%BC%89%E5%BE%8B%E5%B8%88%E4%BA%8B%E5%8A%A1%E6%89%80" class="c_a" target="_blank">北京大成（上海）律师事务所</a>
           </div> 
           <div class="m-b-xs">
            原审第三人 - 
            <a href="/search?key=%E4%B8%8A%E6%B5%B7%E7%9B%92%E9%A9%AC%E7%BD%91%E7%BB%9C%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8" class="c_a" target="_blank">上海盒马网络科技有限公司</a>
           </div> 
           <div class="m-b-xs">
            代理律师事务所 - 
            <a href="/search?key=%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%BE%8B%E5%92%8C%E7%90%86%E5%BE%8B%E5%B8%88%E4%BA%8B%E5%8A%A1%E6%89%80" class="c_a" target="_blank">上海市律和理律师事务所</a>
           </div> 
           <div class="m-b-xs">
            被上诉人（原审被告） - 
            <a href="/search?key=%E5%88%98%E6%8C%AF%E5%BD%AA" class="c_a" target="_blank">刘振彪</a>
           </div> 
           <div class="m-b-xs">
            被上诉人（原审原告） - 
            <a href="/search?key=%E6%B4%AA%E5%B0%8F%E5%B9%B4" class="c_a" target="_blank">洪小年</a>
           </div> 
           <div class="m-b-xs">
            代理律师事务所 - 
            <a href="/search?key=%E5%8C%97%E4%BA%AC%E5%B0%9A%E5%85%AC%EF%BC%88%E4%B8%8A%E6%B5%B7%EF%BC%89%E5%BE%8B%E5%B8%88%E4%BA%8B%E5%8A%A1%E6%89%80" class="c_a" target="_blank">北京尚公（上海）律师事务所</a>
           </div> </td> 
          <td width="15%">上海市第二中级人民法院</td> 
         </tr> 
         <tr> 
          <td class="tx">2</td> 
          <td width=""><a target="_blank" href="/wenshuDetail_com_0c8526ed93bc41331a0c8ed5526163f7.html"><h3 class="seo font-14">田砚荣与宁波上嘉人力资源服务有限公司、上海盒马网络科技有限公司等生命权、健康权、身体权纠纷一审民事判决书</h3></a></td> 
          <td width="103">生命权、健康权、身体权纠纷</td> 
          <td width="103" class="text-center">-</td> 
          <td width="103">2019-03-29</td> 
          <td width="12%">（2019）沪0109民初2917号</td> 
          <td width="16%"> 
           <div class="m-b-xs">
            原告 - 
            <a href="/search?key=%E7%94%B0%E7%A0%9A%E8%8D%A3" class="c_a" target="_blank">田砚荣</a>
           </div> 
           <div class="m-b-xs">
            被告 - 
            <a href="/search?key=%E6%96%B9%E5%BC%BA" class="c_a" target="_blank">方强</a>
           </div> 
           <div class="m-b-xs">
            被告 - 
            <a href="/search?key=%E5%AE%81%E6%B3%A2%E4%B8%8A%E5%98%89%E4%BA%BA%E5%8A%9B%E8%B5%84%E6%BA%90%E6%9C%8D%E5%8A%A1%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8" class="c_a" target="_blank">宁波上嘉人力资源服务有限公司</a>
           </div> 
           <div class="m-b-xs">
            被告 - 
            <a href="/search?key=%E4%B8%8A%E6%B5%B7%E7%9B%92%E9%A9%AC%E7%BD%91%E7%BB%9C%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8" class="c_a" target="_blank">上海盒马网络科技有限公司</a>
           </div> </td> 
          <td width="15%">上海市虹口区人民法院</td> 
         </tr> 
         <tr> 
          <td class="tx">3</td> 
          <td width=""><a target="_blank" href="/wenshuDetail_com_17913e009e395331c1723af177d5855b.html"><h3 class="seo font-14">曹慎之与上海盒马网络科技有限公司、宁波上嘉人力资源服务有限公司生命权、健康权、身体权纠纷一审民事判决书</h3></a></td> 
          <td width="103">生命权、健康权、身体权纠纷</td> 
          <td width="103" class="text-center">-</td> 
          <td width="103">2019-01-16</td> 
          <td width="12%">（2018）沪0104民初7700号</td> 
          <td width="16%"> 
           <div class="m-b-xs">
            原告 - 
            <a href="/search?key=%E6%9B%B9%E6%85%8E%E4%B9%8B" class="c_a" target="_blank">曹慎之</a>
           </div> 
           <div class="m-b-xs">
            被告 - 
            <a href="/search?key=%E4%B8%8A%E6%B5%B7%E7%9B%92%E9%A9%AC%E7%BD%91%E7%BB%9C%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8" class="c_a" target="_blank">上海盒马网络科技有限公司</a>
           </div> 
           <div class="m-b-xs">
            被告 - 
            <a href="/search?key=%E5%AE%81%E6%B3%A2%E4%B8%8A%E5%98%89%E4%BA%BA%E5%8A%9B%E8%B5%84%E6%BA%90%E6%9C%8D%E5%8A%A1%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8" class="c_a" target="_blank">宁波上嘉人力资源服务有限公司</a>
           </div> </td> 
          <td width="15%">上海市徐汇区人民法院</td> 
         </tr> 
         <tr> 
          <td class="tx">4</td> 
          <td width=""><a target="_blank" href="/wenshuDetail_com_f64a8c4823ef2f20619c89d2217d82eb.html"><h3 class="seo font-14">上海上嘉物流有限公司、上海盒马网络科技有限公司机动车交通事故责任纠纷一审民事裁定书</h3></a></td> 
          <td width="103">机动车交通事故责任纠纷</td> 
          <td width="103" class="text-center">-</td> 
          <td width="103">2018-12-28</td> 
          <td width="12%">（2018）京0108民初52810号</td> 
          <td width="16%"> - </td> 
          <td width="15%">北京市海淀区人民法院</td> 
         </tr> 
         <tr> 
          <td class="tx">5</td> 
          <td width=""><a target="_blank" href="/wenshuDetail_com_4b66e10c83db94543062b1aa8254dac6.html"><h3 class="seo font-14">沈正清与上海盒马网络科技有限公司、昆山力伟劳务派遣有限公司生命权、健康权、身体权纠纷一审民事判决书</h3></a></td> 
          <td width="103">生命权、健康权、身体权纠纷</td> 
          <td width="103" class="text-center">-</td> 
          <td width="103">2018-12-24</td> 
          <td width="12%">（2018）沪0106民初12235号</td> 
          <td width="16%"> 
           <div class="m-b-xs">
            原告 - 
            <a href="/search?key=%E6%B2%88%E6%AD%A3%E6%B8%85" class="c_a" target="_blank">沈正清</a>
           </div> 
           <div class="m-b-xs">
            代理律师事务所 - 
            <a href="/search?key=%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%90%8C%E5%BB%BA%E5%BE%8B%E5%B8%88%E4%BA%8B%E5%8A%A1%E6%89%80" class="c_a" target="_blank">上海市同建律师事务所</a>
           </div> 
           <div class="m-b-xs">
            被告 - 
            <a href="/search?key=%E4%B8%8A%E6%B5%B7%E7%9B%92%E9%A9%AC%E7%BD%91%E7%BB%9C%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8" class="c_a" target="_blank">上海盒马网络科技有限公司</a>
           </div> 
           <div class="m-b-xs">
            代理律师事务所 - 
            <a href="/search?key=%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%BE%8B%E5%92%8C%E7%90%86%E5%BE%8B%E5%B8%88%E4%BA%8B%E5%8A%A1%E6%89%80" class="c_a" target="_blank">上海市律和理律师事务所</a>
           </div> 
           <div class="m-b-xs">
            被告 - 
            <a href="/search?key=%E6%98%86%E5%B1%B1%E5%8A%9B%E4%BC%9F%E5%8A%B3%E5%8A%A1%E6%B4%BE%E9%81%A3%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8" class="c_a" target="_blank">昆山力伟劳务派遣有限公司</a>
           </div> </td> 
          <td width="15%">上海市静安区人民法院</td> 
         </tr> 
         <tr> 
          <td class="tx">6</td> 
          <td width=""><a target="_blank" href="/wenshuDetail_com_701ec9700f13149bda5b188aa68988e9.html"><h3 class="seo font-14">吴华强与上海盒马网络科技有限公司、上海环宇消防集团有限公司等提供劳务者受害责任纠纷一审民事判决书</h3></a></td> 
          <td width="103">提供劳务受害者责任纠纷</td> 
          <td width="103" class="text-center">-</td> 
          <td width="103">2018-11-20</td> 
          <td width="12%">（2018）沪0112民初13349号</td> 
          <td width="16%"> 
           <div class="m-b-xs">
            原告 - 
            <a href="/search?key=%E5%90%B4%E5%8D%8E%E5%BC%BA" class="c_a" target="_blank">吴华强</a>
           </div> 
           <div class="m-b-xs">
            代理律师事务所 - 
            <a href="/search?key=%E4%B8%8A%E6%B5%B7%E7%BF%B0%E6%B5%A9%E5%BE%8B%E5%B8%88%E4%BA%8B%E5%8A%A1%E6%89%80" class="c_a" target="_blank">上海翰浩律师事务所</a>
           </div> 
           <div class="m-b-xs">
            被告 - 
            <a href="/search?key=%E4%B8%8A%E6%B5%B7%E7%9B%92%E9%A9%AC%E7%BD%91%E7%BB%9C%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8" class="c_a" target="_blank">上海盒马网络科技有限公司</a>
           </div> 
           <div class="m-b-xs">
            代理律师事务所 - 
            <a href="/search?key=%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%BE%8B%E5%92%8C%E7%90%86%E5%BE%8B%E5%B8%88%E4%BA%8B%E5%8A%A1%E6%89%80" class="c_a" target="_blank">上海市律和理律师事务所</a>
           </div> 
           <div class="m-b-xs">
            被告 - 
            <a href="/search?key=%E4%B8%8A%E6%B5%B7%E7%8E%AF%E5%AE%87%E6%B6%88%E9%98%B2%E9%9B%86%E5%9B%A2%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8" class="c_a" target="_blank">上海环宇消防集团有限公司</a>
           </div> 
           <div class="m-b-xs">
            代理律师事务所 - 
            <a href="/search?key=%E4%B8%8A%E6%B5%B7%E5%8D%8E%E5%8B%A4%E5%9F%BA%E4%BF%A1%E5%BE%8B%E5%B8%88%E4%BA%8B%E5%8A%A1%E6%89%80" class="c_a" target="_blank">上海华勤基信律师事务所</a>
           </div> 
           <div class="m-b-xs">
            被告 - 
            <a href="/search?key=%E7%A7%A6%E5%85%89%E6%9D%83" class="c_a" target="_blank">秦光权</a>
           </div> </td> 
          <td width="15%">上海市闵行区人民法院</td> 
         </tr> 
         <tr> 
          <td class="tx">7</td> 
          <td width=""><a target="_blank" href="/wenshuDetail_com_37a472dbabe9a57d222dd15fdd814944.html"><h3 class="seo font-14">上海市杨浦区优芝面包房与上海波司登投资发展有限公司、嘉凯城集团商业资产管理有限公司等财产损害赔偿纠纷一审民事判决书</h3></a></td> 
          <td width="103">财产损害赔偿纠纷</td> 
          <td width="103" class="text-center">69495.85元</td> 
          <td width="103">2018-09-27</td> 
          <td width="12%">（2017）沪0110民初15372号</td> 
          <td width="16%"> 
           <div class="m-b-xs">
            原告 - 
            <a href="/search?key=%E4%B8%8A%E6%B5%B7%E5%B8%82%E6%9D%A8%E6%B5%A6%E5%8C%BA%E4%BC%98%E8%8A%9D%E9%9D%A2%E5%8C%85%E6%88%BF" class="c_a" target="_blank">上海市杨浦区优芝面包房</a>
           </div> 
           <div class="m-b-xs">
            代理律师事务所 - 
            <a href="/search?key=%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%8D%8E%E8%8D%A3%E5%BE%8B%E5%B8%88%E4%BA%8B%E5%8A%A1%E6%89%80" class="c_a" target="_blank">上海市华荣律师事务所</a>
           </div> 
           <div class="m-b-xs">
            被告 - 
            <a href="/search?key=%E4%B8%8A%E6%B5%B7%E6%B3%A2%E5%8F%B8%E7%99%BB%E6%8A%95%E8%B5%84%E5%8F%91%E5%B1%95%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8" class="c_a" target="_blank">上海波司登投资发展有限公司</a>
           </div> 
           <div class="m-b-xs">
            被告 - 
            <a href="/search?key=%E5%98%89%E5%87%AF%E5%9F%8E%E9%9B%86%E5%9B%A2%E5%95%86%E4%B8%9A%E8%B5%84%E4%BA%A7%E7%AE%A1%E7%90%86%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8" class="c_a" target="_blank">嘉凯城集团商业资产管理有限公司</a>
           </div> 
           <div class="m-b-xs">
            被告 - 
            <a href="/search?key=%E4%B8%8A%E6%B5%B7%E4%BC%A0%E5%AF%8C%E7%BD%91%E7%BB%9C%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8" class="c_a" target="_blank">上海传富网络科技有限公司</a>
           </div> 
           <div class="m-b-xs">
            代理律师事务所 - 
            <a href="/search?key=%E4%B8%8A%E6%B5%B7%E7%94%B3%E6%B5%A9%E5%BE%8B%E5%B8%88%E4%BA%8B%E5%8A%A1%E6%89%80" class="c_a" target="_blank">上海申浩律师事务所</a>
           </div> 
           <div class="m-b-xs">
            被告 - 
            <a href="/search?key=%E4%B8%8A%E6%B5%B7%E7%9B%92%E9%A9%AC%E7%BD%91%E7%BB%9C%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8" class="c_a" target="_blank">上海盒马网络科技有限公司</a>
           </div> 
           <div class="m-b-xs">
            代理律师事务所 - 
            <a href="/search?key=%E4%B8%8A%E6%B5%B7%E7%94%B3%E6%B5%A9%E5%BE%8B%E5%B8%88%E4%BA%8B%E5%8A%A1%E6%89%80" class="c_a" target="_blank">上海申浩律师事务所</a>
           </div> 
           <div class="m-b-xs">
            第三人 - 
            <a href="/search?key=%E4%B8%8A%E6%B5%B7%E5%AE%9D%E7%AB%8B%E5%BB%BA%E7%AD%91%E8%A3%85%E9%A5%B0%E5%B7%A5%E7%A8%8B%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8" class="c_a" target="_blank">上海宝立建筑装饰工程有限公司</a>
           </div> </td> 
          <td width="15%">上海市杨浦区人民法院</td> 
         </tr> 
         <tr> 
          <td class="tx">8</td> 
          <td width=""><a target="_blank" href="/wenshuDetail_com_24f8dff0e04267966427bed6efdfabc0.html"><h3 class="seo font-14">上海市杨浦区优芝面包房与上海盒马网络科技有限公司、上海波司登投资发展有限公司等财产损害赔偿纠纷二审民事判决书</h3></a></td> 
          <td width="103">财产损害赔偿纠纷</td> 
          <td width="103" class="text-center">-</td> 
          <td width="103">2018-09-27</td> 
          <td width="12%">（2018）沪02民终1968号</td> 
          <td width="16%"> 
           <div class="m-b-xs">
            上诉人（原审原告） - 
            <a href="/search?key=%E4%B8%8A%E6%B5%B7%E5%B8%82%E6%9D%A8%E6%B5%A6%E5%8C%BA%E4%BC%98%E8%8A%9D%E9%9D%A2%E5%8C%85%E6%88%BF" class="c_a" target="_blank">上海市杨浦区优芝面包房</a>
           </div> 
           <div class="m-b-xs">
            代理律师事务所 - 
            <a href="/search?key=%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%8D%8E%E8%8D%A3%E5%BE%8B%E5%B8%88%E4%BA%8B%E5%8A%A1%E6%89%80" class="c_a" target="_blank">上海市华荣律师事务所</a>
           </div> 
           <div class="m-b-xs">
            原审被告 - 
            <a href="/search?key=%E4%B8%8A%E6%B5%B7%E6%B3%A2%E5%8F%B8%E7%99%BB%E6%8A%95%E8%B5%84%E5%8F%91%E5%B1%95%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8" class="c_a" target="_blank">上海波司登投资发展有限公司</a>
           </div> 
           <div class="m-b-xs">
            原审被告 - 
            <a href="/search?key=%E5%98%89%E5%87%AF%E5%9F%8E%E9%9B%86%E5%9B%A2%E5%95%86%E4%B8%9A%E8%B5%84%E4%BA%A7%E7%AE%A1%E7%90%86%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8" class="c_a" target="_blank">嘉凯城集团商业资产管理有限公司</a>
           </div> 
           <div class="m-b-xs">
            原审被告 - 
            <a href="/search?key=%E4%B8%8A%E6%B5%B7%E4%BC%A0%E5%AF%8C%E7%BD%91%E7%BB%9C%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8" class="c_a" target="_blank">上海传富网络科技有限公司</a>
           </div> 
           <div class="m-b-xs">
            原审第三人 - 
            <a href="/search?key=%E4%B8%8A%E6%B5%B7%E5%AE%9D%E7%AB%8B%E5%BB%BA%E7%AD%91%E8%A3%85%E9%A5%B0%E5%B7%A5%E7%A8%8B%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8" class="c_a" target="_blank">上海宝立建筑装饰工程有限公司</a>
           </div> 
           <div class="m-b-xs">
            被上诉人（原审被告） - 
            <a href="/search?key=%E4%B8%8A%E6%B5%B7%E7%9B%92%E9%A9%AC%E7%BD%91%E7%BB%9C%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8" class="c_a" target="_blank">上海盒马网络科技有限公司</a>
           </div> 
           <div class="m-b-xs">
            代理律师事务所 - 
            <a href="/search?key=%E4%B8%8A%E6%B5%B7%E7%94%B3%E6%B5%A9%E5%BE%8B%E5%B8%88%E4%BA%8B%E5%8A%A1%E6%89%80" class="c_a" target="_blank">上海申浩律师事务所</a>
           </div> </td> 
          <td width="15%">上海市第二中级人民法院</td> 
         </tr> 
         <tr> 
          <td class="tx">9</td> 
          <td width=""><a target="_blank" href="/wenshuDetail_com_c8ea8d19cce5208ff0c9cf087dc62c5e.html"><h3 class="seo font-14">唐亚贞与上海盒马网络科技有限公司网络购物合同纠纷一审民事裁定书</h3></a></td> 
          <td width="103">网络购物纠纷</td> 
          <td width="103" class="text-center">-</td> 
          <td width="103">2018-08-02</td> 
          <td width="12%">（2018）沪0115民初17673号</td> 
          <td width="16%"> 
           <div class="m-b-xs">
            原告 - 
            <a href="/search?key=%E5%94%90%E4%BA%9A%E8%B4%9E" class="c_a" target="_blank">唐亚贞</a>
           </div> 
           <div class="m-b-xs">
            被告 - 
            <a href="/search?key=%E4%B8%8A%E6%B5%B7%E7%9B%92%E9%A9%AC%E7%BD%91%E7%BB%9C%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8" class="c_a" target="_blank">上海盒马网络科技有限公司</a>
           </div> </td> 
          <td width="15%">上海市浦东新区人民法院</td> 
         </tr> 
         <tr> 
          <td class="tx">10</td> 
          <td width=""><a target="_blank" href="/wenshuDetail_com_e020168c8e79e86b24620f9c17a04b68.html"><h3 class="seo font-14">阎家明与上海盒马网络科技有限公司买卖合同纠纷民事调解书</h3></a></td> 
          <td width="103">买卖合同纠纷</td> 
          <td width="103" class="text-center">-</td> 
          <td width="103">2018-06-30</td> 
          <td width="12%">（2017）沪0115民初34231号</td> 
          <td width="16%"> - </td> 
          <td width="15%">上海市浦东新区人民法院</td> 
         </tr> 
        </tbody>
       </table> 
       <div> 
        <nav class="text-right"> 
         <ul class="pagination"> 
          <li class="active"><a htef="#">1</a></li>
          <li><a id="ajaxpage" href="javascript:getTabList(2,&quot;susong&quot;,&quot;wenshu&quot;)">2</a></li>
          <li><a id="ajaxpage" href="javascript:getTabList(3,&quot;susong&quot;,&quot;wenshu&quot;)">3</a></li> 
          <li><a id="ajaxpage" href="javascript:getTabList(2,&quot;susong&quot;,&quot;wenshu&quot;)">&gt;</a></li> 
         </ul> 
        </nav> 
       </div> 
      </section> 
      <section class="panel b-a clear" id="noticelist"> 
       <div class="tcaption"> 
        <h3 class="title"> 开庭公告</h3> 
        <span class="tbadger">43</span> 
        <span class="watermark"></span> 
       </div> 
       <table class="ntable ntable-odd"> 
        <tbody>
         <tr>
          <th class="tx">序号</th>
          <th>案号</th>
          <th>开庭日期</th>
          <th>案由</th>
          <th>公诉人/原告/上诉人/申请人</th>
          <th>被告人/被告/被上诉人/被申请人</th>
         </tr> 
         <tr> 
          <td class="tx">1</td> 
          <td width="120"> <a class="text-primary" onclick="showRelatModal(&quot;ktnotice&quot;,&quot;99112f1c73dd8cde579014ebed8c30f25&quot;)">(2019)苏01民终3209号</a> </td> 
          <td width="103">2019-05-20 09:30</td> 
          <td width="130">侵害商标权纠纷</td> 
          <td width="205">魏金光</td> 
          <td>上海盒马网络科技有限公司南京第分公司 李雪桦</td> 
         </tr> 
         <tr> 
          <td class="tx">2</td> 
          <td width="120"> <a class="text-primary" onclick="showRelatModal(&quot;ktnotice&quot;,&quot;e68799c04449d9bfaceb768f0552bd155&quot;)">(2019)沪0112民初8604号</a> </td> 
          <td width="103">2019-05-08 15:00</td> 
          <td width="130">生命权、健康权、身体权纠纷</td> 
          <td width="205">钱宝珍</td> 
          <td>上海盒马网络科技有限公司 廖浪沙 上海通贤投资管理有限公司</td> 
         </tr> 
         <tr> 
          <td class="tx">3</td> 
          <td width="120"> <a class="text-primary" onclick="showRelatModal(&quot;ktnotice&quot;,&quot;c4deab7400e049997f7f11cf86c54da75&quot;)">(2018)沪0105民初23235号</a> </td> 
          <td width="103">2019-04-09 14:00</td> 
          <td width="130">机动车交通事故责任纠纷</td> 
          <td width="205">龚美环</td> 
          <td>上海盒马网络科技有限公司 昆山力伟劳务派遣有限公司宁波分公司 昆山力伟劳务派遣有限公司 曹胜</td> 
         </tr> 
         <tr> 
          <td class="tx">4</td> 
          <td width="120"> <a class="text-primary" onclick="showRelatModal(&quot;ktnotice&quot;,&quot;03d3b75560a326042078095bfb93a1b95&quot;)">(2019)沪0112民初2237号</a> </td> 
          <td width="103">2019-04-01 13:45</td> 
          <td width="130">机动车交通事故责任纠纷</td> 
          <td width="205">张洹</td> 
          <td>上海盒马网络科技有限公司 徐凯 宁波上嘉人力资源服务有限公司 中国人寿财产保险股份有限公司北京市分公司</td> 
         </tr> 
         <tr> 
          <td class="tx">5</td> 
          <td width="120"> <a class="text-primary" onclick="showRelatModal(&quot;ktnotice&quot;,&quot;e958aa030eb37642da4b79456c06d6d95&quot;)">(2019)沪0115民初11697号</a> </td> 
          <td width="103">2019-03-19 13:45</td> 
          <td width="130">提供劳务者受害责任纠纷</td> 
          <td width="205">徐吉全</td> 
          <td>上海盒马网络科技有限公司 宁波上嘉人力资源服务有限公司 宁波上嘉弘昇物流有限公司</td> 
         </tr> 
         <tr> 
          <td class="tx">6</td> 
          <td width="120"> <a class="text-primary" onclick="showRelatModal(&quot;ktnotice&quot;,&quot;4f0a6f66697cb0bfd2644c9218269ca75&quot;)">(2019)沪0106民初10224号</a> </td> 
          <td width="103">2019-03-18 10:00</td> 
          <td width="130">买卖合同纠纷</td> 
          <td width="205">夏雷</td> 
          <td>上海盒马网络科技有限公司 上海盒马网络科技有限公司静安第二分公司</td> 
         </tr> 
         <tr> 
          <td class="tx">7</td> 
          <td width="120"> <a class="text-primary" onclick="showRelatModal(&quot;ktnotice&quot;,&quot;710e1c219be8479ee8fb859fa9092ecc5&quot;)">(2018)沪0105民初17998号</a> </td> 
          <td width="103">2019-02-21 13:45</td> 
          <td width="130">生命权、健康权、身体权纠纷</td> 
          <td width="205">李福兰</td> 
          <td>闫旭 上海盒马网络科技有限公司 益服企业管理(上海)有限公司 上海盒马网络科技有限公司闵行分公司</td> 
         </tr> 
         <tr> 
          <td class="tx">8</td> 
          <td width="120"> <a class="text-primary" onclick="showRelatModal(&quot;ktnotice&quot;,&quot;1acee38ae477413234408c426899e3895&quot;)">(2019)沪0115民初1432号</a> </td> 
          <td width="103">2019-02-18 09:15</td> 
          <td width="130">生命权、健康权、身体权纠纷</td> 
          <td width="205">郑瑞</td> 
          <td>上海盒马网络科技有限公司 昂纳科技有限公司 代单林</td> 
         </tr> 
         <tr> 
          <td class="tx">9</td> 
          <td width="120"> <a class="text-primary" onclick="showRelatModal(&quot;ktnotice&quot;,&quot;281509d04986f96dcd93b1d3e0c6143d5&quot;)">(2018)沪0115民初92469号</a> </td> 
          <td width="103">2019-01-21 13:30</td> 
          <td width="130">生命权、健康权、身体权纠纷</td> 
          <td width="205">孟彩萍</td> 
          <td>张雷 上海盒马网络科技有限公司浦东第一分公司 上海盒马网络科技有限公司 上海庆楷实业有限公司</td> 
         </tr> 
         <tr> 
          <td class="tx">10</td> 
          <td width="120"> <a class="text-primary" onclick="showRelatModal(&quot;ktnotice&quot;,&quot;7b9c6127bdc25766c2685312506844825&quot;)">(2018)沪0115民初91806号</a> </td> 
          <td width="103">2019-01-14 13:45</td> 
          <td width="130">产品责任纠纷</td> 
          <td width="205">朱利达</td> 
          <td>上海盒马网络科技有限公司</td> 
         </tr> 
        </tbody>
       </table> 
       <div> 
        <nav class="text-right"> 
         <ul class="pagination"> 
          <li class="active"><a htef="#">1</a></li>
          <li><a id="ajaxpage" href="javascript:getTabList(2,&quot;susong&quot;,&quot;notice&quot;)">2</a></li>
          <li><a id="ajaxpage" href="javascript:getTabList(3,&quot;susong&quot;,&quot;notice&quot;)">3</a></li>
          <li><a id="ajaxpage" href="javascript:getTabList(4,&quot;susong&quot;,&quot;notice&quot;)">4</a></li>
          <li><a id="ajaxpage" href="javascript:getTabList(5,&quot;susong&quot;,&quot;notice&quot;)">5</a></li> 
          <li><a id="ajaxpage" href="javascript:getTabList(2,&quot;susong&quot;,&quot;notice&quot;)">&gt;</a></li> 
         </ul> 
        </nav> 
       </div> 
      </section> 
      <div class="modal fade" id="dnoticeModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> 
       <div class="modal-dialog nmodal"> 
        <div class="modal-content"> 
         <div class="modal-header"> 
          <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> 
          <h4 class="modal-title">送达公告详情</h4> 
         </div> 
         <div class="modal-body"></div> 
        </div> 
       </div> 
      </div> 
      <div class="modal fade" id="assistanceModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> 
       <div class="modal-dialog nmodal"> 
        <div class="modal-content"> 
         <div class="modal-header"> 
          <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> 
          <h4 class="modal-title" id="myModalLabel">司法协助详情</h4> 
         </div> 
         <div class="modal-body"> 
          <div id="xzxkview"></div> 
         </div> 
        </div> 
       </div> 
      </div> 
      <div class="modal fade" id="lianModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> 
       <div class="modal-dialog nmodal"> 
        <div class="modal-content"> 
         <div class="modal-header"> 
          <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> 
          <h4 class="modal-title" id="myModalLabel">立案信息详情</h4> 
         </div> 
         <div class="modal-body"> 
          <div id="lianview"></div> 
         </div> 
        </div> 
       </div> 
      </div> 
      <section class="panel b-a clear"> 
       <div class="m_ptsc" style="padding:20px 0;">
        数据来源：中国裁判文书网、中国执行信息公开网、中华人民共和国最高人民法院、人民法院公告网、各地方人民法院。
       </div> 
      </section> 
      <script type="text/javascript" src="/material/theme/chacha/cms/v2/js/judgeChart.js?time=1557743995"></script> 
      <script type="text/javascript">

    function hideChart(dom){
    	if($(dom).find('i').hasClass('i-arrow-up4')){
    		$(dom).find('i').removeClass('i-arrow-up4');
    		$(dom).find('i').addClass('i-arrow-down4')
    		$(dom).find('span').html('展开');
    		$(dom).parent().next().hide();
    	}else{
    		$(dom).find('i').removeClass('i-arrow-down4');
    		$(dom).find('i').addClass('i-arrow-up4')
    		$(dom).find('span').html('收起');
    		$(dom).parent().next().show();
    	}
    	
    }



    $(function(){
    	var zhixing  = JSON.parse('[]');
	    var shixin  = JSON.parse('[]');
	    var wenshuList  = JSON.parse('[{"key":"casetype","items":[{"value":"ms","count":23,"desc":"\u6c11\u4e8b\u6848\u4ef6"},{"desc":"\u5176\u4ed6","count":7,"value":"other"}]},{"key":"province","items":[{"value":"BJ","count":1,"desc":"\u5317\u4eac"},{"value":"SH","count":29,"desc":"\u4e0a\u6d77"}]},{"key":"submityear","items":[{"value":"2019","count":3,"desc":"2019"},{"value":"2018","count":26,"desc":"2018"},{"value":"2017","count":1,"desc":"2017"}]},{"key":"courtlevel","items":[{"value":"3","count":3,"desc":"\u4e2d\u7ea7\u6cd5\u9662"},{"value":"2","count":25,"desc":"\u57fa\u5c42\u6cd5\u9662"},{"value":"1","count":2,"desc":"\u5176\u4ed6"}]},{"key":"courtmonth","items":[{"value":"201905","count":1,"desc":"2019\u5e745\u6708"},{"value":"201903","count":1,"desc":"2019\u5e743\u6708"},{"value":"201901","count":1,"desc":"2019\u5e741\u6708"},{"value":"201812","count":2,"desc":"2018\u5e7412\u6708"},{"value":"201811","count":1,"desc":"2018\u5e7411\u6708"},{"value":"201809","count":2,"desc":"2018\u5e749\u6708"},{"value":"201808","count":1,"desc":"2018\u5e748\u6708"},{"value":"201806","count":7,"desc":"2018\u5e746\u6708"}]},{"key":"casereasontype","items":[{"value":"0418","count":16,"desc":"\u4e70\u5356\u5408\u540c\u7ea0\u7eb7"},{"value":"0016","count":4,"desc":"\u751f\u547d\u6743\u3001\u5065\u5eb7\u6743\u3001\u8eab\u4f53\u6743\u7ea0\u7eb7"},{"value":"0029","count":3,"desc":"\u8d22\u4ea7\u635f\u5bb3\u8d54\u507f\u7ea0\u7eb7"},{"value":"0124","count":3,"desc":"\u7f51\u7edc\u8d2d\u7269\u7ea0\u7eb7"},{"value":"0001","count":2,"desc":"\u6c11\u95f4\u501f\u8d37\u7ea0\u7eb7"},{"value":"0003","count":1,"desc":"\u673a\u52a8\u8f66\u4ea4\u901a\u4e8b\u6545\u8d23\u4efb\u7ea0\u7eb7"},{"value":"0028","count":1,"desc":"\u63d0\u4f9b\u52b3\u52a1\u53d7\u5bb3\u8005\u8d23\u4efb\u7ea0\u7eb7"}]},{"key":"participant","items":[{"value":"d","count":27,"desc":"\u88ab\u544a"}]},{"key":"lawsuitresult","items":[{"value":"C","count":8,"desc":"\u64a4\u8bc9"},{"value":"L","count":2,"desc":"\u8d25\u8bc9"},{"value":"N","count":3,"desc":"\u5176\u4ed6"},{"value":"W","count":8,"desc":"\u80dc\u8bc9"}]}]');
	    var gonggaoList  = JSON.parse('null');
	    var noticeList  = JSON.parse('[{"Key":"courtyear","Items":[{"Desc":"2017","Value":"2017","Count":"9"},{"Desc":"2018","Value":"2018","Count":"23"},{"Desc":"2019","Value":"2019","Count":"11"}],"key":"courtyear","items":[{"Desc":"2017","Value":"2017","Count":"9","count":"9","desc":"2017","value":"2017"},{"Desc":"2018","Value":"2018","Count":"23","count":"23","desc":"2018","value":"2018"},{"Desc":"2019","Value":"2019","Count":"11","count":"11","desc":"2019","value":"2019"}]},{"Key":"province","Items":[{"Desc":"\u6c5f\u82cf","Value":"JS","Count":"1"},{"Desc":"\u4e0a\u6d77","Value":"SH","Count":"42"}],"key":"province","items":[{"Desc":"\u6c5f\u82cf","Value":"JS","Count":"1","count":"1","desc":"\u6c5f\u82cf","value":"JS"},{"Desc":"\u4e0a\u6d77","Value":"SH","Count":"42","count":"42","desc":"\u4e0a\u6d77","value":"SH"}]},{"Key":"risklevel","Items":[{"Desc":"","Value":"0","Count":"42"},{"Desc":"","Value":"3","Count":"1"}],"key":"risklevel","items":[{"Desc":"","Value":"0","Count":"42","count":"42","desc":"","value":"0"},{"Desc":"","Value":"3","Count":"1","count":"1","desc":"","value":"3"}]}]');


	    var provinceList = [];
	    var yearData = {
	    	xData:[],
	    	yDatas:[]
	    };

	    function drawSusongChart(){
	    	if(zhixing && zhixing.length>0){
		    	addProvince(zhixing[0]);
		    	countYear(zhixing[2],'被执行人信息');
		    }
		    if(shixin && shixin.length>0){
		    	addProvince(shixin[0]);
		    	countYear(shixin[2],'失信被执行人');
		    }
		    if(wenshuList && wenshuList.length>0){
		    	addProvince(wenshuList[1]);
		    	countYear(wenshuList[2],'裁判文书');
		    }
		    if(gonggaoList && gonggaoList.length>0){
		    	addProvince(gonggaoList[0]);
		    	countYear(gonggaoList[1],'法院公告');
		    }
		    if(noticeList && noticeList.length>0){
		    	addProvince(noticeList[1]);
		    	countYear(noticeList[0],'开庭公告');
		    }

		    yearData.xData.sort(function (a, b) {
		        var pa = 0;
		    	var pb = 0;
		    	if(a!='未知'){
		    		pa = parseInt(a);
		    	}
		    	if(b!='未知'){
		    		pb = parseInt(b);
		    	}
	            return pa - pb;
	        });

		    var unknown = null;
	        yearData.xData.forEach(function (data,index) {
				if(data == '未知'){
	                unknown = data;
	                yearData.xData.splice(index,1);
				}
	        });
	        if(unknown){
	            yearData.xData.push(unknown);
			}

		    if(zhixing && zhixing.length>0){
		    	kateYear(zhixing[2],'被执行人信息');
		    }
		    if(shixin && shixin.length>0){
		    	kateYear(shixin[2],'失信被执行人');
		    }
		    if(wenshuList && wenshuList.length>0){
		    	kateYear(wenshuList[2],'裁判文书');
		    }
		    if(gonggaoList && gonggaoList.length>0){
		    	kateYear(gonggaoList[1],'法院公告');
		    }
		    if(noticeList && noticeList.length>0){
		    	kateYear(noticeList[0],'开庭公告');
		    }

		    var yearDataStr = '{"xData":["2015","2016","2017"],"yDatas":[{"name":"被执行人信息","index":0,"value":[3,3,4]},{"name":"失信被执行人","index":1,"value":[1,3,3]},{"name":"裁判文书","index":2,"value":[5,6,2]},{"name":"法院公告","index":3,"value":[3,5,2]}]}'


		    chartUtil.drawMap(provinceList,"susong-province",1,'法律诉讼省份分布');

		    chartUtil.drawBarMuti(yearData,"susong-year",1,'法律诉讼年份分布');
	    }
	    

	    function addProvince(list){
	    	if(list && list.items){
	    		list.items.forEach(function(obj){
		    		var province = containsProvince(provinceList,obj);
		    		if(!province){
		    			provinceList.push({
		    			value: parseInt(obj.count),
	                	name: obj.desc,
		    		})
		    		}else{
		    			province.value+=parseInt(obj.count);
		    		}
		    		
		    	})
	    	}else{

	    	}
	    	
	    	
	    }

	    function containsProvince(provinceList,obj){
	    	for(var i=0;i<provinceList.length;i++){
	    		if(provinceList[i].name==obj.desc){
	    			return provinceList[i];
	    		}
	    	}
	    	return null;
	    }

	    function countYear(list,title){
	    	if(!list || !list.items){
	    		return;
	    	} 
	    	list.items.forEach(function(obj){
	    		var year = containsYear(yearData.xData,obj);
	    		if(!year){
	    			if(obj.value==""){
	    				obj.value="未知"
	    			}
	    			yearData.xData.push(obj.value)
	    			
	    		}
	    	});
	    	yearData.yDatas.push({
	    		name:title,
	    		index:yearData.yDatas.length,
	    		value:[]
	    	});
	    	
	    }

	    

	    function containsYear(yearList,obj){
	    	for(var i=0;i<yearList.length;i++){
	    		if(yearList[i]==obj.value){
	    			return yearList[i];
	    		}
	    	}
	    	return null;
	    }

	    function kateYear(list,title){
	    	var index = getIndex(title,yearData.yDatas);
	    	yearData.xData.forEach(function(year){
	    		if(list.items){
	    			var item = containsYear2(list.items,year);
	    			if(item){
	    				yearData.yDatas[index].value.push(item.count);
		    		}else{
		    			yearData.yDatas[index].value.push(0);
		    		}
	    		}
		    		
	    	});
	    }

	    function containsYear2(yearList,year){
	    	for(var i=0;i<yearList.length;i++){
	    		if(yearList[i].value==year){
	    			return yearList[i];
	    		}
	    	}
	    	return null;
	    }

	    function getIndex(title,yDatas){
	    	for(var i=0;i<yDatas.length;i++){
	    		if(yDatas[i].name==title){
	    			return yDatas[i].index;
	    		}
	    	}
	    }



	    $('.chooseSusong').find('a').on('click',function(){
            var targetDiv = $(this).parent().parent().parent().parent();
            var target = targetDiv.attr('data-box');
            var optionArr = ['casetype','casereason'];
            var hiddenName = '';
            var hiddenValue = '';
            var ajaxData = {};
            ajaxData['box'] = 'wenshu';
            var option = $(this).attr('data-option');
            //option = target + option;
            var value = $(this).attr('data-value');
            var text = $(this).text();
            var textArr = text.split('(');
            $("input[name=" + option + "]").val(value);

            $("input[name=" + option + "]").attr('data-desc',textArr[0]);
            //取所有筛选条件的值
            for(var i=0;i<optionArr.length;i++){
                hiddenName = optionArr[i];
                hiddenValue = $("input[name=" + hiddenName + "]").val();
                ajaxData[hiddenName] = hiddenValue;
            }
            //拼接其他参数
            ajaxData['unique'] = $("#unique").val();
            ajaxData['companyname'] = $("#companyname").val();
            ajaxData['tab'] = 'susong';
            ajaxData['p'] = '1';
            getTabListNew(ajaxData);
        });
        
	            judgeChart(wenshuList);
        
        	    drawSusongChart();
	        });

		
      
    </script> 
     </div> 
     <div class="data_div" id="report_div" style="display: none;">
      <div class="report_info"></div> 
      <style>
#loadReport{
   text-align:center;
   margin-top:100px;
   display:none;
}
</style> 
      <section class="panel b-a clear m_dataTab"> 
       <div class="panel-body"> 
        <a href="javascript:;" onclick="boxScrollNew('#report');zhugeTrack('企业主页-企业发展-企业年报',{'企业名称':'上海盒马网络科技有限公司'});" class="btn btn-sm btn-default  m-r-sm" style="white-space:nowrap;"> 企业年报&nbsp;3 </a> 
        <a href="javascript:;" onclick="boxScrollNew('#financingInfo');zhugeTrack('企业主页-企业发展-融资信息',{'企业名称':'上海盒马网络科技有限公司'});" class="btn btn-sm btn-default  m-r-sm" style="white-space:nowrap;"> 融资信息&nbsp;1 </a> 
        <a href="javascript:;" class="btn btn-sm btn-default  m-r-sm c_disable" style="white-space:nowrap;cursor: default"> 投资机构&nbsp;0 </a> 
        <a href="javascript:;" onclick="boxScrollNew('#memberInfo');zhugeTrack('企业主页-企业发展-核心人员',{'企业名称':'上海盒马网络科技有限公司'});" class="btn btn-sm btn-default  m-r-sm" style="white-space:nowrap;"> 核心人员&nbsp;1 </a> 
        <a href="javascript:;" onclick="boxScrollNew('#productInfo');zhugeTrack('企业主页-企业发展-企业业务',{'企业名称':'上海盒马网络科技有限公司'});" class="btn btn-sm btn-default  m-r-sm" style="white-space:nowrap;"> 企业业务&nbsp;1 </a> 
        <a href="javascript:;" onclick="boxScrollNew('#compatProductInfo');zhugeTrack('企业主页-企业发展-竞品信息',{'企业名称':'上海盒马网络科技有限公司'});" class="btn btn-sm btn-default  m-r-sm" style="white-space:nowrap;"> 竞品信息&nbsp;13 </a> 
        <a href="javascript:;" class="btn btn-sm btn-default  m-r-sm c_disable" style="white-space:nowrap;cursor: default"> 私募基金 </a> 
       </div> 
      </section> 
      <section class="panel b-a" id="report"> 
       <div class="tcaption"> 
        <span class="title">企业年报</span> 
        <span class="tbadge">3</span> 
        <div class="chooseReport" data-box="report" style="float: right"> 
         <div class="tdrop"> 
          <a class="btn m-l-xs a" href="#0" data-toggle="tab" onclick="changeReportTab(this,1);zhugeTrack('企业主页-企业年报',{'企业名称':'上海盒马网络科技有限公司'});"> 2017年 </a> 
          <a class="btn m-l-xs " href="#1" data-toggle="tab" onclick="changeReportTab(this,1);zhugeTrack('企业主页-企业年报',{'企业名称':'上海盒马网络科技有限公司'});"> 2016年 </a> 
          <a class="btn m-l-xs " href="#2" data-toggle="tab" onclick="changeReportTab(this,1);zhugeTrack('企业主页-企业年报',{'企业名称':'上海盒马网络科技有限公司'});"> 2015年 </a> 
         </div> 
        </div> 
        <span class="watermark"></span> 
       </div> 
       <div class="tab-content"> 
        <div class="tab-pane fade in active" id="0"> 
         <div class="tcaption"> 
          <h3 class="subtitle">企业基本信息</h3> 
          <span class="pull-right text-gray">2018-06-12&nbsp;公布</span> 
         </div> 
         <table class="ntable"> 
          <tbody> 
           <tr> 
            <td class="tb" width="20%">注册号</td> 
            <td width="30%">310141000157096</td> 
            <td class="tb" width="20%">统一社会信用代码</td> 
            <td width="30%">91310115342050446K</td> 
           </tr> 
           <tr> 
            <td class="tb" width="20%">企业经营状态</td> 
            <td width="30%">开业</td> 
            <td class="tb" width="20%">企业联系电话</td> 
            <td width="25%">021-38565188</td> 
           </tr> 
           <tr> 
            <td class="tb" width="20%">从业人数 </td> 
            <td width="25%">企业选择不公示</td> 
            <td class="tb" width="20%">邮政编码</td> 
            <td width="25%">200042</td> 
           </tr> 
           <tr> 
            <td class="tb" width="20%">有限责任公司本年度是否发生股东股权转让</td> 
            <td>否</td> 
            <td class="tb" width="20%">企业是否有投资信息或购买其他公司股权</td> 
            <td colspan="3">否</td> 
           </tr> 
           <tr> 
            <td class="tb" width="20%">电子邮箱</td> 
            <td colspan="3"><a href="mailto:不公示" style="color:#555;">不公示</a></td> 
           </tr> 
           <tr> 
            <td class="tb" width="20%">企业通讯地址</td> 
            <td colspan="3"><a onclick="showMapModal('上海市长宁区长宁路88号KING88广场8、9楼','')">上海市长宁区长宁路88号KING88广场8、9楼</a></td> 
           </tr> 
          </tbody> 
         </table> 
         <div class="tcaption">
          <h3 class="subtitle">股东（发起人）出资信息</h3>
          <span class="watermark"></span>
         </div> 
         <table class="ntable ntable-odd ntable-stext"> 
          <tbody> 
           <tr> 
            <th class="tx">序号</th> 
            <th>发起人</th> 
            <th>认缴出资额(万元)</th> 
            <th>认缴出资时间</th> 
            <th>认缴出资方式 </th> 
            <th>实缴出资额(万元)</th> 
            <th>实缴出资时间</th> 
            <th>实缴出资方式</th> 
           </tr> 
           <tr> 
            <td class="tx">1</td> 
            <td class="text-center"> <a href="/firm_hcb57b19bc9cd13855cfb774959b8730.html" target="_blank">Hema (Hong Kong) Limited</a> </td> 
            <td width="125" class="text-center">64913</td> 
            <td width="100" class="text-center">2016-09-19</td> 
            <td width="100" class="text-center">货币</td> 
            <td width="125" class="text-center">34638.5</td> 
            <td width="100" class="text-center">2016-11-15</td> 
            <td width="100" class="text-center">货币</td> 
           </tr> 
          </tbody> 
         </table> 
         <div class="tcaption">
          <h3 class="subtitle">企业资产状况信息</h3>
          <span class="watermark"></span>
         </div> 
         <table class="ntable"> 
          <tbody>
           <tr> 
            <td class="tb" width="20%">资产总额</td> 
            <td>企业选择不公示</td> 
            <td class="tb" width="20%">所有者权益合计</td> 
            <td>企业选择不公示</td> 
           </tr> 
           <tr> 
            <td class="tb">营业总收入 </td> 
            <td>企业选择不公示</td> 
            <td class="tb">利润总额 </td> 
            <td>企业选择不公示</td> 
           </tr> 
           <tr> 
            <td class="tb">营业总收入中主营业务收入 </td> 
            <td>企业选择不公示</td> 
            <td class="tb">净利润 </td> 
            <td>企业选择不公示</td> 
           </tr> 
           <tr> 
            <td class="tb">纳税总额 </td> 
            <td>企业选择不公示</td> 
            <td class="tb">负债总额 </td> 
            <td>企业选择不公示</td> 
           </tr> 
          </tbody>
         </table> 
         <div class="tcaption">
          <h3 class="subtitle">社保信息</h3>
          <span class="watermark"></span>
         </div> 
         <table class="ntable"> 
          <tbody> 
           <tr> 
            <td class="tb" width="22%">城镇职工基本养老保险</td> 
            <td width="30%">337人</td> 
            <td class="tb" width="20%">职工基本医疗保险</td> 
            <td width="30%">337人</td> 
           </tr> 
           <tr> 
            <td class="tb" width="20%">生育保险</td> 
            <td width="25%">336人</td> 
            <td class="tb" width="20%">失业保险</td> 
            <td width="30%">337人</td> 
           </tr> 
           <tr> 
            <td class="tb" width="20%">工伤保险</td> 
            <td width="25%" colspan="3">337人</td> 
           </tr> 
           <tr> 
            <td class="tb" width="20%" rowspan="5">单位缴纳基数</td> 
            <td width="30%">单位参加城镇职工基本养老保险缴费基数</td> 
            <td width="30%" colspan="2">企业选择不公示</td> 
           </tr> 
           <tr> 
            <td width="30%">单位参加失业保险缴费基数</td> 
            <td width="30%" colspan="2">企业选择不公示</td> 
           </tr> 
           <tr> 
            <td width="30%">单位参加职工基本医疗保险缴费基数</td> 
            <td width="30%" colspan="2">企业选择不公示</td> 
           </tr> 
           <tr> 
            <td width="30%">单位参加工伤保险缴费基数</td> 
            <td width="30%" colspan="2">-</td> 
           </tr> 
           <tr> 
            <td width="30%">单位参加生育保险缴费基数</td> 
            <td width="30%" colspan="2">企业选择不公示</td> 
           </tr> 
           <tr> 
            <td class="tb" width="20%" rowspan="5">本期实际缴费金额</td> 
            <td width="40%">参加城镇职工基本养老保险本期实际缴费金额</td> 
            <td width="30%" colspan="2">企业选择不公示</td> 
           </tr> 
           <tr> 
            <td width="30%">参加失业保险本期实际缴费金额</td> 
            <td width="30%" colspan="2">企业选择不公示</td> 
           </tr> 
           <tr> 
            <td width="30%">参加职工基本医疗保险本期实际缴费金额</td> 
            <td width="30%" colspan="2">企业选择不公示</td> 
           </tr> 
           <tr> 
            <td width="30%">参加工伤保险本期实际缴费金额</td> 
            <td width="30%" colspan="2">企业选择不公示</td> 
           </tr> 
           <tr> 
            <td width="30%">参加生育保险本期实际缴费金额</td> 
            <td width="30%" colspan="2">企业选择不公示</td> 
           </tr> 
           <tr> 
            <td class="tb" width="20%" rowspan="5">单位累计欠缴金额</td> 
            <td width="30%">单位参加城镇职工基本养老保险累计欠缴金额</td> 
            <td width="30%" colspan="2">企业选择不公示</td> 
           </tr> 
           <tr> 
            <td width="30%">单位参加失业保险累计欠缴金额</td> 
            <td width="30%" colspan="2">企业选择不公示</td> 
           </tr> 
           <tr> 
            <td width="30%">单位参加职工基本医疗保险累计欠缴金额</td> 
            <td width="30%" colspan="2">企业选择不公示</td> 
           </tr> 
           <tr> 
            <td width="30%">单位参加工伤保险累计欠缴金额</td> 
            <td width="30%" colspan="2">企业选择不公示</td> 
           </tr> 
           <tr> 
            <td width="30%">单位参加生育保险累计欠缴金额</td> 
            <td width="30%" colspan="2">企业选择不公示</td> 
           </tr> 
          </tbody> 
         </table> 
        </div> 
        <div class="tab-pane fade in " id="1"> 
         <div class="tcaption"> 
          <h3 class="subtitle">企业基本信息</h3> 
          <span class="pull-right text-gray">2017-06-13&nbsp;公布</span> 
         </div> 
         <table class="ntable"> 
          <tbody> 
           <tr> 
            <td class="tb" width="20%">注册号</td> 
            <td width="30%">-</td> 
            <td class="tb" width="20%">统一社会信用代码</td> 
            <td width="30%">91310115342050446K</td> 
           </tr> 
           <tr> 
            <td class="tb" width="20%">企业经营状态</td> 
            <td width="30%">开业</td> 
            <td class="tb" width="20%">企业联系电话</td> 
            <td width="25%">021-38565188</td> 
           </tr> 
           <tr> 
            <td class="tb" width="20%">从业人数 </td> 
            <td width="25%">-</td> 
            <td class="tb" width="20%">邮政编码</td> 
            <td width="25%">200042</td> 
           </tr> 
           <tr> 
            <td class="tb" width="20%">有限责任公司本年度是否发生股东股权转让</td> 
            <td>是</td> 
            <td class="tb" width="20%">企业是否有投资信息或购买其他公司股权</td> 
            <td colspan="3">否</td> 
           </tr> 
           <tr> 
            <td class="tb" width="20%">电子邮箱</td> 
            <td colspan="3"><a href="mailto:不公示" style="color:#555;">不公示</a></td> 
           </tr> 
           <tr> 
            <td class="tb" width="20%">企业通讯地址</td> 
            <td colspan="3"><a onclick="showMapModal('上海市长宁区长宁路88号KING88广场8、9楼','')">上海市长宁区长宁路88号KING88广场8、9楼</a></td> 
           </tr> 
          </tbody> 
         </table> 
         <div class="tcaption">
          <h3 class="subtitle">股东（发起人）出资信息</h3>
          <span class="watermark"></span>
         </div> 
         <table class="ntable ntable-odd ntable-stext"> 
          <tbody> 
           <tr> 
            <th class="tx">序号</th> 
            <th>发起人</th> 
            <th>认缴出资额(万元)</th> 
            <th>认缴出资时间</th> 
            <th>认缴出资方式 </th> 
            <th>实缴出资额(万元)</th> 
            <th>实缴出资时间</th> 
            <th>实缴出资方式</th> 
           </tr> 
           <tr> 
            <td class="tx">1</td> 
            <td class="text-center"> <a href="/firm_hcb57b19bc9cd13855cfb774959b8730.html" target="_blank">Hema (Hong Kong) Limited</a> </td> 
            <td width="125" class="text-center">64913</td> 
            <td width="100" class="text-center">2016-09-19</td> 
            <td width="100" class="text-center">货币</td> 
            <td width="125" class="text-center">34638.5</td> 
            <td width="100" class="text-center">2016-11-15</td> 
            <td width="100" class="text-center">货币</td> 
           </tr> 
          </tbody> 
         </table> 
         <div class="tcaption">
          <h3 class="subtitle">企业资产状况信息</h3>
          <span class="watermark"></span>
         </div> 
         <table class="ntable"> 
          <tbody>
           <tr> 
            <td class="tb" width="20%">资产总额</td> 
            <td>企业选择不公示</td> 
            <td class="tb" width="20%">所有者权益合计</td> 
            <td>企业选择不公示</td> 
           </tr> 
           <tr> 
            <td class="tb">营业总收入 </td> 
            <td>企业选择不公示</td> 
            <td class="tb">利润总额 </td> 
            <td>企业选择不公示</td> 
           </tr> 
           <tr> 
            <td class="tb">营业总收入中主营业务收入 </td> 
            <td>企业选择不公示</td> 
            <td class="tb">净利润 </td> 
            <td>企业选择不公示</td> 
           </tr> 
           <tr> 
            <td class="tb">纳税总额 </td> 
            <td>企业选择不公示</td> 
            <td class="tb">负债总额 </td> 
            <td>企业选择不公示</td> 
           </tr> 
          </tbody>
         </table> 
         <div class="tcaption">
          <h3 class="subtitle">股权变更信息</h3>
          <span class="watermark"></span>
         </div> 
         <table class="ntable ntable-odd"> 
          <tbody> 
           <tr> 
            <th class="tx">序号</th> 
            <th>股东</th> 
            <th>变更前股权比例</th> 
            <th>变更后股权比例</th> 
            <th>股权变更日期</th> 
           </tr> 
           <tr> 
            <td class="tx">1</td> 
            <td>Hema (Hong Kong) Limited</td> 
            <td width="130" class="text-center">0.0%</td> 
            <td width="130" class="text-center">100.0%</td> 
            <td width="130" class="text-center">2016-09-19</td> 
           </tr> 
          </tbody> 
         </table> 
         <div class="tcaption">
          <h3 class="subtitle">社保信息</h3>
          <span class="watermark"></span>
         </div> 
         <table class="ntable"> 
          <tbody> 
           <tr> 
            <td class="tb" width="22%">城镇职工基本养老保险</td> 
            <td width="30%">0 人</td> 
            <td class="tb" width="20%">职工基本医疗保险</td> 
            <td width="30%">0 人</td> 
           </tr> 
           <tr> 
            <td class="tb" width="20%">生育保险</td> 
            <td width="25%">0 人</td> 
            <td class="tb" width="20%">失业保险</td> 
            <td width="30%">0 人</td> 
           </tr> 
           <tr> 
            <td class="tb" width="20%">工伤保险</td> 
            <td width="25%" colspan="3">0 人</td> 
           </tr> 
           <tr> 
            <td class="tb" width="20%" rowspan="5">单位缴纳基数</td> 
            <td width="30%">单位参加城镇职工基本养老保险缴费基数</td> 
            <td width="30%" colspan="2">选择不公示</td> 
           </tr> 
           <tr> 
            <td width="30%">单位参加失业保险缴费基数</td> 
            <td width="30%" colspan="2">选择不公示</td> 
           </tr> 
           <tr> 
            <td width="30%">单位参加职工基本医疗保险缴费基数</td> 
            <td width="30%" colspan="2">选择不公示</td> 
           </tr> 
           <tr> 
            <td width="30%">单位参加工伤保险缴费基数</td> 
            <td width="30%" colspan="2">-</td> 
           </tr> 
           <tr> 
            <td width="30%">单位参加生育保险缴费基数</td> 
            <td width="30%" colspan="2">选择不公示</td> 
           </tr> 
           <tr> 
            <td class="tb" width="20%" rowspan="5">本期实际缴费金额</td> 
            <td width="40%">参加城镇职工基本养老保险本期实际缴费金额</td> 
            <td width="30%" colspan="2">选择不公示</td> 
           </tr> 
           <tr> 
            <td width="30%">参加失业保险本期实际缴费金额</td> 
            <td width="30%" colspan="2">选择不公示</td> 
           </tr> 
           <tr> 
            <td width="30%">参加职工基本医疗保险本期实际缴费金额</td> 
            <td width="30%" colspan="2">选择不公示</td> 
           </tr> 
           <tr> 
            <td width="30%">参加工伤保险本期实际缴费金额</td> 
            <td width="30%" colspan="2">选择不公示</td> 
           </tr> 
           <tr> 
            <td width="30%">参加生育保险本期实际缴费金额</td> 
            <td width="30%" colspan="2">选择不公示</td> 
           </tr> 
           <tr> 
            <td class="tb" width="20%" rowspan="5">单位累计欠缴金额</td> 
            <td width="30%">单位参加城镇职工基本养老保险累计欠缴金额</td> 
            <td width="30%" colspan="2">选择不公示</td> 
           </tr> 
           <tr> 
            <td width="30%">单位参加失业保险累计欠缴金额</td> 
            <td width="30%" colspan="2">选择不公示</td> 
           </tr> 
           <tr> 
            <td width="30%">单位参加职工基本医疗保险累计欠缴金额</td> 
            <td width="30%" colspan="2">选择不公示</td> 
           </tr> 
           <tr> 
            <td width="30%">单位参加工伤保险累计欠缴金额</td> 
            <td width="30%" colspan="2">选择不公示</td> 
           </tr> 
           <tr> 
            <td width="30%">单位参加生育保险累计欠缴金额</td> 
            <td width="30%" colspan="2">选择不公示</td> 
           </tr> 
          </tbody> 
         </table> 
        </div> 
        <div class="tab-pane fade in " id="2"> 
         <div class="tcaption"> 
          <h3 class="subtitle">企业基本信息</h3> 
          <span class="pull-right text-gray">2016-02-26&nbsp;公布</span> 
         </div> 
         <table class="ntable"> 
          <tbody> 
           <tr> 
            <td class="tb" width="20%">注册号</td> 
            <td width="30%">310141000157096</td> 
            <td class="tb" width="20%">统一社会信用代码</td> 
            <td width="30%">-</td> 
           </tr> 
           <tr> 
            <td class="tb" width="20%">企业经营状态</td> 
            <td width="30%">开业</td> 
            <td class="tb" width="20%">企业联系电话</td> 
            <td width="25%">18918398291</td> 
           </tr> 
           <tr> 
            <td class="tb" width="20%">从业人数 </td> 
            <td width="25%">企业选择不公示</td> 
            <td class="tb" width="20%">邮政编码</td> 
            <td width="25%">200040</td> 
           </tr> 
           <tr> 
            <td class="tb" width="20%">有限责任公司本年度是否发生股东股权转让</td> 
            <td>否</td> 
            <td class="tb" width="20%">企业是否有投资信息或购买其他公司股权</td> 
            <td colspan="3">否</td> 
           </tr> 
           <tr> 
            <td class="tb" width="20%">电子邮箱</td> 
            <td colspan="3"><a href="mailto:manlu@suneee.com" style="color:#555;">manlu@suneee.com</a></td> 
           </tr> 
           <tr> 
            <td class="tb" width="20%">企业通讯地址</td> 
            <td colspan="3"><a onclick="showMapModal('上海市静安区延安中路841号2601室','')">上海市静安区延安中路841号2601室</a></td> 
           </tr> 
          </tbody> 
         </table> 
         <div class="tcaption">
          <h3 class="subtitle">股东（发起人）出资信息</h3>
          <span class="watermark"></span>
         </div> 
         <table class="ntable ntable-odd ntable-stext"> 
          <tbody> 
           <tr> 
            <th class="tx">序号</th> 
            <th>发起人</th> 
            <th>认缴出资额(万元)</th> 
            <th>认缴出资时间</th> 
            <th>认缴出资方式 </th> 
            <th>实缴出资额(万元)</th> 
            <th>实缴出资时间</th> 
            <th>实缴出资方式</th> 
           </tr> 
           <tr> 
            <td class="tx">1</td> 
            <td class="text-center"> <a href="/firm_a8e7e2067e33b36274e99cf223943016.html" target="_blank">象翌微链科技发展有限公司</a> </td> 
            <td width="125" class="text-center">1000</td> 
            <td width="100" class="text-center">2025-12-31</td> 
            <td width="100" class="text-center">货币</td> 
            <td width="125" class="text-center">-</td> 
            <td width="100" class="text-center">-</td> 
            <td width="100" class="text-center">-</td> 
           </tr> 
          </tbody> 
         </table> 
         <div class="tcaption">
          <h3 class="subtitle">企业资产状况信息</h3>
          <span class="watermark"></span>
         </div> 
         <table class="ntable"> 
          <tbody>
           <tr> 
            <td class="tb" width="20%">资产总额</td> 
            <td>企业选择不公示</td> 
            <td class="tb" width="20%">所有者权益合计</td> 
            <td>企业选择不公示</td> 
           </tr> 
           <tr> 
            <td class="tb">营业总收入 </td> 
            <td>企业选择不公示</td> 
            <td class="tb">利润总额 </td> 
            <td>企业选择不公示</td> 
           </tr> 
           <tr> 
            <td class="tb">营业总收入中主营业务收入 </td> 
            <td>企业选择不公示</td> 
            <td class="tb">净利润 </td> 
            <td>企业选择不公示</td> 
           </tr> 
           <tr> 
            <td class="tb">纳税总额 </td> 
            <td>企业选择不公示</td> 
            <td class="tb">负债总额 </td> 
            <td>企业选择不公示</td> 
           </tr> 
          </tbody>
         </table> 
        </div> 
       </div> 
      </section> 
      <section class="panel b-a" id="financingInfo"> 
       <div class="tcaption"> 
        <h3 class="title">融资信息</h3> 
        <span class="tbadge">1</span> 
        <span class="watermark"></span> 
       </div> 
       <table class="ntable ntable-odd"> 
        <tbody>
         <tr>
          <th>序号</th> 
          <th>日期</th> 
          <th>产品名称</th> 
          <th>融资轮次</th> 
          <th>金额</th> 
          <th>投资方</th> 
          <th>新闻来源</th> 
         </tr>
         <tr> 
          <td class="tx">1</td> 
          <td width="103">2016-03-12</td> 
          <td width="103" class="text-center">盒马鲜生</td> 
          <td width="103" class="text-center">A轮</td> 
          <td class="text-center">1.5亿美元</td> 
          <td> 
           <div> 
            <a class="c_a" href="/company_investor?companykey=e45ee37279ffb3f2ce9bbbcfa39d8133&amp;companyname=上海盒马网络科技有限公司&amp;id=eb9849ba221467982e56799d97a39ba6">阿里巴巴</a> 
           </div> </td> 
          <td width="180"> <a href="http://www.ebrun.com/20160312/168684.shtml" target="_blank">传阿里投盒马鲜生1.5亿美金 这是想干啥？</a> </td> 
         </tr> 
        </tbody>
       </table> 
      </section> 
      <section class="m-t-lg" id="memberInfo"> 
       <div class="tcaption"> 
        <h3 class="title">核心人员</h3> 
        <span class="tbadge">1</span> 
        <span class="watermark"></span> 
       </div> 
       <table class="ntable ntable-odd"> 
        <tbody>
         <tr> 
          <th class="tx">序号</th>
          <th>姓名</th>
          <th>职位</th>
          <th>简介</th> 
         </tr> 
         <tr> 
          <td class="tx">1</td> 
          <td width="15%"> <span class="headimg"> <img src="https://co-image.qichacha.com/PersonImage/p73ac1d107d8235907d5087e3b3abe6b.jpg" /> </span> 
           <div class="whead-text"> 
            <a href="/pl_p73ac1d107d8235907d5087e3b3abe6b.html">侯毅</a> 
           </div> </td> 
          <td width="20%" class="text-center">创始人兼CEO</td> 
          <td>
           <div class="line-clamp">
            侯毅，盒马鲜生创始人兼CEO。曾担任京东物流总监。
           </div></td> 
         </tr> 
        </tbody>
       </table> 
      </section> 
      <section class="panel b-a" id="productInfo"> 
       <div class="tcaption"> 
        <h3 class="title">企业业务</h3> 
        <span class="tbadge">1</span> 
        <span class="watermark"></span> 
       </div> 
       <table class="ntable ntable-odd"> 
        <tbody>
         <tr> 
          <th class="tx">序号</th> 
          <th>产品图片</th> 
          <th width="10%">产品名</th> 
          <th width="10%">融资信息</th> 
          <th width="15%">成立时间</th> 
          <th width="10%">所属地</th> 
          <th class="ma_center">产品介绍</th> 
         </tr> 
         <tr> 
          <td class="tx">1</td> 
          <td><img src="http://img.qichacha.com/Product/9bc1b095-ab92-4088-b82e-3c8b5ab22efc.jpg" style="width: 66px;max-height: 66px;" /></td> 
          <td class="text-center"> <a class="c_a" href="/product_9bc1b095-ab92-4088-b82e-3c8b5ab22efc">盒马鲜生</a> </td> 
          <td class="text-center">A轮</td> 
          <td class="text-center"> 2015-06-02 </td> 
          <td class="text-center">上海</td> 
          <td>
           <div class="line-clamp">
            盒马鲜生是一家生鲜电商O2O服务品牌，通过线上APP、线下门店等，提供生鲜食品和餐饮服务。致力于为消费者提供一站式“极致新鲜”的生活方式。
           </div></td> 
         </tr> 
        </tbody>
       </table> 
      </section> 
      <section class="m-t-lg" id="compatProductInfo"> 
       <div class="tcaption"> 
        <h3 class="title">竞品信息</h3> 
        <span class="tbadge">13</span> 
        <span class="watermark"></span> 
       </div> 
       <table class="ntable ntable-odd"> 
        <tbody>
         <tr> 
          <th class="tx">序号</th> 
          <th>产品图片</th> 
          <th>产品名</th> 
          <th>融资信息</th> 
          <th>成立时间</th> 
          <th>所属地</th> 
          <th>产品介绍</th> 
         </tr> 
         <tr> 
          <td class="tx">1</td> 
          <td width="90"><img style="width: 66px;max-height: 66px;" src="http://img.qichacha.com/Product/17d00759-2e40-4e64-9369-9414da013534.jpg" alt="鲜生活" /></td> 
          <td width="10%" class="text-center"><a onclick="" class="text-primary" target="_blank" href="/product_17d00759-2e40-4e64-9369-9414da013534">鲜生活</a></td> 
          <td width="10%" class="text-center">战略投资</td> 
          <td width="12%" class="text-center">2014-07-25</td> 
          <td width="10%" class="text-center">北京</td> 
          <td style="position: relative;">
           <div class="line-clamp" style="height: 89.6px;">
            鲜生活是一家专注于便利店行业的新零售赋能、运营和整合型公司。鲜生活通过旗下「楼下」生态系统为便利店进行线上线下一体化解决方案的赋能改造提升，进行新零售运营，在更好服务消费者的同时提升便利店的营收和盈利性。
           </div>
           <div class="line-clamp-btn">
            <span style="color:#222">…</span>更多
           </div></td> 
         </tr> 
         <tr> 
          <td class="tx">2</td> 
          <td width="90"><img style="width: 66px;max-height: 66px;" src="http://img.qichacha.com/Product/189df8dc-03ae-43bf-a2a7-2bf33d523913.jpg" alt="食得鲜" /></td> 
          <td width="10%" class="text-center"><a onclick="" class="text-primary" target="_blank" href="/product_189df8dc-03ae-43bf-a2a7-2bf33d523913">食得鲜</a></td> 
          <td width="10%" class="text-center">C轮</td> 
          <td width="12%" class="text-center">2017-06-22</td> 
          <td width="10%" class="text-center">广州</td> 
          <td style="position: relative;">
           <div class="line-clamp" style="height: 89.6px;">
            食得鲜创始于2014年，是一家通过自主研发云系统和自建强物流，将线下体验式前置仓和线上商城进行渠道融合的新零售线上平价超市。为用户提供更好的生鲜购买解决方案，通过高效的配送系统与售后服务为用户提供三小时内送达、超时免单等优质服务，为用户搭建出良好生鲜购物场景。
           </div>
           <div class="line-clamp-btn">
            <span style="color:#222">…</span>更多
           </div></td> 
         </tr> 
         <tr> 
          <td class="tx">3</td> 
          <td width="90"><img style="width: 66px;max-height: 66px;" src="http://img.qichacha.com/Product/9d38ee00-539c-4e87-9b91-240bb28dd96f.jpg" alt="地球港" /></td> 
          <td width="10%" class="text-center"><a onclick="" class="text-primary" target="_blank" href="/product_9d38ee00-539c-4e87-9b91-240bb28dd96f">地球港</a></td> 
          <td width="10%" class="text-center">Pre-A轮</td> 
          <td width="12%" class="text-center">2017-03-23</td> 
          <td width="10%" class="text-center">北京</td> 
          <td>
           <div class="line-clamp">
            地球港，一个全球好食新空间，带你无时差品尝世界新鲜美食，体验趣味创新科技，享受生活本真热爱。
           </div></td> 
         </tr> 
         <tr> 
          <td class="tx">4</td> 
          <td width="90"><img style="width: 66px;max-height: 66px;" src="http://img.qichacha.com/Product/7b84fc92-710b-49e9-b620-166a2ffb0954.jpg" alt="生鲜传奇" /></td> 
          <td width="10%" class="text-center"><a onclick="" class="text-primary" target="_blank" href="/product_7b84fc92-710b-49e9-b620-166a2ffb0954">生鲜传奇</a></td> 
          <td width="10%" class="text-center">B轮</td> 
          <td width="12%" class="text-center">2017-08-24</td> 
          <td width="10%" class="text-center">安徽</td> 
          <td style="position: relative;">
           <div class="line-clamp" style="height: 89.6px;">
            生鲜传奇是一个生鲜连锁超市，采用阿尔迪折扣店的模式，利用货架管理和成本控制的模式，针对用户的饮食习惯、购物习惯、居住和交通习惯等数据信息，为用户提供生鲜及厨房周边商品，包括豆制品、冷冻品、水产、蛋品、杂粮等。
           </div>
           <div class="line-clamp-btn">
            <span style="color:#222">…</span>更多
           </div></td> 
         </tr> 
         <tr> 
          <td class="tx">5</td> 
          <td width="90"><img style="width: 66px;max-height: 66px;" src="http://img.qichacha.com/Product/05ba021e-8bc9-4bab-9ed4-b1a66109db09.jpg" alt="比由技术工场" /></td> 
          <td width="10%" class="text-center"><a onclick="" class="text-primary" target="_blank" href="/product_05ba021e-8bc9-4bab-9ed4-b1a66109db09">比由技术工场</a></td> 
          <td width="10%" class="text-center">Pre-A轮</td> 
          <td width="12%" class="text-center">2016-03-29</td> 
          <td width="10%" class="text-center">常州</td> 
          <td style="position: relative;">
           <div class="line-clamp" style="height: 89.6px;">
            比由技术工场是一家物联网技术创投公司，采用技术入股方式，以创业企业5%左右的股份作为部分开发费用，为其提供长期技术服务。提供APP开发服务、软件微信开发及物联网技术服务。同时提供投融资对接服务，拥有“聚份子”平台，为创业者解决“找钱难”的问题，快速对接投资人。
           </div>
           <div class="line-clamp-btn">
            <span style="color:#222">…</span>更多
           </div></td> 
         </tr> 
         <tr> 
          <td class="tx">6</td> 
          <td width="90"><img style="width: 66px;max-height: 66px;" src="http://img.qichacha.com/Product/003c7c72-913a-498d-8ad7-9b8cb593e954.jpg" alt="博流科技" /></td> 
          <td width="10%" class="text-center"><a onclick="" class="text-primary" target="_blank" href="/product_003c7c72-913a-498d-8ad7-9b8cb593e954">博流科技</a></td> 
          <td width="10%" class="text-center">A轮</td> 
          <td width="12%" class="text-center">2010-09-19</td> 
          <td width="10%" class="text-center">杭州</td> 
          <td>
           <div class="line-clamp">
            公司专注于基于流体机械的控制类产品和测试解决方案，主要产品包括：高精度全自动泵测试系统、智能阀门定位器，智能调节阀等。
           </div></td> 
         </tr> 
         <tr> 
          <td class="tx">7</td> 
          <td width="90"><img style="width: 66px;max-height: 66px;" src="http://img.qichacha.com/Product/00938f73-b744-4c6f-a252-03aebd81dafa.jpg" alt="乐乐优品" /></td> 
          <td width="10%" class="text-center"><a onclick="" class="text-primary" target="_blank" href="/product_00938f73-b744-4c6f-a252-03aebd81dafa">乐乐优品</a></td> 
          <td width="10%" class="text-center">-</td> 
          <td width="12%" class="text-center">2013-10-14</td> 
          <td width="10%" class="text-center">西安</td> 
          <td>
           <div class="line-clamp">
            乐乐优品是一个LBS的生活服务解决方案提供商，为用户提供食住的解决方案。
           </div></td> 
         </tr> 
         <tr> 
          <td class="tx">8</td> 
          <td width="90"><img style="width: 66px;max-height: 66px;" src="/material/theme/chacha/cms/v2/images/no_image.png" alt="沙丁网络" /></td> 
          <td width="10%" class="text-center"><a onclick="" class="text-primary" target="_blank" href="/product_0098c217-db7f-4e60-a4b3-144b6ee24bc0">沙丁网络</a></td> 
          <td width="10%" class="text-center">-</td> 
          <td width="12%" class="text-center">2013-07-17</td> 
          <td width="10%" class="text-center">南京</td> 
          <td>
           <div class="line-clamp">
            沙丁网络致力于o2o的实践，为了能让我们生活的更有价值这一理念而努力。
           </div></td> 
         </tr> 
         <tr> 
          <td class="tx">9</td> 
          <td width="90"><img style="width: 66px;max-height: 66px;" src="http://img.qichacha.com/Product/00c65b53-fe27-4ac9-b638-e45077efc689.jpg" alt="紫米商城" /></td> 
          <td width="10%" class="text-center"><a onclick="" class="text-primary" target="_blank" href="/product_00c65b53-fe27-4ac9-b638-e45077efc689">紫米商城</a></td> 
          <td width="10%" class="text-center">B轮</td> 
          <td width="12%" class="text-center">2012-02-23</td> 
          <td width="10%" class="text-center">南京</td> 
          <td>
           <div class="line-clamp">
            紫米电子是一家手机精品配件及消费电子公司，产品涉及移动电源、蓝牙音箱、无线路由器等，旗下产品有小米移动电源等。
           </div></td> 
         </tr> 
         <tr> 
          <td class="tx">10</td> 
          <td width="90"><img style="width: 66px;max-height: 66px;" src="/material/theme/chacha/cms/v2/images/no_image.png" alt="西安沃泰" /></td> 
          <td width="10%" class="text-center"><a onclick="" class="text-primary" target="_blank" href="/product_00cabf2f-444a-4003-8297-edc6c2b018d9">西安沃泰</a></td> 
          <td width="10%" class="text-center">战略投资</td> 
          <td width="12%" class="text-center">2001-09-30</td> 
          <td width="10%" class="text-center">西安</td> 
          <td style="position: relative;">
           <div class="line-clamp" style="height: 89.6px;">
            西安沃泰科技有限公司是一家以水利信息化为方向的专业化企业，提供测控产品销售、业务系统集成及综合解决方案等服务，实现了水利应用软件的平台化和模块化，形成了C/S与B/S结合的水利信息化综合管理平台，并有灌区配水管理、水费计收、水务公开、闸泵监控、水雨情测报、防汛决策支持、智能节水灌溉、自来水（污水）处理、城市供水综合调度、水库运行调度、地下水动态监测等丰富的功能模块。此外还有应用于水利和供水领域的十几项硬件产品，包括超声波、雷达、磁致伸缩、压力等水位、流量传感器；遥测终端、智能管网压力终端和多种一体化测控模块等二次设备；以及闸门控制柜、泵站监测保护柜等成套设备，覆盖面广，可靠性高。
           </div>
           <div class="line-clamp-btn">
            <span style="color:#222">…</span>更多
           </div></td> 
         </tr> 
         <tr> 
          <td class="tx">11</td> 
          <td width="90"><img style="width: 66px;max-height: 66px;" src="http://img.qichacha.com/Product/00ead9a3-8f03-4440-81fc-20ce729fc214.jpg" alt="物联时代" /></td> 
          <td width="10%" class="text-center"><a onclick="" class="text-primary" target="_blank" href="/product_00ead9a3-8f03-4440-81fc-20ce729fc214">物联时代</a></td> 
          <td width="10%" class="text-center">Pre-A轮</td> 
          <td width="12%" class="text-center">2017-08-09</td> 
          <td width="10%" class="text-center">深圳</td> 
          <td style="position: relative;">
           <div class="line-clamp" style="height: 89.6px;">
            物联时代是一家专注于物联网服务，智能产品研发、制造、销售于一体的高新技术企业，物联时代通过智能硬件成本补贴的方式，消除挡在智能硬件入口的壁垒，让用户直达核心需求。物联时代通过流量充值业务、新零售业务、广告业务、其他增值业务等打造综合型物联网平台。
           </div>
           <div class="line-clamp-btn">
            <span style="color:#222">…</span>更多
           </div></td> 
         </tr> 
         <tr> 
          <td class="tx">12</td> 
          <td width="90"><img style="width: 66px;max-height: 66px;" src="http://img.qichacha.com/Product/00ede687-e91b-4dbf-95d2-304083ecbba7.jpg" alt="蝶莱新风系统" /></td> 
          <td width="10%" class="text-center"><a onclick="" class="text-primary" target="_blank" href="/product_00ede687-e91b-4dbf-95d2-304083ecbba7">蝶莱新风系统</a></td> 
          <td width="10%" class="text-center">-</td> 
          <td width="12%" class="text-center">2005-03-17</td> 
          <td width="10%" class="text-center">广州</td> 
          <td>
           <div class="line-clamp">
            蝶莱新风系统是专注于室内空气环境改善的服务商，服务领域包含生物医药、生物制剂、食品、日化、电子、半导体等行业。
           </div></td> 
         </tr> 
         <tr> 
          <td class="tx">13</td> 
          <td width="90"><img style="width: 66px;max-height: 66px;" src="http://img.qichacha.com/Product/011ac706-de8c-46bb-aa78-b91e2f57a578.jpg" alt="力策科技" /></td> 
          <td width="10%" class="text-center"><a onclick="" class="text-primary" target="_blank" href="/product_011ac706-de8c-46bb-aa78-b91e2f57a578">力策科技</a></td> 
          <td width="10%" class="text-center">战略投资</td> 
          <td width="12%" class="text-center">2013-10-12</td> 
          <td width="10%" class="text-center">深圳</td> 
          <td style="position: relative;">
           <div class="line-clamp" style="height: 89.6px;">
            力策科技是消费级激光雷达的开发商，面向机器人、工业自动化、智能家居、无人机等行业，提供二维激光雷达ME-01、三维激光雷达SS-01等产品，并提供激光雷达系统、激光雷达应用软件、微器件设计与加工等服务。
           </div>
           <div class="line-clamp-btn">
            <span style="color:#222">…</span>更多
           </div></td> 
         </tr> 
        </tbody>
       </table> 
      </section> 
      <section class="panel b-a clear"> 
       <div class="m_ptsc" style="padding:20px 0;">
        数据来源：国家企业信用信息公示系统。
       </div> 
      </section> 
      <script type="text/javascript">
	initMoreTextHide(4);
</script> 
     </div> 
     <div class="data_div" id="assets_div" style="display: none;"> 
      <style>
    .dropdownSpan{
        padding: 2px 10px;
    }
    #shangbiaolist .dropdown-menu{
        max-height: 400px;
        overflow-x: hidden;
        overflow-y: auto;
    }
    #zhuanlilist .dropdown-menu{
        max-height: 400px;
        overflow-x: hidden;
        overflow-y: auto;
    }
</style> 
      <div class="assets_info"></div> 
      <section class="panel b-a clear m_dataTab"> 
       <div class="panel-body"> 
        <a href="javascript:;" class="btn btn-sm btn-default  m-r-sm c_disable" style="white-space:nowrap;cursor: default"> 商标信息&nbsp;0 </a> 
        <a href="javascript:;" class="btn btn-sm btn-default  m-r-sm c_disable" style="white-space:nowrap;cursor: pointer"> 专利信息&nbsp;0 </a> 
        <a href="javascript:;" onclick="boxScrollNew('#zhengshulist');zhugeTrack('企业主页-知识产权-证书信息',{'企业名称':'上海盒马网络科技有限公司'});" class="btn btn-sm btn-default  m-r-sm" style="white-space:nowrap;"> 证书信息&nbsp;2 </a> 
        <a href="javascript:;" onclick="boxScrollNew('#zzqlist');zhugeTrack('企业主页-知识产权-作品著作权',{'企业名称':'上海盒马网络科技有限公司'});" class="btn btn-sm btn-default  m-r-sm" style="white-space:nowrap;"> 作品著作权&nbsp;17 </a> 
        <a href="javascript:;" class="btn btn-sm btn-default  m-r-sm c_disable" style="white-space:nowrap;cursor: default"> 软件著作权&nbsp;0 </a> 
        <a href="javascript:;" onclick="boxScrollNew('#websitelist');zhugeTrack('企业主页-知识产权-网站信息',{'企业名称':'上海盒马网络科技有限公司'});" class="btn btn-sm btn-default  m-r-sm" style="white-space:nowrap;"> 网站信息&nbsp;2 </a> 
       </div> 
      </section> 
      <section class="panel b-a clear" id="zhengshulist"> 
       <div class="tcaption"> 
        <h3 class="title">证书信息</h3> 
        <span class="tbadge">2</span> 
        <div class="chooseAssets" data-box="zs" style="float: right"> 
         <div class="tdrop"> 
          <span class="btn" data-toggle="dropdown"> <span>所有类型</span> <span class="caret m-l"></span> </span> 
          <ul class="dropdown-menu dropdown-menu-right"> 
           <li><a href="javascript:;" data-option="certCategory" data-value="0">不限</a></li> 
           <li><a href="javascript:;" data-option="certCategory" data-value="cnca051">信息安全管理体系认证(2)</a></li> 
          </ul> 
         </div> 
        </div> 
        <span class="watermark"></span> 
       </div> 
       <div class="col-md-12"></div>
       <table class="ntable ntable-odd"> 
        <tbody>
         <tr>
          <th class="tx">序号</th>
          <th>证书类型</th>
          <th>证书名称</th>
          <th>证书编号</th>
          <th>发证日期</th>
          <th>截止日期</th>
         </tr> 
         <tr> 
          <td class="tx">1</td> 
          <td width="160">信息安全管理体系认证</td> 
          <td> <a class="text-primary" data-toggle="modal" data-target="#zsModal" onclick="zsView(&quot;5654c5ee32c24697ec7797bdce294f1f1&quot;)"> - </a> </td> 
          <td width="110">279840CC3-2018-AIS-RGC-UKAS</td> 
          <td width="103">2018-12-26 </td> 
          <td width="103">2021-12-26</td> 
         </tr> 
         <tr> 
          <td class="tx">2</td> 
          <td width="160">信息安全管理体系认证</td> 
          <td> <a class="text-primary" data-toggle="modal" data-target="#zsModal" onclick="zsView(&quot;55bb29ea5ce2089f032aee4c7f080fcf1&quot;)"> - </a> </td> 
          <td width="110">281265CC3-2018-AIS-RGC-CNAS</td> 
          <td width="103">2018-12-26 </td> 
          <td width="103">2021-12-26</td> 
         </tr> 
        </tbody>
       </table> 
       <div class="m-b"> 
       </div> 
      </section> 
      <section class="panel b-a clear" id="zzqlist"> 
       <div class="tcaption"> 
        <h3 class="title">作品著作权</h3> 
        <span class="tbadge"> 17 </span> 
        <span class="watermark"></span> 
       </div> 
       <div class="col-md-12"></div>
       <div class="col-md-12"></div>
       <div class="col-md-12"></div>
       <div class="col-md-12"></div>
       <div class="col-md-12"></div>
       <table class="ntable ntable-odd"> 
        <tbody>
         <tr>
          <th class="tx">序号</th>
          <th>作品名称</th>
          <th>首次发表日期</th>
          <th>创作完成日期</th>
          <th>登记号</th>
          <th>登记日期</th>
          <th>登记类别</th>
         </tr> 
         <tr> 
          <td class="tx">1</td> 
          <td width="182">REX</td> 
          <td width="112" class="text-center">2018-11-15</td> 
          <td width="112" class="text-center">2018-11-15</td> 
          <td>国作登字-2018-F-00666164</td> 
          <td width="103" class="text-center">2018-11-15</td> 
          <td class="text-center">美术</td> 
         </tr> 
         <tr> 
          <td class="tx">2</td> 
          <td width="182">盒马吉祥物舞狮版</td> 
          <td width="112" class="text-center">2018-07-02</td> 
          <td width="112" class="text-center">2018-07-02</td> 
          <td>国作登字-2018-F-00571515</td> 
          <td width="103" class="text-center">2018-07-02</td> 
          <td class="text-center">美术</td> 
         </tr> 
         <tr> 
          <td class="tx">3</td> 
          <td width="182">盒马吉祥物2018版坐姿</td> 
          <td width="112" class="text-center">2018-07-02</td> 
          <td width="112" class="text-center">2018-07-02</td> 
          <td>国作登字-2018-F-00571734</td> 
          <td width="103" class="text-center">2018-07-02</td> 
          <td class="text-center">美术</td> 
         </tr> 
         <tr> 
          <td class="tx">4</td> 
          <td width="182">盒马内容类表情系列2018版</td> 
          <td width="112" class="text-center">2018-07-02</td> 
          <td width="112" class="text-center">2018-07-02</td> 
          <td>国作登字-2018-F-00571736</td> 
          <td width="103" class="text-center">2018-07-02</td> 
          <td class="text-center">美术</td> 
         </tr> 
         <tr> 
          <td class="tx">5</td> 
          <td width="182">盒马吉祥物配送版</td> 
          <td width="112" class="text-center">2018-07-02</td> 
          <td width="112" class="text-center">2018-07-02</td> 
          <td>国作登字-2018-F-00571753</td> 
          <td width="103" class="text-center">2018-07-02</td> 
          <td class="text-center">美术</td> 
         </tr> 
         <tr> 
          <td class="tx">6</td> 
          <td width="182">盒马吉祥物2018版</td> 
          <td width="112" class="text-center">2018-07-02</td> 
          <td width="112" class="text-center">2018-07-02</td> 
          <td>国作登字-2018-F-00571735</td> 
          <td width="103" class="text-center">2018-07-02</td> 
          <td class="text-center">美术</td> 
         </tr> 
         <tr> 
          <td class="tx">7</td> 
          <td width="182">盒马表情系列2018版</td> 
          <td width="112" class="text-center">2018-07-02</td> 
          <td width="112" class="text-center">2018-07-02</td> 
          <td>国作登字-2018-F-00571737</td> 
          <td width="103" class="text-center">2018-07-02</td> 
          <td class="text-center">美术</td> 
         </tr> 
         <tr> 
          <td class="tx">8</td> 
          <td width="182">盒马吉祥物婴儿版</td> 
          <td width="112" class="text-center">2018-07-02</td> 
          <td width="112" class="text-center">2018-07-02</td> 
          <td>国作登字-2018-F-00571741</td> 
          <td width="103" class="text-center">2018-07-02</td> 
          <td class="text-center">美术</td> 
         </tr> 
         <tr> 
          <td class="tx">9</td> 
          <td width="182">盒马辅助标识系列一</td> 
          <td width="112" class="text-center">2018-06-04</td> 
          <td width="112" class="text-center">2018-06-04</td> 
          <td>国作登字-2018-F-00557445</td> 
          <td width="103" class="text-center">2018-06-04</td> 
          <td class="text-center">美术</td> 
         </tr> 
         <tr> 
          <td class="tx">10</td> 
          <td width="182">帝皇鲜DIFRESCO</td> 
          <td width="112" class="text-center">2018-04-08</td> 
          <td width="112" class="text-center">2018-04-08</td> 
          <td>国作登字-2018-F-00530160</td> 
          <td width="103" class="text-center">2018-04-08</td> 
          <td class="text-center">美术</td> 
         </tr> 
        </tbody>
       </table> 
       <div class="m-b"> 
        <nav class="text-right"> 
         <ul class="pagination"> 
          <li class="active"><a htef="#">1</a></li>
          <li><a id="ajaxpage" href="javascript:getTabList(2,&quot;assets&quot;,&quot;zzq&quot;)">2</a></li> 
          <li><a id="ajaxpage" href="javascript:getTabList(2,&quot;assets&quot;,&quot;zzq&quot;)">&gt;</a></li> 
         </ul> 
        </nav> 
       </div> 
      </section> 
      <section class="panel b-a clear" id="websitelist"> 
       <style type="text/css"> </style> 
       <div class="tcaption"> 
        <span class="title">网站信息 <span class="tbadge"> 2 </span> <span class="watermark"></span> </span>
       </div> 
       <div class="col-md-12"></div>
       <table class="ntable ntable-odd"> 
        <tbody>
         <tr>
          <th class="tx">序号</th>
          <th width="280" class="tl">网址</th>
          <th width="160" class="tl">网站名称</th>
          <th>域名</th>
          <th width="145">网站备案/许可证号</th>
          <th width="103">审核时间</th>
         </tr> 
         <tr> 
          <td class="tx">1</td> 
          <td class="ti"> <i class="icon-safe webauth-i"> 
            <div class="webauth-template"> 
             <div> 
              <div class="col-left"> 
               <div class="name">
                上海盒马网络科技有限公司
               </div> 
               <div class="info">
                <span>验证深度：</span> 
                <span class="starts"> <span class="icon_start1"></span> <span class="icon_start1"></span> <span class="icon_start0"></span> <span class="icon_start0"></span> <span class="icon_start0"></span> </span> 
               </div> 
               <div class="info">
                <span>信誉积累：</span> 281天
               </div> 
               <div class="info">
                <span>有效期限：</span> 2018/08/07~2019/08/08
               </div> 
              </div> 
              <a target="_blank" rel="nofollow" href="https://v.yunaq.com/certificate?domain=www.hemaos.com" onclick="" class="webauth-gwtb"> <img src="/material/theme/chacha/cms/v2/images/webauth_gwtb2.png" /> <span>查看证书</span> </a> 
              <div class="clearfix"></div> 
              <div class="des">
               通过了经营内容合法性、运营方实名验证、行业经营资质核验、网站安全性评估、网站优质评估等128项审核。
              </div> 
              <div class="bottom">
                以上认证信息由
               <a target="_blank" rel="nofollow" href="https://xinyong.yunaq.com/landing?from=qichacha" style="color: #128bed;" onclick="zhugeTrack('企业主页-网站认证-创宇信用');">创宇信用</a>提供 
              </div> 
             </div> 
            </div> </i> <a class="c_a" href="http://www.hemaos.com" target="_blank" rel="nofollow">www.hemaos.com</a><br /> </td> 
          <td>盒马后控台</td> 
          <td class="text-center"> hemaos.com<br /> </td> 
          <td class="text-center">沪ICP备16036315号-2</td> 
          <td class="text-center">2018-11-21</td> 
         </tr> 
         <tr> 
          <td class="tx">2</td> 
          <td> <a class="c_a" href="http://www.shyhhema.com" target="_blank" rel="nofollow">www.shyhhema.com</a><br /> </td> 
          <td>上海翌恒网络</td> 
          <td class="text-center"> shyhhema.com<br /> </td> 
          <td class="text-center">沪ICP备16036315号-1</td> 
          <td class="text-center">2018-11-21</td> 
         </tr> 
        </tbody>
       </table> 
       <div class="m-b"> 
       </div> 
      </section> 
      <div class="modal fade" id="biaoModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> 
       <div class="modal-dialog nmodal"> 
        <div class="modal-content"> 
         <div class="modal-header"> 
          <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> 
          <h4 class="modal-title" id="myModalLabel">商标详情</h4> 
         </div> 
         <div class="modal-body"> 
          <div class="sbview"></div> 
          <div class="clearfix"></div> 
         </div> 
        </div> 
       </div> 
      </div> 
      <div class="modal fade" id="zlModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> 
       <div class="modal-dialog nmodal"> 
        <div class="modal-content"> 
         <div class="modal-header"> 
          <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> 
          <h4 class="modal-title" id="myModalLabel">专利详情</h4> 
         </div> 
         <div class="modal-body"> 
          <div class="zlview"></div> 
          <div class="clearfix"></div> 
         </div> 
        </div> 
       </div> 
      </div> 
      <div class="modal fade" id="zsModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> 
       <div class="modal-dialog nmodal"> 
        <div class="modal-content"> 
         <div class="modal-header"> 
          <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> 
          <h4 class="modal-title" id="myModalLabel">证书详情</h4> 
         </div> 
         <div class="modal-body" style="max-height: calc(100vh - 125px);overflow-y: auto;"> 
          <div class="zsview"></div> 
          <div class="clearfix"></div> 
         </div> 
        </div> 
       </div> 
      </div> 
      <section class="panel b-a clear"> 
       <div class="m_ptsc" style="padding:20px 0;">
        数据来源：国家工商行政管理总局商标局、中华人民共和国国家知识产权局、中国版权登记门户网。
       </div> 
      </section> 
      <script>
    function hideChart(dom){
        if($(dom).find('i').hasClass('i-arrow-up4')){
            $(dom).find('i').removeClass('i-arrow-up4');
            $(dom).find('i').addClass('i-arrow-down4')
            $(dom).find('span').html('展开');
            $(dom).parent().next().hide();
        }else{
            $(dom).find('i').removeClass('i-arrow-down4');
            $(dom).find('i').addClass('i-arrow-up4')
            $(dom).find('span').html('收起');
            $(dom).parent().next().show();
        }
        
    }
    $(function () {


         //低于5个隐藏图表

         //低于5个隐藏图表
        
       
        
        $('.chooseAssets').find('a').on('click',function(){
            var targetDiv = $(this).parent().parent().parent().parent();
            var target = targetDiv.attr('data-box');
            var optionArr = [];
            var hiddenName = '';
            var hiddenValue = '';
            var ajaxData = {};
            switch(target){
                case 'sb':
                    optionArr = ['sbappdateyear','sbstatus','sbflowno','sbintcls'];
                    ajaxData['box'] = 'shangbiao';
                    break;
                case 'zl':
                    optionArr = ['zlpublicationyear','zlipclist','zlkindcode','zllegalstatus'];
                    ajaxData['box'] = 'zhuanli';
                    break;
                case 'zs':
                    optionArr = ['zscertCategory'];
                    ajaxData['box'] = 'zhengshu';
                    break;
                default :
                    break;
            }
            var option = $(this).attr('data-option');
            option = target + option;
            var value = $(this).attr('data-value');
            var text = $(this).text();
            var textArr = text.split('(');
            $("input[name=" + option + "]").val(value);
            $("input[name=" + option + "]").attr('data-desc',textArr[0]);
            //取所有筛选条件的值
            for(var i=0;i<optionArr.length;i++){
                hiddenName = optionArr[i];
                hiddenValue = $("input[name=" + hiddenName + "]").val();
                ajaxData[hiddenName] = hiddenValue;
            }
            //拼接其他参数
            ajaxData['unique'] = $("#unique").val();
            ajaxData['companyname'] = $("#companyname").val();
            ajaxData['tab'] = 'assets';
            ajaxData['p'] = '1';
            getTabListNew(ajaxData);
        });
    });
</script> 
     </div> 
     <div class="data_div" id="job_div" style="display: none;"></div> 
     <div class="data_div" id="run_div" style="display: none;"> 
      <div class="run_info"></div> 
      <section class="panel b-a clear m_dataTab"> 
       <div class="panel-body" style="padding-top: 5px"> 
        <a href="javascript:;" onclick="boxScrollNew('#licenslist');zhugeTrack('企业主页-经营状况-行政许可',{'企业名称':'上海盒马网络科技有限公司'});" class="btn btn-sm btn-default  m-r-sm m-t-sm" style="white-space:nowrap;"> 行政许可&nbsp;53 </a> 
        <a href="javascript:;" onclick="boxScrollNew('#taxCreditList');zhugeTrack('企业主页-经营状况-税务信用',{'企业名称':'上海盒马网络科技有限公司'});" class="btn btn-sm btn-default  m-r-sm m-t-sm" style="white-space:nowrap;"> 税务信用&nbsp;1 </a> 
        <a href="javascript:;" onclick="boxScrollNew('#tenderlist');zhugeTrack('企业主页-经营状况-招投标信息',{'企业名称':'上海盒马网络科技有限公司'});" class="btn btn-sm btn-default  m-r-sm m-t-sm" style="white-space:nowrap;"> 招投标信息&nbsp;1 </a> 
        <a href="javascript:;" onclick="boxScrollNew('#joblist');zhugeTrack('企业主页-经营状况-招聘',{'企业名称':'上海盒马网络科技有限公司'});" class="btn btn-sm btn-default  m-r-sm m-t-sm" style="white-space:nowrap;"> 招聘&nbsp;1776 </a> 
        <a href="javascript:;" class="btn btn-sm btn-default  m-r-sm m-t-sm c_disable" style="white-space:nowrap;cursor: default"> 财务总览&nbsp;0 </a> 
        <a href="javascript:;" class="btn btn-sm btn-default  m-r-sm m-t-sm c_disable" style="white-space:nowrap;cursor: default"> 进出口信用&nbsp;0 </a> 
        <a href="javascript:;" class="btn btn-sm btn-default  m-r-sm m-t-sm c_disable" style="white-space:nowrap;cursor: default"> 微信公众号&nbsp;0 </a> 
        <a href="javascript:;" onclick="boxScrollNew('#weibolist');zhugeTrack('企业主页-经营状况-微博',{'企业名称':'上海盒马网络科技有限公司'});" class="btn btn-sm btn-default  m-r-sm m-t-sm" style="white-space:nowrap;"> 微博&nbsp;2 </a> 
        <a href="javascript:;" onclick="boxScrollNew('#newslist');zhugeTrack('企业主页-经营状况-新闻舆情',{'企业名称':'上海盒马网络科技有限公司'});" class="btn btn-sm btn-default  m-r-sm m-t-sm" style="white-space:nowrap;"> 新闻舆情&nbsp;4992 </a> 
        <a href="javascript:;" onclick="boxScrollNew('#yblist');zhugeTrack('企业主页-经营状况-公告研报',{'企业名称':'上海盒马网络科技有限公司'});" class="btn btn-sm btn-default  m-r-sm m-t-sm" style="white-space:nowrap;"> 公告研报&nbsp;17 </a> 
        <a href="javascript:;" class="btn btn-sm btn-default  m-r-sm m-t-sm c_disable" style="white-space:nowrap;cursor: default"> 地块公示&nbsp;0 </a> 
        <a href="javascript:;" class="btn btn-sm btn-default  m-r-sm m-t-sm c_disable" style="white-space:nowrap;cursor: default"> 购地信息&nbsp;0 </a> 
        <a href="javascript:;" class="btn btn-sm btn-default  m-r-sm m-t-sm c_disable" style="white-space:nowrap;cursor: default"> 土地转让&nbsp;0 </a> 
        <a href="javascript:;" class="btn btn-sm btn-default  m-r-sm m-t-sm c_disable" style="white-space:nowrap;cursor: default"> 债券信息&nbsp;0 </a> 
        <a href="javascript:;" onclick="boxScrollNew('#spotCheckList');zhugeTrack('企业主页-经营状况-抽查检查',{'企业名称':'上海盒马网络科技有限公司'});" class="btn btn-sm btn-default  m-r-sm m-t-sm" style="white-space:nowrap;"> 抽查检查&nbsp;2 </a> 
        <a href="javascript:;" class="btn btn-sm btn-default  m-r-sm m-t-sm c_disable" style="white-space:nowrap;cursor: default"> 电信许可&nbsp;0 </a> 
        <a href="javascript:;" onclick="boxScrollNew('#supplierlist');zhugeTrack('企业主页-经营状况-供应商',{'企业名称':'上海盒马网络科技有限公司'});" class="btn btn-sm btn-default  m-r-sm m-t-sm" style="white-space:nowrap;"> 供应商&nbsp;1 </a> 
        <a href="javascript:;" onclick="boxScrollNew('#customerlist');zhugeTrack('企业主页-经营状况-客户',{'企业名称':'上海盒马网络科技有限公司'});" class="btn btn-sm btn-default  m-r-sm m-t-sm" style="white-space:nowrap;"> 客户&nbsp;1 </a> 
        <a href="javascript:;" class="btn btn-sm btn-default  m-r-sm m-t-sm c_disable" style="white-space:nowrap;cursor: default"> 信用评级&nbsp;0 </a> 
       </div> 
      </section> 
      <section class="panel clear b-a" id="licenslist"> 
       <div class="tcaption"> 
        <h3 class="title"> 行政许可 [工商局]</h3> 
        <span class="tbadge">38</span> 
        <span class="thist">（查看更多10条 <a onclick="jumpHistory('hisxzxk')">历史行政许可</a>）</span> 
        <span class="watermark"></span> 
       </div> 
       <table class="ntable ntable-odd"> 
        <tbody>
         <tr>
          <th class="tx">序号</th>
          <th width="15%">许可文件编号</th>
          <th width="20%">许可文件名称</th>
          <th width="103">有效期自</th> 
          <th width="103">有效期至</th>
          <th>许可机关</th>
          <th width="20%">许可内容</th> 
         </tr> 
         <tr> 
         </tr>
         <tr>
          <td class="tx">1</td> 
          <td>徐环审2016-126</td> 
          <td>建设项目环境影响评价文件的审批</td> 
          <td class="text-center">-</td> 
          <td class="text-center">-</td> 
          <td>上海市环境保护局</td> 
          <td>06060001CF81DF2E491D4922AACB59025F39F94C</td> 
         </tr> 
         <tr> 
         </tr>
         <tr>
          <td class="tx">2</td> 
          <td>沪静安环保许管[2016]73号</td> 
          <td>建设项目环境影响评价文件的审批</td> 
          <td class="text-center">-</td> 
          <td class="text-center">-</td> 
          <td>上海市环境保护局</td> 
          <td>060600016330EDF0AD7E4044A62DD9341D9BDFD5</td> 
         </tr> 
         <tr> 
         </tr>
         <tr>
          <td class="tx">3</td> 
          <td>沪浦环保许评[2015]2276号</td> 
          <td>建设项目环境影响评价文件的审批</td> 
          <td class="text-center">-</td> 
          <td class="text-center">-</td> 
          <td>上海市环境保护局</td> 
          <td>060600012BF2F4AD0D0E43B698CBC4AEB5E97F2A</td> 
         </tr> 
         <tr> 
         </tr>
         <tr>
          <td class="tx">4</td> 
          <td>徐环审2016-136</td> 
          <td>建设项目环境影响评价文件的审批</td> 
          <td class="text-center">-</td> 
          <td class="text-center">-</td> 
          <td>上海市环境保护局</td> 
          <td>06060001013C7B41AD62474FAFFC979BC939DD58</td> 
         </tr> 
         <tr> 
         </tr>
         <tr>
          <td class="tx">5</td> 
          <td>徐环审2016-137</td> 
          <td>建设项目环境影响评价文件的审批</td> 
          <td class="text-center">-</td> 
          <td class="text-center">-</td> 
          <td>上海市环境保护局</td> 
          <td>06060001164A44C00F0040CA8A421AB7E17CE4A2</td> 
         </tr> 
         <tr> 
         </tr>
         <tr>
          <td class="tx">6</td> 
          <td>杨环保许评[2016]085号</td> 
          <td>建设项目环境影响评价文件的审批</td> 
          <td class="text-center">-</td> 
          <td class="text-center">-</td> 
          <td>上海市环境保护局</td> 
          <td>06060001FCF2CD281A3B4FE7AE2E17C14871B914</td> 
         </tr> 
         <tr> 
         </tr>
         <tr>
          <td class="tx">7</td> 
          <td>黄环保许管[2016]78号</td> 
          <td>建设项目环境影响评价文件的审批</td> 
          <td class="text-center">-</td> 
          <td class="text-center">-</td> 
          <td>上海市环境保护局</td> 
          <td>060600010497C14AC0AD4A92927D8BD14D704048</td> 
         </tr> 
         <tr> 
         </tr>
         <tr>
          <td class="tx">8</td> 
          <td>沪浦环保许评[2015]2948号</td> 
          <td>建设项目环境影响评价文件的审批</td> 
          <td class="text-center">-</td> 
          <td class="text-center">-</td> 
          <td>上海市环境保护局</td> 
          <td>06060001B26B406488C54E6C993DD821AECB9B1F</td> 
         </tr> 
         <tr> 
         </tr>
         <tr>
          <td class="tx">9</td> 
          <td>沪浦环保许评[2015]1215号</td> 
          <td>建设项目环境影响评价文件的审批</td> 
          <td class="text-center">-</td> 
          <td class="text-center">-</td> 
          <td>上海市环境保护局</td> 
          <td>0606000122FF30A45D6E4BE1A76BEBB9401407EB</td> 
         </tr> 
         <tr> 
         </tr>
         <tr>
          <td class="tx">10</td> 
          <td>长环评工商[2016]41号</td> 
          <td>建设项目环境影响评价文件的审批</td> 
          <td class="text-center">-</td> 
          <td class="text-center">-</td> 
          <td>上海市环境保护局</td> 
          <td>060600012CB7535287274463B7FA8D7A49F605E3</td> 
         </tr> 
        </tbody>
       </table> 
       <div> 
        <nav class="text-right"> 
         <ul class="pagination"> 
          <li class="active"><a htef="#">1</a></li>
          <li><a id="ajaxpage" href="javascript:getTabList(2,&quot;run&quot;,&quot;licens&quot;)">2</a></li>
          <li><a id="ajaxpage" href="javascript:getTabList(3,&quot;run&quot;,&quot;licens&quot;)">3</a></li>
          <li><a id="ajaxpage" href="javascript:getTabList(4,&quot;run&quot;,&quot;licens&quot;)">4</a></li> 
          <li><a id="ajaxpage" href="javascript:getTabList(2,&quot;run&quot;,&quot;licens&quot;)">&gt;</a></li> 
         </ul> 
        </nav> 
       </div> 
      </section> 
      <section class="panel clear b-a"> 
       <div class="tcaption"> 
        <span class="title"> 行政许可 [信用中国]</span> 
        <span class="tbadge">15</span> 
        <span class="thist">（查看更多10条 <a onclick="jumpHistory('hisxzxk')">历史行政许可</a>）</span> 
        <span class="watermark"></span> 
       </div> 
       <table class="ntable ntable-odd"> 
        <tbody>
         <tr>
          <th class="tx">序号</th>
          <th>决定文书号</th>
          <th>许可机关</th> 
          <th>决定日期</th>
          <th>操作</th> 
         </tr> 
         <tr> 
         </tr>
         <tr>
          <td class="tx">1</td> 
          <td class="text-center">沪114环保许管[2018]55号</td> 
          <td class="text-center"> 上海市嘉定区环境保护局 </td> 
          <td width="103"> 2018-03-02 </td> 
          <td width="90" class="text-center"> <a class="ma_court c-max600" data-toggle="modal" data-target="#xkModal" onclick="xzxukeView(&quot;edba11595b78f696ea383a3281b66ad1_7&quot;)"> 查看详情 </a> </td> 
         </tr> 
         <tr> 
         </tr>
         <tr>
          <td class="tx">2</td> 
          <td class="text-center">沪国税浦许准字〔2018〕第1907号</td> 
          <td class="text-center"> 浦东新区税务局 </td> 
          <td width="103"> 2018-02-09 </td> 
          <td width="90" class="text-center"> <a class="ma_court c-max600" data-toggle="modal" data-target="#xkModal" onclick="xzxukeView(&quot;b9639b95bf1cb66934b15c3486893dd4_7&quot;)"> 查看详情 </a> </td> 
         </tr> 
         <tr> 
         </tr>
         <tr>
          <td class="tx">3</td> 
          <td class="text-center">-</td> 
          <td class="text-center"> 上海市浦东新区税务局第二十一税务所 </td> 
          <td width="103"> 2018-02-08 </td> 
          <td width="90" class="text-center"> <a class="ma_court c-max600" data-toggle="modal" data-target="#xkModal" onclick="xzxukeView(&quot;94fd533e7381cbbb6af5b1d697b71ef7_7&quot;)"> 查看详情 </a> </td> 
         </tr> 
         <tr> 
         </tr>
         <tr>
          <td class="tx">4</td> 
          <td class="text-center">ljz201701619</td> 
          <td class="text-center"> 中国（上海）自由贸易试验区管理委员会 </td> 
          <td width="103"> 2017-10-17 </td> 
          <td width="90" class="text-center"> <a class="ma_court c-max600" data-toggle="modal" data-target="#xkModal" onclick="xzxukeView(&quot;f13aa59a4fbd863500ab990bfb26b9db_7&quot;)"> 查看详情 </a> </td> 
         </tr> 
         <tr> 
         </tr>
         <tr>
          <td class="tx">5</td> 
          <td class="text-center">LJZ201701487</td> 
          <td class="text-center"> 中国（上海）自由贸易试验区管理委员会 </td> 
          <td width="103"> 2017-09-18 </td> 
          <td width="90" class="text-center"> <a class="ma_court c-max600" data-toggle="modal" data-target="#xkModal" onclick="xzxukeView(&quot;bf727f4e684af3dd509889a37782d94d_7&quot;)"> 查看详情 </a> </td> 
         </tr> 
         <tr> 
         </tr>
         <tr>
          <td class="tx">6</td> 
          <td class="text-center">松环保许管[2017]1857号</td> 
          <td class="text-center"> 松江区环保局 </td> 
          <td width="103"> 2017-09-12 </td> 
          <td width="90" class="text-center"> <a class="ma_court c-max600" data-toggle="modal" data-target="#xkModal" onclick="xzxukeView(&quot;37f6d4439e2872f0d7e8703fba31cc3c_7&quot;)"> 查看详情 </a> </td> 
         </tr> 
         <tr> 
         </tr>
         <tr>
          <td class="tx">7</td> 
          <td class="text-center">LJZ201701157</td> 
          <td class="text-center"> 中国（上海）自由贸易试验区管理委员会 </td> 
          <td width="103"> 2017-07-25 </td> 
          <td width="90" class="text-center"> <a class="ma_court c-max600" data-toggle="modal" data-target="#xkModal" onclick="xzxukeView(&quot;acc5952b904bae4c217bc9f76f962e11_7&quot;)"> 查看详情 </a> </td> 
         </tr> 
         <tr> 
         </tr>
         <tr>
          <td class="tx">8</td> 
          <td class="text-center">松环保许管[2017]1476号</td> 
          <td class="text-center"> 松江区环保局 </td> 
          <td width="103"> 2017-07-24 </td> 
          <td width="90" class="text-center"> <a class="ma_court c-max600" data-toggle="modal" data-target="#xkModal" onclick="xzxukeView(&quot;46fc950909225362a8f579af08702c94_7&quot;)"> 查看详情 </a> </td> 
         </tr> 
         <tr> 
         </tr>
         <tr>
          <td class="tx">9</td> 
          <td class="text-center">普环保验[2017]85号</td> 
          <td class="text-center"> 普陀区环境保护局 </td> 
          <td width="103"> 2017-07-04 </td> 
          <td width="90" class="text-center"> <a class="ma_court c-max600" data-toggle="modal" data-target="#xkModal" onclick="xzxukeView(&quot;79b7828a346efde6f887b16c223d873b_7&quot;)"> 查看详情 </a> </td> 
         </tr> 
         <tr> 
         </tr>
         <tr>
          <td class="tx">10</td> 
          <td class="text-center">jy13101150257400</td> 
          <td class="text-center"> 上海市浦东新区市场监督管理局 </td> 
          <td width="103"> 2017-06-09 </td> 
          <td width="90" class="text-center"> <a class="ma_court c-max600" data-toggle="modal" data-target="#xkModal" onclick="xzxukeView(&quot;089701547b7954658d8063a04a837056_7&quot;)"> 查看详情 </a> </td> 
         </tr> 
         <tr> 
         </tr>
         <tr>
          <td class="tx">11</td> 
          <td class="text-center">JY13101150257400</td> 
          <td class="text-center"> 上海市浦东新区市场监督管理局 </td> 
          <td width="103"> 2017-06-09 </td> 
          <td width="90" class="text-center"> <a class="ma_court c-max600" data-toggle="modal" data-target="#xkModal" onclick="xzxukeView(&quot;a4795e16b74fa6388607619c9b947517_7&quot;)"> 查看详情 </a> </td> 
         </tr> 
         <tr> 
         </tr>
         <tr>
          <td class="tx">12</td> 
          <td class="text-center">LJZ201700657</td> 
          <td class="text-center"> 中国（上海）自由贸易试验区管理委员会 </td> 
          <td width="103"> 2017-05-03 </td> 
          <td width="90" class="text-center"> <a class="ma_court c-max600" data-toggle="modal" data-target="#xkModal" onclick="xzxukeView(&quot;0f757374acbb131a40c390ca15d95aaf_7&quot;)"> 查看详情 </a> </td> 
         </tr> 
         <tr> 
         </tr>
         <tr>
          <td class="tx">13</td> 
          <td class="text-center">-</td> 
          <td class="text-center"> 上海市浦东新区税务局第二十一税务所 </td> 
          <td width="103"> 2017-03-03 </td> 
          <td width="90" class="text-center"> <a class="ma_court c-max600" data-toggle="modal" data-target="#xkModal" onclick="xzxukeView(&quot;5cc8f741bcbc8f9685dc4d2615672a10_7&quot;)"> 查看详情 </a> </td> 
         </tr> 
         <tr> 
         </tr>
         <tr>
          <td class="tx">14</td> 
          <td class="text-center">LJZ201700200</td> 
          <td class="text-center"> 中国（上海）自由贸易试验区管理委员会 </td> 
          <td width="103"> 2017-02-10 </td> 
          <td width="90" class="text-center"> <a class="ma_court c-max600" data-toggle="modal" data-target="#xkModal" onclick="xzxukeView(&quot;692920236138e85c6177aa030e0d37ab_7&quot;)"> 查看详情 </a> </td> 
         </tr> 
         <tr> 
         </tr>
         <tr>
          <td class="tx">15</td> 
          <td class="text-center">普环保审[2016]33号</td> 
          <td class="text-center"> 上海市普陀区环境保护局 </td> 
          <td width="103"> 2016-07-21 </td> 
          <td width="90" class="text-center"> <a class="ma_court c-max600" data-toggle="modal" data-target="#xkModal" onclick="xzxukeView(&quot;fd53bf4cca92a7fe922a77838f55059f_7&quot;)"> 查看详情 </a> </td> 
         </tr> 
        </tbody>
       </table> 
      </section> 
      <section class="panel clear  b-a" id="taxCreditList"> 
       <div class="tcaption"> 
        <h3 class="title"> 税务信用</h3> 
        <span class="tbadge">1</span> 
        <span class="watermark"></span> 
       </div> 
       <table class="ntable ntable-odd"> 
        <tbody>
         <tr>
          <th class="tx">序号</th>
          <th>评价年度</th>
          <th>纳税人识别号</th>
          <th>纳税信用等级</th> 
          <th>评价单位</th> 
         </tr> 
         <tr> 
         </tr>
         <tr>
          <td class="tx">1</td> 
          <td class="text-center">2018</td> 
          <td class="text-center">91310115342050446K</td> 
          <td class="text-center">A</td> 
          <td class="text-center">国家税务总局</td> 
         </tr> 
        </tbody>
       </table> 
      </section> 
      <section class="panel b-a" id="tenderlist"> 
       <div class="tcaption"> 
        <h3 class="title">招投标信息</h3> 
        <span class="tbadge">1</span> 
        <span class="watermark"></span> 
       </div> 
       <table class="ntable ntable-odd"> 
        <tbody> 
         <tr> 
          <th class="tx">序号</th> 
          <th>描述</th> 
          <th>发布时间</th> 
          <th>所属地区</th> 
          <th>项目分类</th> 
         </tr> 
         <tr> 
          <td class="tx"> 1 </td> 
          <td style="width:50%"> <a data-toggle="modal" data-target="#tenderModal" onclick="tenderview('0c394ee110bdb2dbf46fe26345374f32')" class="text-blue">[吴忠市][论证公告]盐池县人民政府与盒马公司战略签约仪式暨“盐池滩羊”品牌盒马全国十城门店活动推广宣传项目单一来源论证公示</a> </td> 
          <td width="103"> 2018-09-17 </td> 
          <td width="100" class="text-center"> 宁夏</td> 
          <td class="text-center">采购公告</td> 
         </tr> 
        </tbody> 
       </table> 
       <div> 
       </div> 
      </section> 
      <section class="panel b-a clear"> 
       <div class="tcaption  m-t"> 
        <h3 class="title">招聘统计分析</h3> 
        <a class="hchart" onclick="hideChart(this)" href="javascript:;"> <span>收起</span> <i class="i i-arrow-up4"></i> </a> 
       </div> 
       <div class="float-wrap"> 
        <div class="col-sm-6 col-xs-12 no-padding">
         <div id="PieSal" class="nchart-item" _echarts_instance_="ec_1557911544289" style="-webkit-tap-highlight-color: transparent; user-select: none; position: relative; background: transparent;">
          <div style="position: relative; overflow: hidden; width: 436px; height: 258px;">
           <canvas width="523" height="309" data-zr-dom-id="zr_0" style="position: absolute; left: 0px; top: 0px; width: 436px; height: 258px; user-select: none; -webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></canvas>
          </div>
          <div></div>
         </div>
        </div> 
        <div class="col-sm-6 col-xs-12 no-padding" style="padding-left: 7px;">
         <div id="PieArea" class="nchart-item" _echarts_instance_="ec_1557911544290" style="-webkit-tap-highlight-color: transparent; user-select: none; position: relative; background: transparent;">
          <div style="position: relative; overflow: hidden; width: 436px; height: 258px;">
           <canvas width="523" height="309" data-zr-dom-id="zr_0" style="position: absolute; left: 0px; top: 0px; width: 436px; height: 258px; user-select: none; -webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></canvas>
          </div>
          <div></div>
         </div>
        </div> 
        <div class="col-sm-6 col-xs-12 no-padding">
         <div id="PieEdu" class="nchart-item" _echarts_instance_="ec_1557911544291" style="-webkit-tap-highlight-color: transparent; user-select: none; position: relative; background: rgb(255, 255, 255);">
          <div style="position: relative; overflow: hidden; width: 436px; height: 258px;">
           <canvas width="523" height="309" data-zr-dom-id="zr_0" style="position: absolute; left: 0px; top: 0px; width: 436px; height: 258px; user-select: none; -webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></canvas>
          </div>
          <div></div>
         </div>
        </div> 
        <div class="col-sm-6 col-xs-12 no-padding" style="padding-left: 7px;">
         <div id="PieExp" class="nchart-item" _echarts_instance_="ec_1557911544292" style="-webkit-tap-highlight-color: transparent; user-select: none; position: relative; background: transparent;">
          <div style="position: relative; overflow: hidden; width: 436px; height: 258px;">
           <canvas width="523" height="309" data-zr-dom-id="zr_0" style="position: absolute; left: 0px; top: 0px; width: 436px; height: 258px; user-select: none; -webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></canvas>
          </div>
          <div></div>
         </div>
        </div> 
       </div> 
      </section> 
      <section class="panel clear b-a" id="joblist"> 
       <div class="tcaption"> 
        <h3 class="title">招聘</h3> 
        <span class="tbadge">1776</span> 
        <span class="watermark"></span> 
       </div> 
       <table class="ntable ntable-odd"> 
        <tbody> 
         <tr> 
          <th>序号</th> 
          <th>发布时间</th> 
          <th>招聘职位</th> 
          <th>月薪</th> 
          <th>学历</th> 
          <th>经验</th> 
          <th>所在城市</th> 
         </tr> 
         <tr> 
          <td class="tx">1</td> 
          <td width="103"> 2019-05-13 </td> 
          <td> <a href="/jobdetail_e89e842cf32fbd1bf4d9d72790010768">盒马鲜生店员</a> </td> 
          <td width="140" class="text-center"> 3000-5000 </td> 
          <td width="100" class="text-center"> 不限 </td> 
          <td width="140" class="text-center"> 不限 </td> 
          <td width="120" class="text-center"> 上海 </td> 
         </tr> 
         <tr> 
          <td class="tx">2</td> 
          <td width="103"> 2019-05-13 </td> 
          <td> <a href="/jobdetail_efb337d180a3e6357fc8edd2cd421782">盒马APP体验设计专家</a> </td> 
          <td width="140" class="text-center"> 25000-35000 </td> 
          <td width="100" class="text-center"> 本科 </td> 
          <td width="140" class="text-center"> 5-10年 </td> 
          <td width="120" class="text-center"> 上海 </td> 
         </tr> 
         <tr> 
          <td class="tx">3</td> 
          <td width="103"> 2019-05-13 </td> 
          <td> <a href="/jobdetail_4c6a76d1b3eb01b4e22030902c4cbeec">盒马鲜生店员</a> </td> 
          <td width="140" class="text-center"> 3000-5000 </td> 
          <td width="100" class="text-center"> 不限 </td> 
          <td width="140" class="text-center"> 不限 </td> 
          <td width="120" class="text-center"> 上海 </td> 
         </tr> 
         <tr> 
          <td class="tx">4</td> 
          <td width="103"> 2019-05-13 </td> 
          <td> <a href="/jobdetail_b15fd6eb5a97db8d6094025dec79606b">盒马鲜生店员</a> </td> 
          <td width="140" class="text-center"> 3000-5000 </td> 
          <td width="100" class="text-center"> 不限 </td> 
          <td width="140" class="text-center"> 不限 </td> 
          <td width="120" class="text-center"> 上海 </td> 
         </tr> 
         <tr> 
          <td class="tx">5</td> 
          <td width="103"> 2019-05-13 </td> 
          <td> <a href="/jobdetail_7850e04ac5450130d25322bf16220d84">盒马鲜生店员</a> </td> 
          <td width="140" class="text-center"> 3000-5000 </td> 
          <td width="100" class="text-center"> 不限 </td> 
          <td width="140" class="text-center"> 不限 </td> 
          <td width="120" class="text-center"> 上海 </td> 
         </tr> 
         <tr> 
          <td class="tx">6</td> 
          <td width="103"> 2019-05-13 </td> 
          <td> <a href="/jobdetail_d7c67e9dc5561d7921f45046780714bd">盒马鲜生店员</a> </td> 
          <td width="140" class="text-center"> 3000-5000 </td> 
          <td width="100" class="text-center"> 不限 </td> 
          <td width="140" class="text-center"> 不限 </td> 
          <td width="120" class="text-center"> 上海 </td> 
         </tr> 
         <tr> 
          <td class="tx">7</td> 
          <td width="103"> 2019-05-13 </td> 
          <td> <a href="/jobdetail_fa6e89c61f9510cc4d739a30e40a8146">盒马鲜生店员</a> </td> 
          <td width="140" class="text-center"> 3000-5000 </td> 
          <td width="100" class="text-center"> 不限 </td> 
          <td width="140" class="text-center"> 不限 </td> 
          <td width="120" class="text-center"> 上海 </td> 
         </tr> 
         <tr> 
          <td class="tx">8</td> 
          <td width="103"> 2019-05-13 </td> 
          <td> <a href="/jobdetail_34b8252acc4c20af25b75273f6378c14">盒马鲜生店员</a> </td> 
          <td width="140" class="text-center"> 3000-5000 </td> 
          <td width="100" class="text-center"> 不限 </td> 
          <td width="140" class="text-center"> 不限 </td> 
          <td width="120" class="text-center"> 上海 </td> 
         </tr> 
         <tr> 
          <td class="tx">9</td> 
          <td width="103"> 2019-05-13 </td> 
          <td> <a href="/jobdetail_2d1e8404fd554797aa65a77fc4e88b30">盒马鲜生店员</a> </td> 
          <td width="140" class="text-center"> 3000-5000 </td> 
          <td width="100" class="text-center"> 不限 </td> 
          <td width="140" class="text-center"> 不限 </td> 
          <td width="120" class="text-center"> 上海 </td> 
         </tr> 
         <tr> 
          <td class="tx">10</td> 
          <td width="103"> 2019-05-13 </td> 
          <td> <a href="/jobdetail_ba7df42b14804c06c467983dd6164ec7">盒马鲜生店员</a> </td> 
          <td width="140" class="text-center"> 3000-5000 </td> 
          <td width="100" class="text-center"> 不限 </td> 
          <td width="140" class="text-center"> 不限 </td> 
          <td width="120" class="text-center"> 上海 </td> 
         </tr> 
        </tbody> 
       </table> 
       <div> 
        <nav class="text-right"> 
         <ul class="pagination"> 
          <li class="active"><a htef="#">1</a></li>
          <li><a id="ajaxpage" href="javascript:getTabList(2,&quot;run&quot;,&quot;job&quot;)">2</a></li>
          <li><a id="ajaxpage" href="javascript:getTabList(3,&quot;run&quot;,&quot;job&quot;)">3</a></li>
          <li><a id="ajaxpage" href="javascript:getTabList(4,&quot;run&quot;,&quot;job&quot;)">4</a></li>
          <li><a id="ajaxpage" href="javascript:getTabList(5,&quot;run&quot;,&quot;job&quot;)">5</a></li>
          <li><a id="ajaxpage" href="javascript:getTabList(6,&quot;run&quot;,&quot;job&quot;)">6</a></li> 
          <li><a id="ajaxpage" href="javascript:getTabList(2,&quot;run&quot;,&quot;job&quot;)">&gt;</a></li> 
          <li><a id="ajaxpage" href="javascript:getTabList(178,&quot;run&quot;,&quot;job&quot;)"> ...178</a></li> 
         </ul> 
        </nav> 
       </div> 
      </section> 
      <div id="financean"></div> 
      <section class="panel clear b-a" id="weibolist"> 
       <div class="tcaption"> 
        <h3 class="title">微博</h3> 
        <span class="tbadge">2</span> 
        <span class="watermark"></span> 
       </div> 
       <table class="ntable ntable-odd"> 
        <tbody> 
         <tr> 
          <th class="tx">序号</th> 
          <th width="90">头像</th> 
          <th width="140">微博昵称</th> 
          <th width="200">行业类别</th> 
          <th>简介</th> 
         </tr> 
         <tr> 
          <td class="tx"> 1 </td> 
          <td width="90" class="text-center"> <img style="width: 66px;" src="http://img.qichacha.com/Weibo/logo/676d5b8b5ea4d5222039a782e529c68c.jpg" onerror="this.src='/material/theme/chacha/cms/v2/images/no_image.png'" /> </td> 
          <td width="140" class="text-center"> <a href="https://weibo.com/u/3655891783" target="_blank" rel="nofollow">盒鲜姑</a> </td> 
          <td width="200" class="text-center"> 吃喝玩乐睡,读书饮酒茶 </td> 
          <td> 最好金龟换酒,相与醉沧州。 </td> 
         </tr> 
         <tr> 
          <td class="tx"> 2 </td> 
          <td width="90" class="text-center"> <img style="width: 66px;" src="http://img.qichacha.com/Weibo/logo/fe4a33213c3cbf396f8195e22e953a02.jpg" onerror="this.src='/material/theme/chacha/cms/v2/images/no_image.png'" /> </td> 
          <td width="140" class="text-center"> <a href="https://weibo.com/hemabrand" target="_blank" rel="nofollow">盒马</a> </td> 
          <td width="200" class="text-center"> - </td> 
          <td> - </td> 
         </tr> 
        </tbody> 
       </table> 
       <div> 
       </div> 
      </section> 
      <section class="panel b-a clear" style=""> 
       <div class="tcaption  m-t"> 
        <h3 class="title">新闻舆情统计分析</h3> 
        <a class="hchart" onclick="hideChart(this)" href="javascript:;"> <span>收起</span> <i class="i i-arrow-up4"></i> </a> 
       </div> 
       <div class="float-wrap"> 
        <div class="col-sm-6 col-xs-12 no-padding">
         <div class="nchart-item-title">
          舆情情感类型占比
         </div>
         <div id="type-chart" class="nchart-item hmd" _echarts_instance_="ec_1557911544873" style="-webkit-tap-highlight-color: transparent; user-select: none;">
          <div style="position: relative; overflow: hidden; width: 436px; height: 298px; padding: 0px; margin: 0px; border-width: 0px;">
           <canvas data-zr-dom-id="zr_0" width="523" height="357" style="position: absolute; left: 0px; top: 0px; width: 436px; height: 298px; user-select: none; -webkit-tap-highlight-color: rgba(0, 0, 0, 0); padding: 0px; margin: 0px; border-width: 0px;"></canvas>
          </div>
         </div>
        </div> 
        <div class="col-sm-6 col-xs-12 no-padding" style="padding-left: 7px;"> 
         <div class="nchart-item-title">
          新闻舆情趋势
         </div> 
         <div id="trend-chart" class="nchart-item hmd" _echarts_instance_="ec_1557911544876" style="-webkit-tap-highlight-color: transparent; user-select: none;">
          <div style="position: relative; overflow: hidden; width: 436px; height: 298px; padding: 0px; margin: 0px; border-width: 0px;">
           <canvas data-zr-dom-id="zr_0" width="523" height="357" style="position: absolute; left: 0px; top: 0px; width: 436px; height: 298px; user-select: none; -webkit-tap-highlight-color: rgba(0, 0, 0, 0); padding: 0px; margin: 0px; border-width: 0px;"></canvas>
          </div>
         </div> 
        </div> 
        <div class="col-sm-6 col-xs-12 no-padding">
         <div class="nchart-item-title">
          近期媒体印象
         </div>
         <div id="cloud-chart" class="nchart-item hmd" _echarts_instance_="ec_1557911544875" style="-webkit-tap-highlight-color: transparent; user-select: none;">
          <div style="position: relative; overflow: hidden; width: 436px; height: 298px; padding: 0px; margin: 0px; border-width: 0px;">
           <canvas data-zr-dom-id="zr_0" width="523" height="357" style="position: absolute; left: 0px; top: 0px; width: 436px; height: 298px; user-select: none; -webkit-tap-highlight-color: rgba(0, 0, 0, 0); padding: 0px; margin: 0px; border-width: 0px;"></canvas>
          </div>
         </div>
        </div> 
        <div class="col-sm-6 col-xs-12 no-padding" style="padding-left: 7px;"> 
         <div class="nchart-item-title">
          新闻类型分布 TOP10
         </div> 
         <div id="category-chart" class="nchart-item hmd" _echarts_instance_="ec_1557911544874" style="-webkit-tap-highlight-color: transparent; user-select: none;">
          <div style="position: relative; overflow: hidden; width: 436px; height: 298px; padding: 0px; margin: 0px; border-width: 0px;">
           <canvas data-zr-dom-id="zr_0" width="523" height="357" style="position: absolute; left: 0px; top: 0px; width: 436px; height: 298px; user-select: none; -webkit-tap-highlight-color: rgba(0, 0, 0, 0); padding: 0px; margin: 0px; border-width: 0px;"></canvas>
          </div>
         </div> 
        </div> 
       </div> 
      </section> 
      <div id="newslistByjob" style="position: relative;top: -40px;"></div> 
      <section class="panel clear b-a" id="newslist"> 
       <div class="c_split_10"></div> 
       <div class="tcaption"> 
        <span class="title">新闻舆情</span> 
        <span class="tbadge">4992</span> 
        <div class="chooseRun" data-box="news" style="float: right"> 
         <div class="tdrop"> 
          <span class="btn" data-toggle="dropdown"> <span class="newstags">类别不限</span> <span class="caret m-l"></span> </span> 
          <ul class="dropdown-menu dropdown-menu-right"> 
           <li><a href="javascript:;" data-option="tags" data-value="">不限</a></li> 
           <li><a href="javascript:;" data-option="tags" data-value="1100">高管违法(4)</a></li> 
           <li><a href="javascript:;" data-option="tags" data-value="1200">高管变动(80)</a></li> 
           <li><a href="javascript:;" data-option="tags" data-value="2000">违法违纪(111)</a></li> 
           <li><a href="javascript:;" data-option="tags" data-value="2100">造假欺诈(64)</a></li> 
           <li><a href="javascript:;" data-option="tags" data-value="2200">贪污受贿(3)</a></li> 
           <li><a href="javascript:;" data-option="tags" data-value="2300">违纪违规(94)</a></li> 
           <li><a href="javascript:;" data-option="tags" data-value="2400">垄断信息(6)</a></li> 
           <li><a href="javascript:;" data-option="tags" data-value="2600">安全事故(20)</a></li> 
           <li><a href="javascript:;" data-option="tags" data-value="2700">司法纠纷(1)</a></li> 
           <li><a href="javascript:;" data-option="tags" data-value="2800">侵权抄袭(29)</a></li> 
           <li><a href="javascript:;" data-option="tags" data-value="2900">偷税漏税(1)</a></li> 
           <li><a href="javascript:;" data-option="tags" data-value="3100">上市退市(77)</a></li> 
           <li><a href="javascript:;" data-option="tags" data-value="3200">亏损盈利(1254)</a></li> 
           <li><a href="javascript:;" data-option="tags" data-value="3300">投资融资(818)</a></li> 
           <li><a href="javascript:;" data-option="tags" data-value="3400">收购重组(141)</a></li> 
           <li><a href="javascript:;" data-option="tags" data-value="3500">停业破产(51)</a></li> 
           <li><a href="javascript:;" data-option="tags" data-value="3600">股权变动(89)</a></li> 
           <li><a href="javascript:;" data-option="tags" data-value="3700">增持减持(9)</a></li> 
           <li><a href="javascript:;" data-option="tags" data-value="3800">债务抵押(3)</a></li> 
           <li><a href="javascript:;" data-option="tags" data-value="4000">成果信誉(186)</a></li> 
           <li><a href="javascript:;" data-option="tags" data-value="5000">产品相关(588)</a></li> 
           <li><a href="javascript:;" data-option="tags" data-value="0000">其他(2347)</a></li> 
          </ul> 
         </div> 
         <div class="tdrop"> 
          <span class="btn" data-toggle="dropdown"> <span class="newsimpact">情感不限</span> <span class="caret m-l"></span> </span> 
          <ul class="dropdown-menu dropdown-menu-right"> 
           <li><a href="javascript:;" data-option="impact" data-value="">不限</a></li> 
           <li><a href="javascript:;" data-option="impact" data-value="negative">消极(628)</a></li> 
           <li><a href="javascript:;" data-option="impact" data-value="none">中立(1323)</a></li> 
           <li><a href="javascript:;" data-option="impact" data-value="positive">积极(3041)</a></li> 
          </ul> 
         </div> 
        </div> 
        <span class="watermark"></span> 
       </div> 
       <table class="ntable ntable-list"> 
        <tbody>
         <tr>
          <td> <a href="/postnews_c5c8d107a0d5833b280f78617aca4ede.html" target="_blank" class="clearfix"> 
            <div> 
             <div class="news-impact-title"> 
              <span class="news-impact default">中立</span> 
              <span class="title">菜市场新“战事”：消费者、摊主、菜贩的变与不变</span> 
             </div> 
             <div class="news-tag clearfix"> 
              <span>#亏损盈利</span> 
              <span>#生鲜</span> 
              <span>#每日优鲜</span> 
              <span>#蔬果</span> 
              <span>#配送</span> 
              <span>#菜市场</span> 
             </div> 
             <small class="clear subtitle m-t-lg"> <label>来源：</label> 新浪网 <span class="pull-right"><label>发布时间：</label> 1小时前 </span> </small> 
            </div> </a> </td>
         </tr> 
         <tr>
          <td> <a href="/postnews_10f6f1d6f5b1733309292998471980a3.html" target="_blank" class="clearfix"> 
            <div> 
             <div class="news-impact-title"> 
              <span class="news-impact default">中立</span> 
              <span class="title">盒马模式走入死胡同</span> 
             </div> 
             <div class="news-tag clearfix"> 
              <span>#新零售</span> 
              <span>#盒马鲜生</span> 
              <span>#地段</span> 
              <span>#门店</span> 
              <span>#风口</span> 
             </div> 
             <small class="clear subtitle m-t-lg"> <label>来源：</label> 东方财富网 <span class="pull-right"><label>发布时间：</label> 2小时前 </span> </small> 
            </div> </a> </td>
         </tr> 
         <tr>
          <td> <a href="/postnews_5fb4530b107cff3e9dc36fddc608ea31.html" target="_blank" class="clearfix"> 
            <div> 
             <div class="news-impact-title"> 
              <span class="news-impact default">中立</span> 
              <span class="title">福建80后最爱上网买菜&nbsp;传统商超踊跃“入淘”</span> 
             </div> 
             <div class="news-tag clearfix"> 
              <span>#新华都</span> 
              <span>#门店</span> 
              <span>#订单量</span> 
              <span>#占比</span> 
              <span>#商超</span> 
             </div> 
             <small class="clear subtitle m-t-lg"> <label>来源：</label> 人民网福建频道 <span class="pull-right"><label>发布时间：</label> 2小时前 </span> </small> 
            </div> </a> </td>
         </tr> 
         <tr>
          <td> <a href="/postnews_77f855c966f306b471b6f8de5a42588b.html" target="_blank" class="clearfix"> 
            <div> 
             <div class="news-impact-title"> 
              <span class="news-impact default">中立</span> 
              <span class="title">今日食事热点：光明莫斯利安推减肥酸奶、百威遭欧盟罚款</span> 
             </div> 
             <div class="news-tag clearfix"> 
              <span>#亏损盈利</span> 
              <span>#产品相关</span> 
              <span>#Vivera</span> 
              <span>#亿滋</span> 
              <span>#澳优</span> 
              <span>#西王集团</span> 
              <span>#营业收入</span> 
             </div> 
             <small class="clear subtitle m-t-lg"> <label>来源：</label> 食品商务网 <span class="pull-right"><label>发布时间：</label> 3小时前 </span> </small> 
            </div> </a> </td>
         </tr> 
         <tr>
          <td> <a href="/postnews_4ad5c4c360afa5e200ae89ea435b64bb.html" target="_blank" class="clearfix"> 
            <div> 
             <div class="news-impact-title"> 
              <span class="news-impact default">中立</span> 
              <span class="title">马化腾与王健林一起逛街，醉翁之意在新零售</span> 
             </div> 
             <div class="news-tag clearfix"> 
              <span>#成果信誉</span> 
              <span>#新零售</span> 
              <span>#万达广场</span> 
              <span>#腾讯</span> 
              <span>#智慧零售</span> 
              <span>#王健林</span> 
             </div> 
             <small class="clear subtitle m-t-lg"> <label>来源：</label> 百家号 <span class="pull-right"><label>发布时间：</label> 5小时前 </span> </small> 
            </div> </a> </td>
         </tr> 
         <tr>
          <td> <a href="/postnews_2b6a71edf544cb02b00dc2197e3927b5.html" target="_blank" class="clearfix"> 
            <div> 
             <div class="news-impact-title"> 
              <span class="news-impact">积极</span> 
              <span class="title">厉害了！潍坊两企业入围2018年中国连锁百强</span> 
             </div> 
             <div class="news-tag clearfix"> 
              <span>#亏损盈利</span> 
              <span>#成果信誉</span> 
              <span>#占比</span> 
              <span>#集团</span> 
              <span>#潍坊</span> 
              <span>#线上</span> 
              <span>#苏宁</span> 
             </div> 
             <small class="clear subtitle m-t-lg"> <label>来源：</label> 大众网山东频道 <span class="pull-right"><label>发布时间：</label> 7小时前 </span> </small> 
            </div> </a> </td>
         </tr> 
         <tr>
          <td> <a href="/postnews_3b23ac4a033210a78b17cd3034b153b9.html" target="_blank" class="clearfix"> 
            <div> 
             <div class="news-impact-title"> 
              <span class="news-impact">积极</span> 
              <span class="title">腾讯下注，阿里旁观，社区团购的下一站是Costco？</span> 
             </div> 
             <div class="news-tag clearfix"> 
              <span>#投资融资</span> 
              <span>#团长</span> 
              <span>#腾讯</span> 
              <span>#生鲜</span> 
              <span>#引流</span> 
              <span>#赛道</span> 
             </div> 
             <small class="clear subtitle m-t-lg"> <label>来源：</label> 北京瑟风网 <span class="pull-right"><label>发布时间：</label> 7小时前 </span> </small> 
            </div> </a> </td>
         </tr> 
         <tr>
          <td> <a href="/postnews_0fe60339eb9c5c0a37e7462d6ce813b2.html" target="_blank" class="clearfix"> 
            <div> 
             <div class="news-impact-title"> 
              <span class="news-impact default">中立</span> 
              <span class="title">盒马鲜生北京红莲店升级为盒马菜市</span> 
             </div> 
             <div class="news-tag clearfix"> 
              <span>#亏损盈利</span> 
              <span>#盒马鲜生</span> 
              <span>#门店</span> 
              <span>#浙海华地</span> 
              <span>#改造</span> 
              <span>#首店</span> 
             </div> 
             <small class="clear subtitle m-t-lg"> <label>来源：</label> 龙商网 <span class="pull-right"><label>发布时间：</label> 17小时前 </span> </small> 
            </div> </a> </td>
         </tr> 
         <tr>
          <td> <a href="/postnews_f4ad8586bdfee974e2f6067c10a4b1ce.html" target="_blank" class="clearfix"> 
            <div> 
             <div class="news-impact-title"> 
              <span class="news-impact default">中立</span> 
              <span class="title">当年轻人不再出门买菜，互联网菜场的好日子来了</span> 
             </div> 
             <div class="news-tag clearfix"> 
              <span>#亏损盈利</span> 
              <span>#投资融资</span> 
              <span>#叮咚买菜</span> 
              <span>#每日优鲜</span> 
              <span>#配送员</span> 
              <span>#饿了么</span> 
              <span>#陈晓</span> 
             </div> 
             <small class="clear subtitle m-t-lg"> <label>来源：</label> 微信公众号 <span class="pull-right"><label>发布时间：</label> 19小时前 </span> </small> 
            </div> </a> </td>
         </tr> 
         <tr>
          <td> <a href="/postnews_96ff646ff711ccb67d4498c9e331b2b7.html" target="_blank" class="clearfix"> 
            <div> 
             <div class="news-impact-title"> 
              <span class="news-impact default">中立</span> 
              <span class="title">为什么传统超市越学盒马，业绩越不咋地？</span> 
             </div> 
             <div class="news-tag clearfix"> 
              <span>#亏损盈利</span> 
              <span>#高鑫零售</span> 
              <span>#永辉</span> 
              <span>#人人乐</span> 
              <span>#营收</span> 
              <span>#卜蜂莲花</span> 
             </div> 
             <small class="clear subtitle m-t-lg"> <label>来源：</label> 时讯网 <span class="pull-right"><label>发布时间：</label> 19小时前 </span> </small> 
            </div> </a> </td>
         </tr> 
        </tbody>
       </table> 
       <div style="margin-bottom: 30px;"> 
        <nav class="text-right"> 
         <ul class="pagination"> 
          <li class="active"><a htef="#">1</a></li>
          <li><a id="ajaxpage" href="javascript:getTabList(2,&quot;run&quot;,&quot;news&quot;)">2</a></li>
          <li><a id="ajaxpage" href="javascript:getTabList(3,&quot;run&quot;,&quot;news&quot;)">3</a></li>
          <li><a id="ajaxpage" href="javascript:getTabList(4,&quot;run&quot;,&quot;news&quot;)">4</a></li>
          <li><a id="ajaxpage" href="javascript:getTabList(5,&quot;run&quot;,&quot;news&quot;)">5</a></li>
          <li><a id="ajaxpage" href="javascript:getTabList(6,&quot;run&quot;,&quot;news&quot;)">6</a></li> 
          <li><a id="ajaxpage" href="javascript:getTabList(2,&quot;run&quot;,&quot;news&quot;)">&gt;</a></li> 
          <li><a id="ajaxpage" href="javascript:getTabList(500,&quot;run&quot;,&quot;news&quot;)"> ...500</a></li> 
         </ul> 
        </nav> 
       </div> 
       <script type="text/javascript">
        var optionArr = ['newstags','newsimpact'];
        var descArr = ['类别不限','情感不限'];
        var hiddenName = '';
        var hiddenValue = '';
        var hiddenDesc = '';
        for(var i=0;i<optionArr.length;i++){
            hiddenName = optionArr[i];
            hiddenValue = $("input[name=" + hiddenName + "]").val();
            hiddenDesc = $("input[name=" + hiddenName + "]").attr('data-desc');
            var text = '.' + hiddenName;
            if(hiddenValue != '' && hiddenValue != '0'){
                $(text).text(hiddenDesc);
            }else{
                $(text).text(descArr[i]);
            }
        }
        $(function () {
            $('#newslist .chooseRun').find('a').on('click',function(){
                var targetDiv = $(this).parent().parent().parent().parent();
                var target = targetDiv.attr('data-box');
                var optionArr = [];
                var hiddenName = '';
                var hiddenValue = '';
                var ajaxData = {};
                switch(target){
                    case 'news':
                        optionArr = ['newstags','newsimpact'];
                        ajaxData['box'] = 'news';
                        break;
                    default :
                        break;
                }
                var option = $(this).attr('data-option');
                option = target + option;
                var value = $(this).attr('data-value');
                var text = $(this).text();
                var textArr = text.split('(');
                $("input[name=" + option + "]").val(value);
                $("input[name=" + option + "]").attr('data-desc',textArr[0]);
                //取所有筛选条件的值
                for(var i=0;i<optionArr.length;i++){
                    hiddenName = optionArr[i];
                    hiddenValue = $("input[name=" + hiddenName + "]").val();
                    ajaxData[hiddenName] = hiddenValue;
                }
                //拼接其他参数
                ajaxData['unique'] = $("#unique").val();
                ajaxData['companyname'] = $("#companyname").val();
                ajaxData['tab'] = 'run';
                ajaxData['p'] = '1';
                getTabListNew(ajaxData);
            });
        });
    </script> 
      </section> 
      <section class="panel clear b-a" id="yblist"> 
       <div class="tcaption"> 
        <h3 class="title">公告研报</h3> 
        <span class="tbadge">17</span> 
        <div class="chooseRun" data-box="yb" style="float: right"> 
         <div class="tdrop"> 
          <span class="btn" data-toggle="dropdown"> <span class="ybtype">全部报告</span> <span class="caret m-l"></span> </span> 
          <ul class="dropdown-menu dropdown-menu-right"> 
           <li><a href="javascript:;" data-option="type" data-value="0">不限</a></li> 
           <li><a href="javascript:;" data-option="type" data-value="2">企业研报(1)</a></li> 
           <li><a href="javascript:;" data-option="type" data-value="3">相关公告(16)</a></li> 
          </ul> 
         </div> 
        </div> 
        <span class="watermark"></span> 
       </div> 
       <table class="ntable ntable-odd"> 
        <tbody> 
         <tr> 
          <th>序号</th> 
          <th>研报内容</th> 
          <th width="85">报告种类</th> 
          <th width="114">发布时间</th> 
         </tr> 
         <tr> 
          <td class="tx"> 1 </td> 
          <td> <a href="http://qccdata.qichacha.com/Disclosure/a52a8c36ba621f8ffbef0748f80d7a33.pdf" target="_blank" download="true"> 2018年年度审计报告 </a> </td> 
          <td class="text-center"> 相关公告 </td> 
          <td class="text-center"> 2019-04-25 </td> 
         </tr> 
         <tr> 
          <td class="tx"> 2 </td> 
          <td> <a href="http://qccdata.qichacha.com/Disclosure/5a37590a0f9f28996f5293008a227a94.pdf" target="_blank" download="true"> 2018年年度报告 </a> </td> 
          <td class="text-center"> 相关公告 </td> 
          <td class="text-center"> 2019-04-25 </td> 
         </tr> 
         <tr> 
          <td class="tx"> 3 </td> 
          <td> <a href="http://qccdata.qichacha.com/Disclosure/094c8672507ae31c1f8f3c670f0bea9b.pdf" target="_blank" download="true"> 2018年年度审计报告 </a> </td> 
          <td class="text-center"> 相关公告 </td> 
          <td class="text-center"> 2019-04-24 </td> 
         </tr> 
         <tr> 
          <td class="tx"> 4 </td> 
          <td> <a href="http://qccdata.qichacha.com/Disclosure/d2e3594c309bf4b9a84adfd89dc9e419.pdf" target="_blank" download="true"> 2018年年度报告 </a> </td> 
          <td class="text-center"> 相关公告 </td> 
          <td class="text-center"> 2019-04-24 </td> 
         </tr> 
         <tr> 
          <td class="tx"> 5 </td> 
          <td> <a href="http://qccdata.qichacha.com/Disclosure/122776d3acd6294d26a1fb9348bd008c.pdf" target="_blank" download="true"> [定期报告]壮元海:2018年年度报告 </a> </td> 
          <td class="text-center"> 相关公告 </td> 
          <td class="text-center"> 2019-04-23 </td> 
         </tr> 
         <tr> 
          <td class="tx"> 6 </td> 
          <td> <a href="http://qccdata.qichacha.com/Disclosure/481bdab824eb7c30de48db86ca9e2c63.pdf" target="_blank" download="true"> [定期报告]希源农业:2018年年度报告 </a> </td> 
          <td class="text-center"> 相关公告 </td> 
          <td class="text-center"> 2019-04-16 </td> 
         </tr> 
         <tr> 
          <td class="tx"> 7 </td> 
          <td> <a href="http://qccdata.qichacha.com/Disclosure/f4542b54cfe8bf0277f85d70a1716edc.pdf" target="_blank" download="true"> 2018年年度报告 </a> </td> 
          <td class="text-center"> 相关公告 </td> 
          <td class="text-center"> 2019-04-11 </td> 
         </tr> 
         <tr> 
          <td class="tx"> 8 </td> 
          <td> <a href="http://qccdata.qichacha.com/Disclosure/0e612dd1f02d97b04b47c2ed830baeaf.pdf" target="_blank" download="true"> [定期报告]东邦御厨:2018年年度报告 </a> </td> 
          <td class="text-center"> 相关公告 </td> 
          <td class="text-center"> 2019-04-02 </td> 
         </tr> 
         <tr> 
          <td class="tx"> 9 </td> 
          <td> <a href="http://qccdata.qichacha.com/Disclosure/fca994194f5b409b62a521eedd42844d.pdf" target="_blank" download="true"> [定期报告]猫诚股份:2018年年度报告 </a> </td> 
          <td class="text-center"> 相关公告 </td> 
          <td class="text-center"> 2019-03-20 </td> 
         </tr> 
         <tr> 
          <td class="tx"> 10 </td> 
          <td> <a href="http://qccdata.qichacha.com/Disclosure/eca5ffff6efe15e0f3a66889e536edc7.pdf" target="_blank" download="true"> 商贸零售行业2018年10月份第1期周报:节假日效应凸显‚消费增速或现企稳趋势 </a> </td> 
          <td class="text-center"> 企业研报 </td> 
          <td class="text-center"> 2018-10-08 </td> 
         </tr> 
        </tbody> 
       </table> 
       <div> 
        <nav class="text-right"> 
         <ul class="pagination"> 
          <li class="active"><a htef="#">1</a></li>
          <li><a id="ajaxpage" href="javascript:getTabList(2,&quot;run&quot;,&quot;yb&quot;)">2</a></li> 
          <li><a id="ajaxpage" href="javascript:getTabList(2,&quot;run&quot;,&quot;yb&quot;)">&gt;</a></li> 
         </ul> 
        </nav> 
       </div> 
       <script>
    $(function () {
        //设置选择状态
        var optionArr = ['ybtype'];
        var descArr = ['全部报告'];
        var hiddenName = '';
        var hiddenValue = '';
        var hiddenDesc = '';
        for(var i=0;i<optionArr.length;i++){
            hiddenName = optionArr[i];
            hiddenValue = $("input[name=" + hiddenName + "]").val();
            hiddenDesc = $("input[name=" + hiddenName + "]").attr('data-desc');
            var text = '.' + hiddenName;
            if(hiddenValue != '' && hiddenValue != '0'){
                $(text).text(hiddenDesc);
            }else{
                $(text).text(descArr[i]);
            }
        }
    });
</script> 
      </section> 
      <section class="panel clear  b-a" id="spotCheckList"> 
       <div class="tcaption"> 
        <h3 class="title"> 抽查检查</h3> 
        <span class="tbadge">2</span> 
        <span class="watermark"></span> 
       </div> 
       <table class="ntable ntable-odd"> 
        <tbody>
         <tr>
          <th class="tx">序号</th>
          <th>检查实施机关</th>
          <th>类型</th>
          <th>日期</th>
          <th>结果</th> 
         </tr> 
         <tr> 
         </tr>
         <tr>
          <td class="tx">1</td> 
          <td width="140">洋泾市场监管所</td> 
          <td width="90" class="text-center">抽查</td> 
          <td width="103">2018-10-30</td> 
          <td class="text-center">食品流通单位双随机检查：其他</td> 
         </tr> 
         <tr> 
         </tr>
         <tr>
          <td class="tx">2</td> 
          <td width="140">洋泾市场监管所</td> 
          <td width="90" class="text-center">抽查</td> 
          <td width="103">2018-10-30</td> 
          <td class="text-center">第三方交易平台经营者履行平台管理主体责任的检查：未发现问题；商品经营柜台出租者、商品展销会举办者、网络交易平台提供者、广播电视购物平台经营者，应当对申请进入其经营场所或者平台销售商品的经营者的主体资格履行审查登记义务的检查：未发现问题；销售者购进或销售商品的检查：未发现问题；进货检查验收制度执行情况的检查：未发现问题；服务业经营者违法行为的检查：未发现问题；不符合产品包装、标识要求的检查：未发现问题；自媒体广告内容的检查：未发现问题；销售失效、变质的产品的检查：未发现问题</td> 
         </tr> 
        </tbody>
       </table> 
      </section> 
      <section class="panel b-a" id="supplierlist"> 
       <div class="tcaption"> 
        <span class="title">供应商</span> 
        <span class="tbadge">1</span> 
        <div class="chooseRun" data-box="supplier" style="float: right"> 
         <div class="tdrop"> 
          <a class="btn m-l-xs supplieryear 2017 a" href="javascript:;" data-option="year" data-value="2017"> 2017年 </a> 
         </div> 
        </div> 
        <span class="watermark"></span> 
       </div> 
       <table class="ntable ntable-odd"> 
        <tbody> 
         <tr> 
          <th>序号</th> 
          <th>供应商</th> 
          <th>采购占比</th> 
          <th>采购金额(万元)</th> 
          <th>报告期</th> 
          <th>数据来源</th> 
          <th>关联关系</th> 
         </tr> 
         <tr> 
          <td class="tx"> 1 </td> 
          <td> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/857c5a5515307d8ed943a567367be308.jpg?x-oss-process=style/qcc_cmp" /> </span> 
           <div class="whead-text"> 
            <a href="/firm_857c5a5515307d8ed943a567367be308.html" target="_blank"><h3 class="seo font-14">上海猫诚电子商务股份有限公司</h3></a> 
           </div> </td> 
          <td width="86" class="text-center"> - </td> 
          <td width="120" class="text-center"> 302 </td> 
          <td width="102" class="text-center"> 2017 </td> 
          <td width="108" class="text-center"> 供应商公告 </td> 
          <td width="108" class="text-center"> 非关联方 </td> 
         </tr> 
        </tbody> 
       </table> 
       <div> 
       </div> 
       <script>
    $(function () {
        $('.supplieryear').removeClass('a');
        var hiddenValue = $("input[name=supplieryear]").val();
        if(hiddenValue){
            $('.supplieryear.'+hiddenValue).addClass('a');
        }else{
            $('.supplieryear').eq(0).addClass('a');
        }

        $('#supplierlist .chooseRun').find('a').on('click',function(){
            var targetDiv = $(this).parent().parent();
            var target = targetDiv.attr('data-box');
            var optionArr = ['supplieryear'];
            var hiddenName = '';
            var hiddenValue = '';
            var ajaxData = {};
            ajaxData['box'] = 'supplier';
            var option = $(this).attr('data-option');
            option = target + option;
            var value = $(this).attr('data-value');
            var text = $(this).text();
            var textArr = text.split('(');
            $("input[name=" + option + "]").val(value);
            $("input[name=" + option + "]").attr('data-desc',textArr[0]);
            //取所有筛选条件的值
            for(var i=0;i<optionArr.length;i++){
                hiddenName = optionArr[i];
                hiddenValue = $("input[name=" + hiddenName + "]").val();
                ajaxData[hiddenName] = hiddenValue;
            }
            //拼接其他参数
            ajaxData['unique'] = $("#unique").val();
            ajaxData['companyname'] = $("#companyname").val();
            ajaxData['tab'] = 'run';
            ajaxData['p'] = '1';
            getTabListNew(ajaxData);
        });
    });
</script> 
      </section> 
      <section class="panel b-a" id="customerlist"> 
       <div class="tcaption"> 
        <span class="title">客户</span> 
        <span class="tbadge">1</span> 
        <div class="chooseRun" data-box="customer" style="float: right"> 
         <div class="tdrop"> 
          <a class="btn m-l-xs customeryear 2017 a" href="javascript:;" data-option="year" data-value="2017"> 2017年 </a> 
         </div> 
        </div> 
        <span class="watermark"></span> 
       </div> 
       <table class="ntable ntable-odd"> 
        <tbody> 
         <tr> 
          <th>序号</th> 
          <th>客户</th> 
          <th>销售占比</th> 
          <th>销售金额(万元)</th> 
          <th>报告期</th> 
          <th>数据来源</th> 
          <th>关联关系</th> 
         </tr> 
         <tr> 
          <td class="tx"> 1 </td> 
          <td> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/5a76eea859c3915401de9c8833b8fc77.jpg?x-oss-process=style/qcc_cmp" /> </span> 
           <div class="whead-text"> 
            <a href="/firm_5a76eea859c3915401de9c8833b8fc77.html" target="_blank"><h3 class="seo font-14">上海名传信息技术股份有限公司</h3></a> 
           </div> </td> 
          <td width="86" class="text-center"> - </td> 
          <td width="120" class="text-center"> 0 </td> 
          <td width="102" class="text-center"> 2017 </td> 
          <td width="108" class="text-center"> 客户公告 </td> 
          <td width="108" class="text-center"> 非关联方 </td> 
         </tr> 
        </tbody> 
       </table> 
       <div> 
       </div> 
       <script>
    $(function () {
        $('.customeryear').removeClass('a');
        var hiddenValue = $("input[name=customeryear]").val();
        if(hiddenValue){
            $('.customeryear.'+hiddenValue).addClass('a');
        }else{
            $('.customeryear').eq(0).addClass('a');
        }

        $('#customerlist .chooseRun').find('a').on('click',function(){
            var targetDiv = $(this).parent().parent();
            var target = targetDiv.attr('data-box');
            var optionArr = ['customeryear'];
            var hiddenName = '';
            var hiddenValue = '';
            var ajaxData = {};
            ajaxData['box'] = 'customer';
            var option = $(this).attr('data-option');
            option = target + option;
            var value = $(this).attr('data-value');
            var text = $(this).text();
            var textArr = text.split('(');
            $("input[name=" + option + "]").val(value);
            $("input[name=" + option + "]").attr('data-desc',textArr[0]);
            //取所有筛选条件的值
            for(var i=0;i<optionArr.length;i++){
                hiddenName = optionArr[i];
                hiddenValue = $("input[name=" + hiddenName + "]").val();
                ajaxData[hiddenName] = hiddenValue;
            }
            //拼接其他参数
            ajaxData['unique'] = $("#unique").val();
            ajaxData['companyname'] = $("#companyname").val();
            ajaxData['tab'] = 'run';
            ajaxData['p'] = '1';
            getTabListNew(ajaxData);
        });
    });
</script> 
      </section> 
      <section class="panel b-a clear"> 
       <div class="m_ptsc" style="padding:20px 0;">
        数据来源：国家企业信用信息公示系统。
       </div> 
      </section> 
      <div class="modal fade" id="xkModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> 
       <div class="modal-dialog nmodal"> 
        <div class="modal-content"> 
         <div class="modal-header"> 
          <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> 
          <h4 class="modal-title" id="myModalLabel">行政许可详情</h4> 
         </div> 
         <div class="modal-body"> 
          <div class="xzxukeview"></div> 
          <div class="clearfix"></div> 
         </div> 
        </div> 
       </div> 
      </div> 
      <div class="modal fade" id="appDownloadModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> 
       <div class="modal-dialog nmodal"> 
        <div class="modal-content"> 
         <div class="modal-header"> 
          <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> 
          <h4 class="modal-title">下载APP</h4> 
         </div> 
         <div class="modal-body"> 
          <div class="qocdeBox"> 
           <img src="/material/theme/chacha/cms/app/images/download_qcode.png" /> 
          </div> 
         </div> 
         <div class="modal-footer">
           扫描下载企查查APP，查看招投标信息 
         </div> 
        </div> 
       </div> 
      </div> 
      <div class="modal fade" id="tenderModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> 
       <div class="modal-dialog nmodal"> 
        <div class="modal-content"> 
         <div class="modal-header"> 
          <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> 
          <h4 class="modal-title">招投标详情</h4> 
         </div> 
         <div class="modal-body reptile-view" style="max-height: calc(100vh - 125px);overflow-y: auto;"> 
         </div> 
        </div> 
       </div> 
      </div> 
      <div class="modal fade" id="jcModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> 
       <div class="modal-dialog nmodal"> 
        <div class="modal-content"> 
         <div class="modal-header"> 
          <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> 
          <h4 class="modal-title" id="myModalLabel">海关进出口信用信息详情</h4> 
         </div> 
         <div class="modal-body"> 
          <div class="jcxyview"></div> 
          <div class="clearfix"></div> 
         </div> 
        </div> 
       </div> 
      </div> 
      <div class="modal fade" id="landpubModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> 
       <div class="modal-dialog nmodal"> 
        <div class="modal-content"> 
         <div class="modal-header"> 
          <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> 
          <h4 class="modal-title" id="myModalLabel">地块公示详情</h4> 
         </div> 
         <div class="modal-body"> 
          <div id="landpubview"></div> 
         </div> 
        </div> 
       </div> 
      </div> 
      <div class="modal fade" id="landpurchaseModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> 
       <div class="modal-dialog nmodal"> 
        <div class="modal-content"> 
         <div class="modal-header"> 
          <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> 
          <h4 class="modal-title" id="myModalLabel">购地信息详情</h4> 
         </div> 
         <div class="modal-body"> 
          <div id="landpurchaseview"></div> 
         </div> 
        </div> 
       </div> 
      </div> 
      <div class="modal fade" id="landmarketModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> 
       <div class="modal-dialog nmodal"> 
        <div class="modal-content"> 
         <div class="modal-header"> 
          <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> 
          <h4 class="modal-title" id="myModalLabel">土地转让详情</h4> 
         </div> 
         <div class="modal-body"> 
          <div id="landmarketview"></div> 
         </div> 
        </div> 
       </div> 
      </div> 
      <div class="modal fade" id="telecomModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> 
       <div class="modal-dialog nmodal"> 
        <div class="modal-content"> 
         <div class="modal-header"> 
          <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> 
          <h4 class="modal-title" id="myModalLabel">电信许可详情</h4> 
         </div> 
         <div class="modal-body"> 
         </div> 
        </div> 
       </div> 
      </div> 
      <div class="modal fade" id="creditorModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> 
       <div class="modal-dialog"> 
        <div class="modal-content"> 
         <div class="modal-header"> 
          <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> 
          <h4 class="modal-title" id="myModalLabel">债券信息详情</h4> 
         </div> 
         <div class="modal-body"> 
          <div id="creditorview"></div> 
          <div class="clearfix"></div> 
          <div id="creditorannouncementlist"></div> 
          <div class="clearfix"></div> 
         </div> 
        </div> 
       </div> 
      </div> 
      <script type="text/javascript">
    setTimeout(function() {
        jobChart({"salgroup":[{"value":"2","count":1303,"desc":"5-10k"},{"value":"1","count":238,"desc":"0-5k"},{"value":"3","count":97,"desc":"10-15k"},{"value":"6","count":53,"desc":"25k\u4ee5\u4e0a"},{"value":"0","count":35,"desc":"\u9762\u8bae"},{"value":"4","count":26,"desc":"15-20k"},{"value":"5","count":24,"desc":"20-25k"}],"edugroup":[{"value":"5","count":690,"desc":"\u5927\u4e13"},{"value":"3","count":343,"desc":"\u9ad8\u4e2d"},{"value":"4","count":167,"desc":"\u4e2d\u4e13"},{"value":"6","count":142,"desc":"\u672c\u79d1"},{"value":"2","count":58,"desc":"\u521d\u4e2d"},{"value":"7","count":8,"desc":"\u7855\u58eb"}],"expgroup":[{"value":"2","count":588,"desc":"1-3\u5e74"},{"value":"3","count":541,"desc":"3-5\u5e74"},{"value":"4","count":96,"desc":"5-10\u5e74"},{"value":"5","count":8,"desc":"10\u5e74\u4ee5\u4e0a"},{"value":"1","count":7,"desc":"\u5e94\u5c4a\u6bd5\u4e1a\u751f"}],"avgsalary":[{"value":8092,"count":null,"desc":""}],"province":[{"value":"SH","count":1734,"desc":"\u4e0a\u6d77"},{"value":"","count":30,"desc":"\u5176\u4ed6"},{"value":"JS","count":7,"desc":"\u6c5f\u82cf"},{"value":"LN","count":5,"desc":"\u8fbd\u5b81"}],"areagroup":[{"value":"3100","count":1734,"desc":"\u4e0a\u6d77\u5e02"},{"value":"","count":37,"desc":"\u5176\u4ed6"},{"value":"2113","count":5,"desc":"\u671d\u9633\u5e02"}]});
    }, 500);
</script> 
      <script type="text/javascript">
    setTimeout(function() {
        newsChart('e45ee37279ffb3f2ce9bbbcfa39d8133');
    }, 500);
</script> 
      <script>
    $(function () {
        $('body').on('click','.chooseRun a',function(){
            var targetDiv = $(this).parent().parent().parent().parent();
            var target = targetDiv.attr('data-box');
            var optionArr = [];
            var hiddenName = '';
            var hiddenValue = '';
            var ajaxData = {};
            switch(target){
                case 'yb':
                    optionArr = ['ybtype'];
                    ajaxData['box'] = 'yb';
                    break;
                default :
                    break;
            }
            var option = $(this).attr('data-option');
            option = target + option;
            var value = $(this).attr('data-value');
            var text = $(this).text();
            var textArr = text.split('(');
            $("input[name=" + option + "]").val(value);
            $("input[name=" + option + "]").attr('data-desc',textArr[0]);
            //取所有筛选条件的值
            for(var i=0;i<optionArr.length;i++){
                hiddenName = optionArr[i];
                hiddenValue = $("input[name=" + hiddenName + "]").val();
                ajaxData[hiddenName] = hiddenValue;
            }
            //拼接其他参数
            ajaxData['unique'] = $("#unique").val();
            ajaxData['companyname'] = $("#companyname").val();
            ajaxData['tab'] = 'run';
            ajaxData['p'] = '1';
            getTabListNew(ajaxData);
        });
    });
</script> 
     </div> 
     <div class="data_div" id="fengxian_div" style="display: none;"> 
      <div class="fengxian_info"></div> 
      <section class="panel b-a clear m_dataTab"> 
       <div class="panel-body" style="padding-top: 5px"> 
        <a href="javascript:;" onclick="boxScrollNew('#Exceptions');zhugeTrack('企业主页-经营风险-经营异常',{'企业名称':'上海盒马网络科技有限公司'});" class="btn btn-sm btn-default  m-r-sm m-t-sm" style="white-space:nowrap;"> 经营异常&nbsp;1 </a> 
        <a href="javascript:;" class="btn btn-sm btn-default  m-r-sm m-t-sm c_disable" style="white-space:nowrap;cursor: default"> 严重违法&nbsp;0 </a> 
        <a href="javascript:;" onclick="boxScrollNew('#pledgelist');zhugeTrack('企业主页-经营风险-股权出质',{'企业名称':'上海盒马网络科技有限公司'});" class="btn btn-sm btn-default  m-r-sm m-t-sm" style="white-space:nowrap;"> 股权出质&nbsp;2 </a> 
        <a href="javascript:;" class="btn btn-sm btn-default  m-r-sm m-t-sm c_disable" style="white-space:nowrap;cursor: default"> 股权质押&nbsp;0 </a> 
        <a href="javascript:;" onclick="boxScrollNew('#penaltylist');zhugeTrack('企业主页-经营风险-行政处罚',{'企业名称':'上海盒马网络科技有限公司'});" class="btn btn-sm btn-default  m-r-sm m-t-sm" style="white-space:nowrap;"> 行政处罚&nbsp;3 </a> 
        <a href="javascript:;" class="btn btn-sm btn-default  m-r-sm m-t-sm c_disable" style="white-space:nowrap;cursor: default"> 税收违法&nbsp;0 </a> 
        <a href="javascript:;" class="btn btn-sm btn-default  m-r-sm m-t-sm c_disable" style="white-space:nowrap;cursor: default"> 动产抵押&nbsp;0 </a> 
        <a href="javascript:;" class="btn btn-sm btn-default  m-r-sm m-t-sm c_disable" style="white-space:nowrap;cursor: default"> 环保处罚&nbsp;0 </a> 
        <a href="javascript:;" class="btn btn-sm btn-default  m-r-sm m-t-sm c_disable" style="white-space:nowrap;cursor: default"> 清算信息&nbsp;0 </a> 
        <a href="javascript:;" class="btn btn-sm btn-default  m-r-sm m-t-sm c_disable" style="white-space:nowrap;cursor: default"> 司法拍卖&nbsp;0 </a> 
        <a href="javascript:;" class="btn btn-sm btn-default  m-r-sm m-t-sm c_disable" style="white-space:nowrap;cursor: default"> 土地抵押&nbsp;0 </a> 
        <a href="javascript:;" class="btn btn-sm btn-default  m-r-sm m-t-sm c_disable" style="white-space:nowrap;cursor: default"> 简易注销 </a> 
        <a href="javascript:;" class="btn btn-sm btn-default  m-r-sm m-t-sm c_disable" style="white-space:nowrap;cursor: default"> 公示催告&nbsp;0 </a> 
        <a href="javascript:;" class="btn btn-sm btn-default  m-r-sm m-t-sm c_disable" style="white-space:nowrap;cursor: default"> 欠税公告&nbsp;0 </a> 
       </div> 
      </section> 
      <section class="panel b-a clear" id="Exceptions"> 
       <div class="tcaption"> 
        <h3 class="title">经营异常</h3> 
        <span class="tbadger">1</span> 
       </div> 
       <div class="tcaption"> 
        <h3 class="subtitle">移出异常</h3> 
        <span class="watermark"></span> 
       </div> 
       <table class="ntable"> 
        <tbody>
         <tr>
          <th class="tx">序号</th>
          <th>列入日期</th>
          <th>列入经营异常名录原因</th>
          <th>作出决定机关</th>
          <th>移出日期</th>
          <th>移出经营异常名录原因</th> 
         </tr> 
         <tr> 
          <td class="tx">1</td> 
          <td width="103" class="text-center">2016-12-19</td> 
          <td width="220">通过登记的住所或者经营场所无法联系的</td> 
          <td>上海市浦东新区市场监督管理局</td> 
          <td width="103" class="text-center">2017-02-10</td> 
          <td width="220">列入经营异常名录3年内且依照《经营异常名录管理办法》第九条规定被列入经营异常名录的企业，提出通过登记的住所或者经营场所可以重新取得联系，申请移出</td> 
         </tr> 
        </tbody>
       </table> 
      </section> 
      <section class="panel clear  b-a" id="pledgelist"> 
       <div class="tcaption"> 
        <h3 class="title"> 股权出质</h3> 
        <span class="tbadger">2</span> 
        <span class="watermark"></span> 
       </div> 
       <table class="ntable ntable-odd"> 
        <tbody>
         <tr>
          <th class="tx">序号</th>
          <th>登记编号</th>
          <th width="140px;">出质人</th> 
          <th>质权人</th>
          <th>出质股权标的企业</th>
          <th>出质股权数额（万元）</th>
          <th>设立登记日期</th>
          <th class="ma_center">状态</th> 
         </tr> 
         <tr>
          <td class="tx">1</td> 
          <td width="170"><a data-toggle="modal" data-target="#pledgeModal" class="c_a" onclick="pledgeView({&quot;No&quot;:&quot;e805b9c86193ab342aaff662071d5707&quot;,&quot;RegistNo&quot;:&quot;0520180110          &quot;,&quot;RelatedCompanyInfo&quot;:{&quot;Org&quot;:0,&quot;KeyNo&quot;:&quot;f17cc592d93072e6971d1f62d084dc6e&quot;,&quot;Name&quot;:&quot;\u4e0a\u6d77\u8f69\u76d2\u7f51\u7edc\u6280\u672f\u670d\u52a1\u6709\u9650\u516c\u53f8&quot;},&quot;PledgorInfo&quot;:{&quot;Name&quot;:&quot;\u676d\u5dde\u5b9d\u8f69\u6295\u8d44\u7ba1\u7406\u6709\u9650\u516c\u53f8&quot;,&quot;KeyNo&quot;:&quot;1d0b3a6c59074b4976b1e2531810b28c&quot;,&quot;HasImage&quot;:false,&quot;CompanyCount&quot;:0,&quot;No&quot;:null},&quot;PledgeeInfo&quot;:{&quot;Name&quot;:&quot;\u4e0a\u6d77\u76d2\u9a6c\u7f51\u7edc\u79d1\u6280\u6709\u9650\u516c\u53f8&quot;,&quot;KeyNo&quot;:&quot;e45ee37279ffb3f2ce9bbbcfa39d8133&quot;,&quot;HasImage&quot;:false,&quot;CompanyCount&quot;:0,&quot;No&quot;:&quot;91310115342050446K       &quot;},&quot;PledgedAmount&quot;:&quot;1000&quot;,&quot;RegDate&quot;:1541750750,&quot;PublicDate&quot;:1541750750,&quot;Status&quot;:&quot;\u6709\u6548&quot;,&quot;Detail&quot;:{&quot;ChangeList&quot;:[],&quot;CancelDetail&quot;:{&quot;CancelDate&quot;:1541750750,&quot;CancelReason&quot;:&quot;&quot;}},&quot;Source&quot;:1})">0520180110 </a></td> 
          <td> <a href="/firm_1d0b3a6c59074b4976b1e2531810b28c.html" class="c_a" title="杭州宝轩投资管理有限公司"> 杭州宝轩投资管理有限公司 </a> </td> 
          <td><a class="c_a" href="/firm_e45ee37279ffb3f2ce9bbbcfa39d8133.html" target="_blank"> 上海盒马网络科技有限公司 </a> </td> 
          <td><a class="c_a" href="/firm_f17cc592d93072e6971d1f62d084dc6e.html" target="_blank"> 上海轩盒网络技术服务有限公司 </a> </td> 
          <td width="115" class="text-center">1000</td> 
          <td width="115" class="text-center">2018-11-09</td> 
          <td class="text-center" width="60">有效</td> 
         </tr> 
         <tr>
          <td class="tx">2</td> 
          <td width="170"><a data-toggle="modal" data-target="#pledgeModal" class="c_a" onclick="pledgeView({&quot;No&quot;:&quot;19da681d58c4e89ec300ed003f4c9f04&quot;,&quot;RegistNo&quot;:&quot;4120150150          &quot;,&quot;RelatedCompanyInfo&quot;:{&quot;Org&quot;:0,&quot;KeyNo&quot;:&quot;e45ee37279ffb3f2ce9bbbcfa39d8133&quot;,&quot;Name&quot;:&quot;\u4e0a\u6d77\u76d2\u9a6c\u7f51\u7edc\u79d1\u6280\u6709\u9650\u516c\u53f8&quot;},&quot;PledgorInfo&quot;:{&quot;Name&quot;:&quot;\u8c61\u7fcc\u5fae\u94fe\u79d1\u6280\u53d1\u5c55\u6709\u9650\u516c\u53f8&quot;,&quot;KeyNo&quot;:&quot;a8e7e2067e33b36274e99cf223943016&quot;,&quot;HasImage&quot;:false,&quot;CompanyCount&quot;:0,&quot;No&quot;:&quot;\u975e\u516c\u793a\u9879&quot;},&quot;PledgeeInfo&quot;:{&quot;Name&quot;:&quot;\u6d59\u6c5f\u5929\u732b\u6280\u672f\u6709\u9650\u516c\u53f8&quot;,&quot;KeyNo&quot;:&quot;561b327281de903b19bb458772446bfe&quot;,&quot;HasImage&quot;:false,&quot;CompanyCount&quot;:0,&quot;No&quot;:&quot;&quot;},&quot;PledgedAmount&quot;:&quot;1000&quot;,&quot;RegDate&quot;:1444894713,&quot;PublicDate&quot;:1444894713,&quot;Status&quot;:&quot;\u65e0\u6548&quot;,&quot;Detail&quot;:{&quot;ChangeList&quot;:[],&quot;CancelDetail&quot;:{&quot;CancelDate&quot;:1444894713,&quot;CancelReason&quot;:&quot;3&quot;}},&quot;Source&quot;:0})">4120150150 </a></td> 
          <td> <a href="/firm_a8e7e2067e33b36274e99cf223943016.html" class="c_a" title="象翌微链科技发展有限公司"> 象翌微链科技发展有限公司 </a> </td> 
          <td><a class="c_a" href="/firm_561b327281de903b19bb458772446bfe.html" target="_blank"> 浙江天猫技术有限公司 </a> </td> 
          <td><a class="c_a" href="/firm_e45ee37279ffb3f2ce9bbbcfa39d8133.html" target="_blank"> 上海盒马网络科技有限公司 </a> </td> 
          <td width="115" class="text-center">1000</td> 
          <td width="115" class="text-center">2015-10-15</td> 
          <td class="text-center" width="60">无效</td> 
         </tr> 
        </tbody>
       </table> 
       <div> 
       </div> 
      </section> 
      <section class="panel clear  b-a" id="penaltylist"> 
       <div class="tcaption"> 
        <h3 class="title"> 行政处罚 [工商局]</h3> 
        <span class="tbadger">3</span> 
        <span class="thist">（查看更多1条 <a onclick="jumpHistory('hisxzcf')">历史行政处罚</a>）</span> 
        <span class="watermark"></span> 
       </div> 
       <table class="ntable ntable-odd"> 
        <tbody>
         <tr>
          <th class="tx">序号</th>
          <th>决定文书号</th>
          <th>违法行为类型</th>
          <th>行政处罚内容</th> 
          <th>公示日期</th> 
          <th>决定机关</th>
          <th class="text-center">决定日期</th> 
         </tr> 
         <tr>
          <td class="tx">1</td> 
          <td width="180"> 13101152017000034642 </td> 
          <td class="text-center">发票违法</td> 
          <td width="180" data-detail="罚款500元">罚款500元</td> 
          <td width="103">2017-10-16</td> 
          <td width="120"> 上海市浦东新区税务局第二十一税务所 </td> 
          <td width="103"> 2017-10-16 </td> 
         </tr> 
         <tr>
          <td class="tx">2</td> 
          <td width="180"> 13101152017000027656 </td> 
          <td class="text-center">其他违法</td> 
          <td width="180" data-detail="罚款500元">罚款500元</td> 
          <td width="103">2017-08-15</td> 
          <td width="120"> 上海市浦东新区税务局第二十一税务所 </td> 
          <td width="103"> 2017-08-15 </td> 
         </tr> 
         <tr>
          <td class="tx">3</td> 
          <td width="180"> <a href="https://img.qichacha.com/PenaltyDoc/b56b6bad60e89d22a20dbd147d9cf19d.pdf" target="_blank"> 浦市监案处字〔2017〕第150201714216号 </a> </td> 
          <td class="text-center">违反本法第十七条规定,在广告中涉及疾病治疗功能,以及使用医疗用语或者易使推销的商品与药品、医疗器械相混淆的用语的</td> 
          <td width="180" data-detail="罚款 1500.0 元;责令停止发布">罚款 1500.0 元;责令停止发布</td> 
          <td width="103">2017-05-08</td> 
          <td width="120"> 上海市浦东新区市场监督管理局 </td> 
          <td width="103"> 2017-04-20 </td> 
         </tr> 
        </tbody>
       </table> 
       <div> 
       </div> 
      </section> 
      <section class="panel b-a clear"> 
       <div class="m_ptsc" style="padding:20px 0;">
        数据来源：国家企业信用信息公示系统。
       </div> 
      </section> 
      <div class="modal fade" id="sfpmModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> 
       <div class="modal-dialog nmodal"> 
        <div class="modal-content"> 
         <div class="modal-header"> 
          <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> 
          <h4 class="modal-title" id="myModalLabel">司法拍卖详情</h4> 
         </div> 
         <div class="modal-body" style="max-height: calc(100vh - 125px);overflow-y: auto;"> 
          <div class="sfpmview"></div> 
          <div class="clearfix"></div> 
         </div> 
        </div> 
       </div> 
      </div> 
      <div class="modal fade" id="pnModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> 
       <div class="modal-dialog nmodal"> 
        <div class="modal-content"> 
         <div class="modal-header"> 
          <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> 
          <h4 class="modal-title">公示催告详情</h4> 
         </div> 
         <div class="modal-body"></div> 
        </div> 
       </div> 
      </div> 
      <div class="modal fade" id="oweNoticeModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> 
       <div class="modal-dialog nmodal"> 
        <div class="modal-content"> 
         <div class="modal-header"> 
          <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> 
          <h4 class="modal-title">欠税公告详情</h4> 
         </div> 
         <div class="modal-body"></div> 
        </div> 
       </div> 
      </div> 
      <div class="modal fade" id="taxPunishModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> 
       <div class="modal-dialog nmodal"> 
        <div class="modal-content"> 
         <div class="modal-header"> 
          <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> 
          <h4 class="modal-title">行政处罚详情[税务局]</h4> 
         </div> 
         <div class="modal-body"></div> 
        </div> 
       </div> 
      </div> 
      <div class="modal fade" id="otherPunishModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> 
       <div class="modal-dialog nmodal"> 
        <div class="modal-content"> 
         <div class="modal-header"> 
          <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> 
          <h4 class="modal-title">行政处罚详情[其他]</h4> 
         </div> 
         <div class="modal-body"></div> 
        </div> 
       </div> 
      </div> 
      <div class="modal fade" id="pledgeModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> 
       <div class="modal-dialog nmodal"> 
        <div class="modal-content"> 
         <div class="modal-header"> 
          <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> 
          <h4 class="modal-title">股权出质详情</h4> 
         </div> 
         <div class="modal-body"> 
          <div id="pledgeview"></div> 
         </div> 
        </div> 
       </div> 
      </div> 
      <div class="modal fade" id="spledgeModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> 
       <div class="modal-dialog nmodal"> 
        <div class="modal-content"> 
         <div class="modal-header"> 
          <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> 
          <h4 class="modal-title">质押明细</h4> 
         </div> 
         <div class="modal-body"> 
         </div> 
        </div> 
       </div> 
      </div> 
      <div class="modal fade" id="spledgeHoldModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> 
       <div class="modal-dialog nmodal"> 
        <div class="modal-content"> 
         <div class="modal-header"> 
          <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> 
          <h4 class="modal-title">重要股东质押详情</h4> 
         </div> 
         <div class="modal-body"> 
         </div> 
        </div> 
       </div> 
      </div> 
      <div class="modal fade" id="taxIllegalModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> 
       <div class="modal-dialog nmodal"> 
        <div class="modal-content"> 
         <div class="modal-header"> 
          <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> 
          <h4 class="modal-title">税收违法详情</h4> 
         </div> 
         <div class="modal-body"> 
          <div id="taxIllegalview"></div> 
         </div> 
        </div> 
       </div> 
      </div> 
      <div class="modal fade" id="landmortgageModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> 
       <div class="modal-dialog nmodal"> 
        <div class="modal-content"> 
         <div class="modal-header"> 
          <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> 
          <h4 class="modal-title">土地抵押详情</h4> 
         </div> 
         <div class="modal-body"> 
          <div id="landmortgageview"></div> 
         </div> 
        </div> 
       </div> 
      </div> 
      <div class="modal fade" id="envModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> 
       <div class="modal-dialog nmodal"> 
        <div class="modal-content"> 
         <div class="modal-header"> 
          <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> 
          <h4 class="modal-title">环保处罚详情</h4> 
         </div> 
         <div class="modal-body"> 
          <div id="envview"></div> 
         </div> 
        </div> 
       </div> 
      </div> 
      <div class="modal fade" id="cfModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> 
       <div class="modal-dialog"> 
        <div class="modal-content"> 
         <div class="modal-header"> 
          <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">x</span></button> 
          <h4 class="modal-title" id="myModalLabel">行政处罚详情</h4> 
         </div> 
         <div class="modal-body"> 
          <div class="xzcfview"></div> 
          <div class="clearfix"></div> 
         </div> 
        </div> 
       </div> 
      </div>
     </div> 
     <div class="data_div" id="feeds_div" style="display: none;"></div> 
     <div class="data_div" id="muhou_div" style="display: none;"></div> 
     <div class="data_div" id="finance_div" style="display: none;"></div> 
     <div class="data_div" id="pay_div" style="display: none;"></div> 
     <div class="data_div" id="buy_div" style="display: none;"></div> 
     <div class="data_div" id="history_div" style="display: none;"> 
      <div class="history_info"></div> 
      <section class="panel b-a clear m_dataTab"> 
       <div class="panel-body" style="padding-top: 5px"> 
        <a href="javascript:;" onclick="boxScrollNew('#hiscominfo');zhugeTrack('企业主页-历史信息-历史工商信息',{'企业名称':'上海盒马网络科技有限公司'});" class="btn btn-sm btn-default  m-r-sm  m-t-sm" style="white-space:nowrap;"> 历史工商信息&nbsp; </a> 
        <a href="javascript:;" class="btn btn-sm btn-default  m-r-sm m-t-sm c_disable" style="white-space:nowrap;cursor: pointer"> 历史对外投资&nbsp;0 </a> 
        <a href="javascript:;" onclick="boxScrollNew('#hispartnerlist');zhugeTrack('企业主页-历史信息-历史股东',{'企业名称':'上海盒马网络科技有限公司'});" class="btn btn-sm btn-default  m-r-sm  m-t-sm" style="white-space:nowrap;"> 历史股东&nbsp;1 </a> 
        <a href="javascript:;" class="btn btn-sm btn-default  m-r-sm m-t-sm c_disable" style="white-space:nowrap;cursor: default"> 历史失信被执行人&nbsp;0 </a> 
        <a href="javascript:;" onclick="boxScrollNew('#hiszhixinglist');zhugeTrack('企业主页-历史信息-历史被执行人',{'企业名称':'上海盒马网络科技有限公司'});" class="btn btn-sm btn-default  m-r-sm m-t-sm" style="white-space:nowrap;"> 历史被执行人&nbsp;3 </a> 
        <a href="javascript:;" class="btn btn-sm btn-default  m-r-sm m-t-sm c_disable" style="white-space:nowrap;cursor: default"> 历史法院公告&nbsp;0 </a> 
        <a href="javascript:;" class="btn btn-sm btn-default  m-r-sm m-t-sm c_disable" style="white-space:nowrap;cursor: default"> 历史裁判文书&nbsp;0 </a> 
        <a href="javascript:;" onclick="boxScrollNew('#hisxzcf');zhugeTrack('企业主页-历史信息-历史行政处罚',{'企业名称':'上海盒马网络科技有限公司'});" class="btn btn-sm btn-default  m-r-sm m-t-sm" style="white-space:nowrap;"> 历史行政处罚&nbsp;1 </a> 
        <a href="javascript:;" class="btn btn-sm btn-default  m-r-sm m-t-sm c_disable" style="white-space:nowrap;cursor: default"> 历史动产抵押&nbsp;0 </a> 
        <a href="javascript:;" class="btn btn-sm btn-default  m-r-sm m-t-sm c_disable" style="white-space:nowrap;cursor: default"> 历史开庭公告&nbsp;0 </a> 
        <a href="javascript:;" class="btn btn-sm btn-default  m-r-sm m-t-sm c_disable" style="white-space:nowrap;cursor: default"> 历史股权出质&nbsp;0 </a> 
        <a href="javascript:;" onclick="boxScrollNew('#hisxzxk');zhugeTrack('企业主页-历史信息-历史行政许可',{'企业名称':'上海盒马网络科技有限公司'});" class="btn btn-sm btn-default  m-r-sm m-t-sm" style="white-space:nowrap;"> 历史行政许可&nbsp;10 </a> 
       </div> 
      </section> 
      <section class="panel b-a" id="hiscominfo"> 
       <div class="tcaption"> 
        <h3 class="title">历史工商信息</h3> 
        <span class="watermark"></span> 
       </div> 
       <table class="ntable"> 
        <tbody>
         <tr> 
          <td class="tb" width="18%" rowspan="1">历史名称：</td> 
          <td width="103"> 2017-03-03 </td> 
          <td class=""> 上海翌恒网络科技有限公司 </td> 
         </tr> 
         <tr> 
          <td class="tb" width="18%" rowspan="2">历史法定代表人：</td> 
          <td width="103"> 2017-05-11 </td> 
          <td class=""> <a href="/pl_p2c4af03fd352ef1ffb597fa6331f71c.html" class="c_a">郑俊芳</a> </td> 
         </tr> 
         <tr> 
          <td width="103"> 2016-09-19 </td> 
          <td class=""> <a href="/pl_p46782e8db0409a515876b2361290b37.html" class="c_a">陶国谦</a> </td> 
         </tr> 
         <tr> 
          <td class="tb" width="18%" rowspan="1">历史注册资本：</td> 
          <td width="103"> 2016-09-19 </td> 
          <td class=""> 1000万人民币元 </td> 
         </tr> 
         <tr> 
          <td class="tb" width="18%" rowspan="10">历史经营范围：</td> 
          <td width="103"> 2018-09-08 </td> 
          <td class=""> 计算机网络专业领域内的技术开发并提供相关技术咨询及技术服务,计算机系统集成的设计、安装、调试、维护,通信设备维修,食品、宠物用品、服装、成人保健用品、日用百货、家用电器、食用农产品、粮食(中央储备粮食除外)、家居用品、电子产品及配件、甘油、香料香精(除危险化学品、监控化学品、民用爆炸物品)、数码产品及配件、照相器材、针纺织品、化妆品、办公用品、体育用品及器材、玩具、汽车用品、汽摩配件、珠宝首饰(毛钻、裸钻除外)、工艺品(文物、象牙及其制品除外)、五金交电、计算机软硬件及配件(音像制品除外)、机械设备、化工产品(危险化学品除外)、消防器材、建筑装饰材料(钢材、水泥除外)、一类医疗器械、二类医疗器械、母婴用品、乳制品(含婴幼儿配方乳粉)、花卉、酒类的批发、零售(店铺零售限分支机构)、网上零售、进出口、佣金代理(拍卖除外),票务代理(航空票务代理除外),餐饮管理。餐饮服务、洗衣服务、净水器清洗服务、美容、美发、美甲、健身服务、犬只美容、寄养、销售、儿童游乐设施经营(游艺机、危险项目除外)(以上项目均限分支机构经营)。【依法须经批准的项目,经相关部门批准后方可开展经营活动】 </td> 
         </tr> 
         <tr> 
          <td width="103"> 2018-09-07 </td> 
          <td class=""> 计算机网络专业领域内的技术开发并提供相关技术咨询及技术服务，计算机系统集成的设计、安装、调试、维护，通信设备维修，食品、宠物用品、服装、成人保健用品、日用百货、家用电器、食用农产品、粮食（中央储备粮食除外）、家居用品、电子产品及配件、甘油、香料香精（除危险化学品、监控化学品、民用爆炸物品）、数码产品及配件、照相器材、针纺织品、化妆品、办公用品、体育用品及器材、玩具、汽车用品、汽摩配件、珠宝首饰（毛钻、裸钻除外）、工艺品（文物、象牙及其制品除外）、五金交电、计算机软硬件及配件（音像制品除外）、机械设备、化工产品（危险化学品除外）、消防器材、建筑装饰材料（钢材、水泥除外）、一类医疗器械、二类医疗器械、母婴用品、乳制品（含婴幼儿配方乳粉）、花卉、酒类的批发、零售（店铺零售限分支机构）、网上零售、进出口、佣金代理（拍卖除外），票务代理（航空票务代理除外），餐饮管理。餐饮服务、洗衣服务、净水器清洗服务、美容、美发、美甲、健身服务、犬只美容、寄养、销售、儿童游乐设施经营（游艺机、危险项目除外）（以上项目均限分支机构经营）。【依法须经批准的项目，经相关部门批准后方可开展经营活动】 </td> 
         </tr> 
         <tr> 
          <td width="103"> 2018-05-30 </td> 
          <td class=""> 计算机网络专业领域内的技术开发并提供相关技术咨询及技术服务,计算机系统集成的设计、安装、调试、维护,通信设备维修,食品、宠物用品、服装、成人保健用品、日用百货、家用电器、食用农产品、粮食(中央储备粮食除外)、家居用品、数码产品及配件、照相器材、针纺织品、化妆品、办公用品、体育用品及器材、玩具、汽车用品、汽摩配件、珠宝首饰(毛钻、裸钻除外)、工艺品(文物、象牙及其制品除外)、五金交电、计算机软硬件及配件(音像制品除外)、机械设备、化工产品(危险化学品除外)、消防器材、建筑装饰材料(钢材、水泥除外)、一类医疗器械、二类医疗器械、母婴用品、乳制品(含婴幼儿配方乳粉)、花卉、酒类的批发、零售(店铺零售限分支机构)、网上零售、进出口、佣金代理(拍卖除外),票务代理(航空票务代理除外),餐饮管理。餐饮服务、洗衣服务、净水器清洗服务、美容、美发、美甲、健身服务、犬只美容、寄养、销售、儿童游乐设施经营(游艺机、危险项目除外)(以上项目均限分支机构经营)。【依法须经批准的项目,经相关部门批准后方可开展经营活动】。 </td> 
         </tr> 
         <tr> 
          <td width="103"> 2018-04-19 </td> 
          <td class=""> 计算机网络专业领域内的技术开发并提供相关技术咨询及技术服务,计算机系统集成的设计、安装、调试、维护,通信设备维修,食品、宠物用品、服装、成人保健用品、日用百货、家用电器、食用农产品、粮食(中央储备粮食除外)、家居用品、数码产品及配件、照相器材、针纺织品、化妆品、办公用品、体育用品及器材、玩具、汽车用品、汽摩配件、珠宝首饰(毛钻、裸钻除外)、工艺品(文物、象牙及其制品除外)、五金交电、计算机软硬件及配件(音像制品除外)、机械设备、化工产品(危险化学品除外)、消防器材、建筑装饰材料(钢材、水泥除外)、一类医疗器械、二类医疗器械、母婴用品、乳制品(含婴幼儿配方乳粉)、花卉、酒类的批发、零售(店铺零售限分支机构)、网上零售、进出口、佣金代理(拍卖除外),票务代理(航空票务代理除外),餐饮管理餐饮服务、洗衣服务、净水器清洗服务、美容、美发、美甲、健身服务、犬只美容、寄养、销售、儿童游乐设施经营(游艺机、危险项目除外)(以上项目均限分支机构经营)【依法须经批准的项目,经相关部门批准后方可开展经营活动】 </td> 
         </tr> 
         <tr> 
          <td width="103"> 2017-10-19 </td> 
          <td class=""> 计算机网络专业领域内的技术开发并提供相关技术咨询及技术服务，计算机系统集成的设计、安装、调试、维护，食品、服装、日用百货、家用电器、食用农产品、粮食（中央储备粮食除外）、家居用品、数码产品及配件、照相器材、针纺织品、化妆品、办公用品、体育用品及器材、玩具、汽车用品、汽摩配件、珠宝首饰（毛钻、裸钻除外）、工艺品（文物除外）、五金交电、计算机软硬件及配件（音像制品除外）、机械设备、化工产品（危险化学品除外）、消防器材、建筑装饰材料（钢材、水泥除外）、一类医疗器械、二类医疗器械、母婴用品、乳制品（含婴幼儿配方乳粉）、花卉、酒类的批发、零售（店铺零售限分支机构）、网上零售，票务代理（航空票务代理除外），餐饮管理，餐饮服务（限分支机构经营）。【依法须经批准的项目，经相关部门批准后方可开展经营活动】 </td> 
         </tr> 
         <tr> 
          <td width="103"> 2017-08-17 </td> 
          <td class=""> 计算机网络专业领域内的技术开发并提供相关技术咨询及技术服务，计算机系统集成的设计、安装、调试、维护，食品、服装、日用百货、家用电器、食用农产品、粮食（中央储备粮食除外）、家居用品、数码产品及配件、照相器材、针纺织品、化妆品、办公用品、体育用品及器材、玩具、汽车用品、汽摩配件、珠宝首饰（毛钻、裸钻除外）、工艺品（文物除外）、五金交电、计算机软硬件及配件（音像制品除外）、机械设备、化工产品（危险化学品除外）、消防器材、建筑装饰材料（钢材、水泥除外）、一类医疗器械、二类医疗器械、母婴用品、乳制品（含婴幼儿配方乳粉）、花卉、酒类的批发、零售（店铺零售限分支机构），票务代理（航空票务代理除外），餐饮管理，餐饮服务（限分支机构经营）。 【依法须经批准的项目，经相关部门批准后方可开展经营活动】 </td> 
         </tr> 
         <tr> 
          <td width="103"> 2017-03-07 </td> 
          <td class=""> 计算机网络专业领域内的技术开发并提供相关技术咨询及技术服务，计算机系统集成的设计、安装、调试、维护，食品流通、服装、日用百货、家用电器、食用农产品、粮食、家居用品、数码产品及配件、照相器材、针纺织品、化妆品、办公用品、体育用品及器材、玩具、汽车用品、汽摩配件、珠宝首饰（毛钻、裸钻除外）、工艺品（文物除外）、五金交电、计算机软硬件及配件（音像制品除外）、机械设备、化工产品（危险化学品除外）、消防器材、建筑装饰材料（钢材、水泥除外）、一类医疗器械、花卉的批发、零售（店铺零售限分支机构），票务代理（航空票务代理除外），餐饮管理，餐饮服务（限分支机构经营）。【依法须经批准的项目，经相关部门批准后方可开展经营活动】 </td> 
         </tr> 
         <tr> 
          <td width="103"> 2016-09-19 </td> 
          <td class=""> 计算机网络专业领域内的技术开发、技术咨询、技术转让、技术服务，计算机系统集成，服装、日用百货、家用电器、食用农产品、家居用品、数码产品及配件、照相器材、针纺织品、化妆品、办公用品、体育用品及器材、玩具、汽车用品、汽摩配件、珠宝首饰、工艺品、五金交电、计算机软硬件及配件、机械设备、化工产品（除危险化学品、监控化学品、民用爆炸物品、易制毒化学品）、消防器材、建筑装饰材料、医疗器械、花卉的销售，票务代理，餐饮企业管理，餐饮服务（限分支机构经营），食品流通，烟草专卖零售（取得许可证件后方可从事是经营活动）。【依法须经批准的项目，经相关部门批准后方可开展经营活动】 </td> 
         </tr> 
         <tr> 
          <td width="103"> 2016-03-03 </td> 
          <td class=""> 计算机网络专业领域内的技术开发、技术咨询、技术转让、技术服务，计算机系统集成，服装、日用百货、家用电器、食用农产品、家居用品、数码产品及配件、照相器材、针纺织品、化妆品、办公用品、体育用品及器材、玩具、汽车用品、汽摩配件、珠宝首饰、工艺品、五金交电、计算机软硬件及配件、机械设备、化工产品（除危险化学品、监控化学品、烟花爆竹、民用爆炸物品、易制毒化学品）、消防器材、建筑装饰材料、医疗器械的销售，票务代理，餐饮企业管理，餐饮服务（限分支机构经营）。【依法须经批准的项目，经相关部门批准后方可开展经营活动】 </td> 
         </tr> 
         <tr> 
          <td width="103"> 2015-07-02 </td> 
          <td class=""> 计算机网络专业领域内的技术咨询、技术服务、技术转让、技术服务，计算机系统集成，服装、日用百货、家用电器、食用农产品、家居用品、数码产品及配件、照相器材、针纺织品、化妆品、办公用品、体育用品及器材、玩具、汽车用品、汽摩配件、珠宝首饰、工艺品、五金交电、计算机软硬件及配件、机械设备、化工产品（除危险化学品、监控化学品、烟花爆竹、民用爆炸物品、易制毒化学品）、消防器材、建筑装饰材料、医疗器械的销售，票务代理，餐饮企业管理。【依法须经批准的项目，经相关部门批准后方可开展经营活动】 </td> 
         </tr> 
         <tr> 
          <td class="tb" width="18%" rowspan="2">历史主要人员：</td> 
          <td width="103"> 2017-05-11 </td> 
          <td class=""> <a href="/pl_pa14da0de0e32e960da96e985c4f5e5e.html" class="text-primary">徐殿勇</a>, <a href="/pl_p580cd17d9f541702a808e95feee7bc6.html" class="text-primary">俞思瑛</a> </td> 
         </tr> 
         <tr> 
          <td width="103"> 2017-02-18 </td> 
          <td class=""> <a href="/pl_pa14da0de0e32e960da96e985c4f5e5e.html" class="text-primary">徐殿勇</a>(董事), <a href="/pl_pd569a04b441a1ad875c43e236d98a8a.html" class="text-primary">冯云乐</a>(监事), <a href="/pl_p580cd17d9f541702a808e95feee7bc6.html" class="text-primary">俞思瑛</a>(董事), <a href="/pl_p2c4af03fd352ef1ffb597fa6331f71c.html" class="text-primary">郑俊芳</a>(董事长兼总经理) </td> 
         </tr> 
        </tbody>
       </table> 
      </section> 
      <section class="panel b-a" id="hispartnerlist"> 
       <div class="tcaption"> 
        <h3 class="title">历史股东</h3> 
        <span class="tbadge"> 1 </span> 
        <span class="watermark"></span> 
       </div> 
       <table class="ntable ntable-odd"> 
        <tbody>
         <tr>
          <th class="tx">序号</th>
          <th>股东</th>
          <th>持股比例</th>
          <th>股东类型</th>
          <th>认缴出资额</th>
          <th>认缴出资日期</th>
          <th>参股日期</th>
          <th>退出日期</th>
         </tr> 
         <tr> 
          <td class="tx">1</td> 
          <td> <span class="headimg"> <img src="https://co-image.qichacha.com/CompanyImage/a8e7e2067e33b36274e99cf223943016.jpg?x-oss-process=image/resize,w_160" /> </span> 
           <div class="whead-text"> 
            <a href="/firm_a8e7e2067e33b36274e99cf223943016.html">象翌微链科技发展有限公司</a> 
           </div> </td> 
          <td width="93" class="text-center">-</td> 
          <td width="93" class="text-center">-</td> 
          <td width="118" class="text-center">-</td> 
          <td width="118" class="text-center"> - </td> 
          <td width="103" class="text-center">-</td> 
          <td width="103" class="text-center">2016-09-19</td> 
         </tr> 
        </tbody>
       </table> 
       <div class=""> 
       </div> 
      </section> 
      <section class="panel b-a clear" id="hiszhixinglist"> 
       <div class="tcaption"> 
        <h3 class="title">历史被执行人</h3> 
        <span class="tbadge"> 3 </span> 
        <span class="watermark"></span> 
       </div> 
       <table class="ntable ntable-odd"> 
        <tbody>
         <tr>
          <th class="tx">序号</th>
          <th>案号</th>
          <th>立案时间</th>
          <th>执行法院</th>
          <th>执行标的</th>
         </tr> 
         <tr> 
          <td class="tx">1</td> 
          <td>（2018）沪0110执1675号</td> 
          <td width="103" class="text-center">2018-04-20</td> 
          <td>上海市杨浦区人民法院</td> 
          <td class="text-center">70265</td> 
         </tr> 
         <tr> 
          <td class="tx">2</td> 
          <td>（2018）沪0115执5736号</td> 
          <td width="103" class="text-center">2018-03-22</td> 
          <td>上海市浦东新区人民法院</td> 
          <td class="text-center">13394</td> 
         </tr> 
         <tr> 
          <td class="tx">3</td> 
          <td>（2018）沪0115执13176号</td> 
          <td width="103" class="text-center">2018-07-04</td> 
          <td>上海市浦东新区人民法院</td> 
          <td class="text-center">13461</td> 
         </tr> 
        </tbody>
       </table> 
       <div class=""> 
       </div> 
      </section> 
      <div id="hisxzcf"></div> 
      <section class="panel b-a clear" id="hisaplist"> 
       <div class="tcaption"> 
        <h3 class="title">历史行政处罚【工商局】</h3> 
        <span class="tbadge"> 1 </span> 
        <span class="watermark"></span> 
       </div> 
       <table class="ntable ntable-odd"> 
        <tbody>
         <tr>
          <th class="tx">序号</th>
          <th>文号</th>
          <th>类型</th>
          <th>处罚内容</th>
          <th>决定机关</th>
          <th>决定日期</th>
         </tr> 
         <tr> 
          <td class="tx">1</td> 
          <td width="160">浦市监案处字2017第150201714216号</td> 
          <td>违反本法第十七条规定，在广告中涉及疾病治疗功能，以及使用医疗用语或者易使推销的商品与药品、医疗器械相混淆的用语的</td> 
          <td width="140">罚款 1500.0 元;责令停止发布</td> 
          <td width="100">上海市浦东新区市场监督管理局</td> 
          <td width="103">2017-04-20</td> 
         </tr> 
        </tbody>
       </table> 
       <div class=""> 
       </div> 
      </section> 
      <div id="hisxzxk"></div> 
      <section class="panel b-a clear" id="hisal2list"> 
       <div class="tcaption"> 
        <h3 class="title">历史行政许可【信用中国】</h3> 
        <span class="tbadge"> 10 </span> 
        <span class="watermark"></span> 
       </div> 
       <table class="ntable ntable-odd"> 
        <tbody>
         <tr>
          <th width="20%">编号</th>
          <th>项目名称</th>
          <th width="7%">地域</th>
          <th width="12%">决定日期</th>
          <th width="25%">公司</th>
         </tr> 
         <tr>
          <td class="text-center">沪114环保许管[2018]55号</td> 
          <td>上海盒马网络科技有限公司嘉定第一分公司项目</td> 
          <td>总局</td> 
          <td>2018-03-02</td> 
          <td>上海盒马网络科技有限公司</td> 
         </tr> 
         <tr>
          <td class="text-center">沪国税浦许准字〔2018〕第1907号</td> 
          <td>增值税专用发票（增值税税控系统）最高开票限额审批</td> 
          <td>总局</td> 
          <td>2018-02-09</td> 
          <td>上海盒马网络科技有限公司</td> 
         </tr> 
         <tr>
          <td class="text-center">-</td> 
          <td>对增值税防伪税控系统最高开票限额的审批</td> 
          <td>总局</td> 
          <td>2018-02-08</td> 
          <td>上海盒马网络科技有限公司</td> 
         </tr> 
         <tr>
          <td class="text-center">ljz201701619</td> 
          <td>外商投资企业变更备案回执</td> 
          <td>总局</td> 
          <td>2017-10-17</td> 
          <td>上海盒马网络科技有限公司</td> 
         </tr> 
         <tr>
          <td class="text-center">松环保许管[2017]1857号</td> 
          <td>上海盒马网络科技有限公司松江第一分公司项目</td> 
          <td>总局</td> 
          <td>2017-09-12</td> 
          <td>上海盒马网络科技有限公司</td> 
         </tr> 
         <tr>
          <td class="text-center">松环保许管[2017]1476号</td> 
          <td>上海盒马网络科技有限公司松江第一分公司项目</td> 
          <td>总局</td> 
          <td>2017-07-24</td> 
          <td>上海盒马网络科技有限公司</td> 
         </tr> 
         <tr>
          <td class="text-center">普环保验[2017]85号</td> 
          <td>建设项目环保竣工验收的审批</td> 
          <td>总局</td> 
          <td>2017-07-04</td> 
          <td>上海盒马网络科技有限公司</td> 
         </tr> 
         <tr>
          <td class="text-center">jy13101150257400</td> 
          <td>食品经营许可</td> 
          <td>总局</td> 
          <td>2017-06-09</td> 
          <td>上海盒马网络科技有限公司</td> 
         </tr> 
         <tr>
          <td class="text-center">JY13101150257400</td> 
          <td>食品经营</td> 
          <td>总局</td> 
          <td>2017-06-09</td> 
          <td>上海盒马网络科技有限公司</td> 
         </tr> 
         <tr>
          <td class="text-center">-</td> 
          <td>对增值税防伪税控系统最高开票限额的审批</td> 
          <td>总局</td> 
          <td>2017-03-03</td> 
          <td>上海盒马网络科技有限公司</td> 
         </tr> 
        </tbody>
       </table> 
       <div class=""> 
       </div> 
      </section> 
      <section class="panel b-a clear"> 
       <div class="m_ptsc" style="padding:20px 0;">
        数据来源：各官方网站，包括全国企业信用信息公示系统，中国裁判文书网、中华人民共和国最高人民法院全国法院、中国执行信息公开网、国家知识产权局官方网站、国家工商行政管理总局商标局官网、 国家版权局官方网站，为我司保存的官方网站历史记录，因参考、使用该信息造成的损失，企查查不承担任何责任。
       </div> 
      </section> 
      <script>

        $(function () {

            $('.gdchangedate').text('');
            $('.chooseHistory').find('a').on('click',function(){
                var targetDiv = $(this).parent().parent().parent().parent();
                var target = targetDiv.attr('data-box');

                var option_ = '';
                var ajaxData = {};
                console.info(target);
                switch(target){
                    case 'gd':
                        option_ = 'gdchangedate';
                        ajaxData['box'] = 'hispartner';
                        break;
                    case 'xzcf':
                        option_ = 'xzcfsource';
                        ajaxData['box'] = 'hisap';
                        break;
                    case 'xzxk':
                        option_ = 'xzxksource';
                        ajaxData['box'] = 'hisal';
                        break;
                    case 'hisjudgement':
                        option_ = 'hiscasereason';
                        ajaxData['box'] = 'hisjudgement';
                        break;
                    default :
                        break;
                }
                var option = $(this).attr('data-option');
                var value = $(this).attr('data-value');
                var text = $(this).text();
                $("input[name=" + option_ + "]").val(value);
                $("input[name=" + option_ + "]").attr('data-desc',text);
                //取所有筛选条件的值
                ajaxData[option] = $("input[name=" + option_ + "]").val();
                //拼接其他参数
                ajaxData['unique'] = $("#unique").val();
                ajaxData['companyname'] = $("#companyname").val();
                ajaxData['tab'] = 'history';
                ajaxData['p'] = '1';
                getTabListNew(ajaxData);
            });
        });


</script> 
     </div> 
    </div> 
    <div class="col-sm-3 m_rightPanels"> 
     <section class="panel b-a n-s qa-section" style="display: none;"> 
      <div class="panel-heading b-b bg-blue"> 
       <span class="font-bold font-15"><h2 class="text-primary">企业公告</h2></span> 
      </div> 
      <ul class="list-group no-bg auto" id="noticeRight"> 
      </ul> 
     </section> 
     <section class="panel b-a n-s qa-section" id="qaRightAsk"> 
      <div class="panel-heading bg-blue" style="border-bottom: none;"> 
       <img class="qa_lo" src="/material/theme/chacha/cms/v2/images/qa_lo.png" />
       <span>想了解更多这家公司的信息吗？</span> 
      </div> 
      <div class="panel-body" style="background: #F3F9FE;"> 
       <div class="clearfix ask-footer active"> 
        <input type="hidden" name="keyno" value="e45ee37279ffb3f2ce9bbbcfa39d8133" /> 
        <div class="textarea-count"> 
         <textarea placeholder="写下你的问题" maxlength="100" rows="3" class="textarea form-control"></textarea> 
         <span class="wordwrap" style="display: none;"><span class="wordCount">0</span>/<span class="maxCount">100</span></span> 
         <a onclick="askquestion(1)" class="btn btn-primary">提问</a> 
        </div> 
       </div> 
      </div> 
      <ul class="list-group no-bg auto qa-ul-list company-ul" id="companyUlQa"> 
       <a class="list-group-item clearfix"> 
        <div class="question"> 
         <span class="icon"></span>
         <div class="title">
          要是小米倒闭，你有没有什么话对小米说？
         </div> 
         <div class="count">
          <span class="text-danger">1</span>条回答
         </div> 
        </div> 
        <div class="answer"> 
         <span class="icon"></span>爱过！感谢小米搅动了互联网手机市场是我在山村老家的，此处是占位占位… 
        </div> </a> 
       <a class="list-group-item clearfix"> 
        <div class="question"> 
         <span class="icon"></span>
         <div class="title">
          小米要开发的女性手机，指的是什么？
         </div> 
         <div class="count">
          <span class="text-danger">5</span>条回答
         </div> 
        </div> 
        <div class="answer"> 
         <span class="icon"></span>早在智能手机大战初期，有一些厂商曾经炒过一段女性手机，后来也没有做成，不了了之。智能手机整体发展进入天花板，男性和女性的需求差别其实并不大，所以我觉得女性手机只是个伪概念。 
        </div> </a> 
      </ul> 
      <div class="more" style="display: none;"> 
       <a class="text-primary" href="https://pinpai.qichacha.com/own_e45ee37279ffb3f2ce9bbbcfa39d8133.html#qalist">查看全部<span id="companyUlQaCount"></span>个问答&gt;</a> 
      </div> 
     </section> 
     <section class="panel b-a n-s qa-section" style="display: none;"> 
      <div class="panel-heading b-b bg-blue"> 
       <span class="font-bold font-15"><h2 class="text-primary">本公司相关问答</h2></span> 
      </div> 
     </section> 
     <section class="panel b-a n-s qa-section" style=""> 
      <div class="panel-heading b-b"> 
       <span class="font-bold font-15"><h2>热门问答</h2></span> 
      </div> 
      <div class="slimScrollDiv" style="position: relative; overflow: hidden; width: auto; height: 434px;">
       <ul class="list-group no-bg auto qa-ul-list" id="hotUlQa" style="overflow: hidden; width: auto; height: 434px;">
        <li class="list-group-item clearfix">
         <div class="title m-b">
          <img class="logo m-r-sm" src="https://co-image.qichacha.com/CompanyImage/f1c5372005e04ba99175d5fd3db7b8fc.jpg" />
          <a href="/firm_f1c5372005e04ba99175d5fd3db7b8fc.html">深圳市腾讯计算机系统有限公司</a>
         </div>
         <div class="question" onclick="showAnswerListModal('11b98914-ae87-421a-b80a-d94bb3d74978','f1c5372005e04ba99175d5fd3db7b8fc',10)">
          <span class="icon"></span>微信禁止朋友圈分享英语学习打卡，你支持吗？
          <div class="count">
           <span class="text-danger">24</span>条回答
          </div>
         </div>
         <div class="answer" onclick="showAnswerListModal('11b98914-ae87-421a-b80a-d94bb3d74978','f1c5372005e04ba99175d5fd3db7b8fc',10)">
          <span class="icon"></span>
          <pre class="qa-pre">疯狂英语</pre>
         </div></li>
        <li class="list-group-item clearfix">
         <div class="title m-b">
          <img class="logo m-r-sm" src="https://co-image.qichacha.com/CompanyImage/49b60a8e2006546644a998547f4c9b0e.jpg" />
          <a href="/firm_49b60a8e2006546644a998547f4c9b0e.html">上海尚猷网络科技有限公司</a>
         </div>
         <div class="question" onclick="showAnswerListModal('2b50815b-ad6a-41ce-adb6-7f6129842e68','49b60a8e2006546644a998547f4c9b0e',10)">
          <span class="icon"></span>澳门赌王之子何猷君为什么会看上奚梦瑶？？？
          <div class="count">
           <span class="text-danger">23</span>条回答
          </div>
         </div>
         <div class="answer" onclick="showAnswerListModal('2b50815b-ad6a-41ce-adb6-7f6129842e68','49b60a8e2006546644a998547f4c9b0e',10)">
          <span class="icon"></span>
          <pre class="qa-pre">企查查也能看八卦？？？</pre>
         </div></li>
        <li class="list-group-item clearfix">
         <div class="title m-b">
          <img class="logo m-r-sm" src="https://co-image.qichacha.com/CompanyImage/18ff2c7ad1d11bfe40e0bec84f6d04d3.jpg" />
          <a href="/firm_18ff2c7ad1d11bfe40e0bec84f6d04d3.html">视觉(中国)文化发展股份有限公司</a>
         </div>
         <div class="question" onclick="showAnswerListModal('281455f8-de9d-476e-b87b-69f5119d6ca0','18ff2c7ad1d11bfe40e0bec84f6d04d3',10)">
          <span class="icon"></span>视觉中国“活过来”了 吗？
          <div class="count">
           <span class="text-danger">25</span>条回答
          </div>
         </div>
         <div class="answer" onclick="showAnswerListModal('281455f8-de9d-476e-b87b-69f5119d6ca0','18ff2c7ad1d11bfe40e0bec84f6d04d3',10)">
          <span class="icon"></span>
          <pre class="qa-pre">解决同行或者企业的疑难杂症包括电话党们</pre>
         </div></li>
        <li class="list-group-item clearfix">
         <div class="title m-b">
          <img class="logo m-r-sm" src="https://co-image.qichacha.com/CompanyImage/c9d80e466a765162c71287e51fb2eb8e.jpg" />
          <a href="/firm_c9d80e466a765162c71287e51fb2eb8e.html">北京德云社文化传播有限公司</a>
         </div>
         <div class="question" onclick="showAnswerListModal('235f47fe-6c8e-422f-bab1-6706ea9efd73','c9d80e466a765162c71287e51fb2eb8e',10)">
          <span class="icon"></span>如何看待德云社相声演员张云雷做出的道歉？
          <div class="count">
           <span class="text-danger">19</span>条回答
          </div>
         </div>
         <div class="answer" onclick="showAnswerListModal('235f47fe-6c8e-422f-bab1-6706ea9efd73','c9d80e466a765162c71287e51fb2eb8e',10)">
          <span class="icon"></span>
          <pre class="qa-pre">确实有错，但不至于彻底封杀，看认错态度，留校察看吧</pre>
         </div></li>
        <li class="list-group-item clearfix">
         <div class="title m-b">
          <img class="logo m-r-sm" src="https://co-image.qichacha.com/CompanyImage/c70a55cb048c8e4db7bca357a2c113e0.jpg" />
          <a href="/firm_c70a55cb048c8e4db7bca357a2c113e0.html">阿里巴巴(中国)网络技术有限公司</a>
         </div>
         <div class="question" onclick="showAnswerListModal('c38cba5b-ad8f-4505-ac90-24419f1382be','c70a55cb048c8e4db7bca357a2c113e0',10)">
          <span class="icon"></span>如何看待马云说的“婚姻第一KPI是生孩子 ”？开黄腔是否有失身份？
          <div class="count">
           <span class="text-danger">15</span>条回答
          </div>
         </div>
         <div class="answer" onclick="showAnswerListModal('c38cba5b-ad8f-4505-ac90-24419f1382be','c70a55cb048c8e4db7bca357a2c113e0',10)">
          <span class="icon"></span>
          <pre class="qa-pre">怎么生 我自己都养不活</pre>
         </div></li>
       </ul>
       <div class="slimScrollBar" style="background: rgb(0, 0, 0); width: 7px; position: absolute; top: 0px; opacity: 0.4; display: block; border-radius: 7px; z-index: 99; right: 1px; height: 224.233px;"></div>
       <div class="slimScrollRail" style="width: 7px; height: 100%; position: absolute; top: 0px; display: none; border-radius: 7px; background: rgb(51, 51, 51); opacity: 0.2; z-index: 90; right: 1px;"></div>
      </div> 
      <div class="more"> 
       <a class="text-primary" href="/more_hotqa">查看更多热门问答&gt;</a> 
      </div> 
     </section> 
     <script type="text/javascript">
    
    $(function(){

        
        gethotqa();

        
        getcompanyqa('e45ee37279ffb3f2ce9bbbcfa39d8133');
        statInputNum($('#qaRightAsk .textarea-count'),100);
        // $('#qaRightAsk .textarea').on('focus',function(){
        //     $('#qaRightAsk .ask-footer').addClass('active');
        // })
        // $('#qaRightAsk .textarea').on('blur',function(){
        //     if(!this.value){
        //         $('#qaRightAsk .ask-footer').removeClass('active');
        //     }
        // })
            })
   
    
</script> 
     <div id="promoteRight">
      <div class="m-b"> 
       <a onclick="zhugeTrack('广告-让我的企业出现在这里');" href="/order_certpay" target="_blank"> <img src="/material/theme/chacha/cms/v2/images/promoteown.png" style="width:280px;" alt="企查查" /> </a> 
      </div>
     </div> 
     <div class="panel b-a n-s" id="fapiao-title"> 
      <div class="panel-heading b-b btab"> 
       <a href="#qiyeQrcode" onclick="changeQrTAB(1,this);zhugeTrack('企业主页-在手机中查看',{'企业名称':'上海盒马网络科技有限公司'});" data-toggle="tab"><h2>在手机中查看</h2></a> 
       <a href="#fapiaoQrcode" onclick="changeQrTAB(2,this);zhugeTrack('企业主页-保存发票抬头',{'企业名称':'上海盒马网络科技有限公司'});" data-toggle="tab" class="active"><h2>保存发票抬头</h2></a> 
      </div> 
      <div class="panel-body text-center"> 
       <div id="qiyeQrcode" style="display: none;"> 
        <div id="qiye_taitou" class="m_qrp"></div> 
        <div class="m-t-xs text-dark m-b">
         <a href="/app" target="_blank" class="text-primary">企查查APP</a> 扫一扫查看企业详情
        </div> 
       </div> 
       <div id="fapiaoQrcode"> 
        <a id="fapiao_taitou" class="m_qrp" href="/tax_view?keyno=e45ee37279ffb3f2ce9bbbcfa39d8133"> </a> 
        <div class="m-t-xs text-dark">
         <a href="/app" target="_blank" class="text-primary">企查查APP</a> 扫一扫保存发票抬头
        </div> 
        <div class="m-t-md TaxView" style="display: none"> 
         <p class="text-left">名称&nbsp;:&nbsp;<span class="Name"></span></p> 
         <p class="text-left">税号&nbsp;:&nbsp;<span class="CreditCode"></span></p> 
         <p class="text-left">地址&nbsp;:&nbsp;<span class="Address"></span></p> 
         <p class="text-left">电话&nbsp;:&nbsp;<span class="PhoneNumber"></span></p> 
         <p class="text-left">开户银行&nbsp;:&nbsp;<span class="Bank"></span></p> 
         <p class="text-left">银行账户&nbsp;:&nbsp;<span class="Bankaccount"></span></p> 
        </div> 
       </div> 
      </div> 
     </div> 
     <section class="panel b-a n-s"> 
      <div class="panel-heading b-b"> 
       <span class="font-bold font-15 text-dark"><h2>企业图谱</h2></span> 
      </div> 
      <div class="panel-body"> 
       <a onclick="zhugeTrack('企业主页-查看企业图谱',{'企业名称':'上海盒马网络科技有限公司'});" href="/company_businessmap?keyNo=e45ee37279ffb3f2ce9bbbcfa39d8133&amp;name=上海盒马网络科技有限公司" target="_blank"> <img src="/material/theme/chacha/cms/v2/images/tupu.png?t=3" style="width: 100%;margin-bottom: 10px;" /> </a> 
       <a onclick="zhugeTrack('企业主页-查看企业图谱',{'企业名称':'上海盒马网络科技有限公司'});" class="btn btn-primary basePageBt" href="/company_businessmap?keyNo=e45ee37279ffb3f2ce9bbbcfa39d8133&amp;name=%E4%B8%8A%E6%B5%B7%E7%9B%92%E9%A9%AC%E7%BD%91%E7%BB%9C%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8" target="_blank">查看企业图谱</a> 
      </div> 
     </section> 
     <section class="panel b-a n-s"> 
      <div class="panel-heading b-b"> 
       <span class="font-bold font-15 text-dark"><h2>股权穿透图</h2></span> 
      </div> 
      <div class="panel-body"> 
       <a onclick="zhugeTrack('企业主页-查看投资图谱',{'企业名称':'上海盒马网络科技有限公司'});" href="/company_guquan?keyNo=e45ee37279ffb3f2ce9bbbcfa39d8133&amp;name=上海盒马网络科技有限公司" target="_blank"> <img src="/material/theme/chacha/cms/v2/images/chuantou.png?t=3" style="width: 100%;margin-bottom: 10px;" /> </a> 
       <a onclick="zhugeTrack('企业主页-查看投资图谱',{'企业名称':'上海盒马网络科技有限公司'});" class="btn btn-primary basePageBt" href="/company_guquan?keyNo=e45ee37279ffb3f2ce9bbbcfa39d8133&amp;name=%E4%B8%8A%E6%B5%B7%E7%9B%92%E9%A9%AC%E7%BD%91%E7%BB%9C%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8" target="_blank">查看股权穿透</a> 
      </div> 
     </section> 
     <section class="panel b-a n-s"> 
      <div class="panel-heading b-b"> 
       <span class="font-bold font-15 text-dark"><h2>关联图谱</h2></span> 
      </div> 
      <div class="panel-body"> 
       <a onclick="zhugeTrack('企业主页-查看关联图谱',{'企业名称':'上海盒马网络科技有限公司'});" href="/company_muhou3?keyNo=e45ee37279ffb3f2ce9bbbcfa39d8133&amp;name=上海盒马网络科技有限公司" target="_blank"> <img src="/material/theme/chacha/cms/v2/images/muhou.png?t=3" style="width: 100%;margin-bottom: 10px;" /> </a> 
       <a onclick="zhugeTrack('企业主页-查看关联图谱',{'企业名称':'上海盒马网络科技有限公司'});" class="btn btn-primary basePageBt" href="/company_muhou3?keyNo=e45ee37279ffb3f2ce9bbbcfa39d8133&amp;name=%E4%B8%8A%E6%B5%B7%E7%9B%92%E9%A9%AC%E7%BD%91%E7%BB%9C%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8" target="_blank">查看关联图谱</a> 
      </div> 
     </section> 
     <section class="panel b-a n-s"> 
      <div class="panel-heading b-b"> 
       <span class="font-bold font-15 text-dark"><h2>您可能感兴趣的企业</h2></span> 
      </div> 
      <ul class="list-group no-bg auto"> 
       <a onclick="zhugeTrack('企业主页-您可能感兴趣的公司',{'公司名称':'安徽新天地塑业有限公司'});" href="/firm_93d8fbb1e77d7886c23a65468e4ff598" target="_blank" class="list-group-item clearfix"> <span class="clear"> <span>安徽新天地塑业有限公司</span><br /> </span> </a> 
       <a onclick="zhugeTrack('企业主页-您可能感兴趣的公司',{'公司名称':'厦门市翔安区翔互利液化气供应站'});" href="/firm_2036801dac6b2aecb6b4ef76f1dcb52f" target="_blank" class="list-group-item clearfix"> <span class="clear"> <span>厦门市翔安区翔互利液化气供应站</span><br /> </span> </a> 
       <a onclick="zhugeTrack('企业主页-您可能感兴趣的公司',{'公司名称':'广西鹿寨亿建混凝土有限公司'});" href="/firm_6680fc895eaa3b178d768a686bf582e1" target="_blank" class="list-group-item clearfix"> <span class="clear"> <span>广西鹿寨亿建混凝土有限公司</span><br /> </span> </a> 
       <a onclick="zhugeTrack('企业主页-您可能感兴趣的公司',{'公司名称':'株洲开拓者机器人科技有限公司'});" href="/firm_01d02efc39b005495393cb9f2e4f532d" target="_blank" class="list-group-item clearfix"> <span class="clear"> <span>株洲开拓者机器人科技有限公司</span><br /> </span> </a> 
       <a onclick="zhugeTrack('企业主页-您可能感兴趣的公司',{'公司名称':'達仁國際有限公司'});" href="/firm_t643f4058ad1fa54428905269cd287ec" target="_blank" class="list-group-item clearfix"> <span class="clear"> <span>達仁國際有限公司</span><br /> </span> </a> 
      </ul> 
     </section> 
     <div class="m-b"> 
      <a onclick="zhugeTrack('广告-企查查小程序');" href="javascript:;" target="_blank"> <img src="https://co-image.qichacha.com/upload/chacha/img/20190319/1552977777156818.png" style="width:280px;" alt="企查查" /> </a> 
     </div> 
    </div> 
   </div> 
  </div>
 </body>
</html>"""
# 根据选择获取模块内容
def contentPage(soup, option):
    # 初始化模块信息储存空间
    moduleInf = None

    if option == "基本信息":
        # 获取基本信息模块信息
        print("基本信息")
        moduleInf = basicInfo(soup)
    elif option == "法律诉讼":
        # 获取法律诉讼信息
        print("法律诉讼")
        moduleInf = legalAction(soup)
    elif option == "经营状况":
        # 获取经营状况信息
        print("经营状况")
        moduleInf = runState(soup)
    elif option == "经营风险":
        # 获取经营风险信息
        print("经营风险")
        moduleInf = runRisk(soup)
    elif option == "企业发展":
        # 获取企业发展信息
        print("企业发展")
        moduleInf = companyDev(soup)
    elif option == "历史信息":
        # 获取企业发展信息
        print("历史信息")
        moduleInf = historyInfo(soup)
    elif option == '上市信息':
        # 获取企业上市信息
        print("上市信息")
        moduleInf = ipoInfo(soup)

    return (option, moduleInf)
    # 目前知识产权一栏不处理
    # elif option=="知识产权":
    #     #获取知识产权信息
    #     print("知识产权")
    #     #IntellectualPro(soup)


# 方法二：通过点击目录，直接获取所有内容
def getClassName(name):
    if name == '基本信息':
        return "base_info", "base_div"
    elif name == '法律诉讼':
        return "susong_info", "susong_div"
    elif name == '经营状况':
        return "run_info", "run_div"
    elif name == '经营风险':
        return "fengxian_info", "fengxian_div"
    elif name == '企业发展':
        return "report_info", "report_div"
    elif name == '知识产权':
        return "assets_info", "assets_div"
    elif name == '历史信息':
        return "history_info", "history_div"
    elif name == '上市信息':
        return "ipo_info", "ipo_div"

# 根据每个目录开始爬取内容
def beginNav():

    soup = BeautifulSoup(html)

    # 初始化公司信息内容储存表
    items = list()
    names=['基本信息','法律诉讼','经营状况','经营风险','企业发展','知识产权','历史信息']
    for name in names:
        className, id = getClassName(name)  # 获取内容对应的id和class名称

        # 根据id定位模块
        div = soup.find('div', {'id': id})

        # 开始爬取数据, type:<tuple>
        moduleInfo = contentPage(div, name)

        # 需要把内容根据名字放入列表中
        if moduleInfo[1] != None:
            items.append(moduleInfo)

    return items


beginNav()