from login import models
from pyecharts.charts import Pie, Line, Bar, Funnel
from pyecharts import options as opt


def html_pie_sex():
    user = models.UserInfo.objects.all()
    male = user.filter(sex="男").count()
    female = user.filter(sex="女").count()
    secret = user.filter(sex="保密").count()
    sex = ['男', '女', '保密']
    count = [male, female, secret]

    pie_sex = Pie(init_opts=opt.InitOpts(height='400px', page_title='性别比列'))

    pie_sex.add("",
                [list(data) for data in zip(sex, count)],
                radius=["30%", "75%"],
                rosetype="radius"
                )
    pie_sex.set_global_opts(title_opts=opt.TitleOpts(title='B站男女比例'))
    pie_sex.render('./login/templates/pie_sex.html')


def html_funnel_level():
    user = models.UserInfo.objects.all()
    level_x = ['level1', 'level2', 'level3', 'level4', 'level5', 'level6']
    level_y = [user.filter(level='1').count(), user.filter(level='2').count(), user.filter(level='3').count(),
               user.filter(level='4').count(), user.filter(level='5').count(), user.filter(level='6').count()]

    data = [[level_x[i], level_y[i]] for i in range(len(level_x))]
    level = Funnel(init_opts=opt.InitOpts(height='600px', page_title='各等级数量'))
    level.add(
        "等级",
        data_pair=data,
        sort_='ascending',
        label_opts=opt.LabelOpts(is_show=True, position='inside'),
        gap=2,
    )
    level.set_global_opts(title_opts=opt.TitleOpts(title='B站各等级数量'))
    level.render('./login/templates/funnel_level.html')


def html_bar_followers():
    users = models.UserInfo.objects.all().values('name', 'follower').order_by("follower")[
            models.UserInfo.objects.all().count() - 15:models.UserInfo.objects.all().count()]
    follower_y = []
    name_x = []
    for user in users:
        follower_y.append(user['follower'])
        name_x.append(user['name'])
    # print(name_x, follower_y)
    bar_followers = Bar(init_opts=opt.InitOpts(height='800px', page_title='UP粉丝数量排行'))
    bar_followers.add_xaxis(name_x)
    bar_followers.add_yaxis('用户名', follower_y)
    bar_followers.reversal_axis()
    bar_followers.set_series_opts(label_opts=opt.LabelOpts(position='right'))
    bar_followers.set_global_opts(title_opts=opt.TitleOpts(title='UP粉丝数量排行'))
    bar_followers.render('./login/templates/bar_followers.html')


def html_pie_vip():
    user = models.UserInfo.objects.all()
    vip_null = user.filter(vip="").count()
    vip_ = user.filter(vip="大会员").count()
    vip_year = user.filter(vip="年度大会员").count()
    vip_decade = user.filter(vip='十年大会员').count()
    vip = ['', '大会员', '年度大会员', '十年大会员']
    count = [vip_null, vip_, vip_year, vip_decade]
    pie_sex = Pie(init_opts=opt.InitOpts(height='500px', page_title='会员比例'))
    pie_sex.add("",
                [list(data) for data in zip(vip, count)],
                radius=["30%", "75%"],
                rosetype="radius"
                )
    pie_sex.set_global_opts(title_opts=opt.TitleOpts(title='B站会员比例'))
    pie_sex.render('./login/templates/pie_vip.html')

