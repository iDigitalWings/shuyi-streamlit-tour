import numpy as np
import altair as alt
import pandas as pd
import streamlit as st
import datetime
import time
import random

st.set_page_config(layout="wide", page_title='数翼 Streamlit 教程')
st.title('数翼 Streamlit 教程')

expanded = True


title = "数据展示"
with st.expander(title, expanded):
    expanded = False
    st.header(title, divider='rainbow')

    col1, col2 = st.columns(2)
    with col1:
        st.subheader('高亮')
        df = pd.DataFrame(
            np.random.randn(4, 6),
            columns=('col %d' % i for i in range(6)))

        st.dataframe(df.style.highlight_max(axis=0))
    with col2:
        st.subheader('定制表格')
        df = pd.DataFrame(
            {
                "name": ["Roadmap", "Extras", "Issues"],
                "url": ["https://roadmap.streamlit.app", "https://extras.streamlit.app",
                        "https://issues.streamlit.app"],
                "stars": [random.randint(0, 1000) for _ in range(3)],
                "views_history": [[random.randint(0, 5000) for _ in range(30)] for _ in range(3)],
            }
        )
        st.dataframe(
            df,
            column_config={
                "name": "App name",
                "stars": st.column_config.NumberColumn(
                    "Github Stars",
                    help="Number of stars on GitHub",
                    format="%d ⭐",
                ),
                "url": st.column_config.LinkColumn("App URL"),
                "views_history": st.column_config.LineChartColumn(
                    "Views (past 30 days)", y_min=0, y_max=5000
                ),
            },
            hide_index=True,
        )

    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader('编辑表格')
        df = pd.DataFrame(
            [
                {"command": "st.selectbox", "rating": 4, "is_widget": True},
                {"command": "st.balloons", "rating": 5, "is_widget": False},
                {"command": "st.time_input", "rating": 3, "is_widget": True},
            ]
        )
        edited_df = st.data_editor(
            df,
            column_config={
                "command": "Streamlit Command",
                "rating": st.column_config.NumberColumn(
                    "Your rating",
                    help="How much do you like this command (1-5)?",
                    min_value=1,
                    max_value=5,
                    step=1,
                    format="%d ⭐",
                ),
                "is_widget": "Widget ?",
            },
            disabled=["command", "is_widget"],
            hide_index=True,
            use_container_width=True
        )

        favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
        st.markdown(f"Your favorite command is **{favorite_command}** 🎈")
    with col2:
        st.subheader('指标')
        col01, col02, col03 = st.columns(3)
        col01.metric("Temperature", "70 °F", "1.2 °F")
        col02.metric("Wind", "9 mph", "-8%")
        col03.metric("Humidity", "86%", "4%")
    with col3:
        st.subheader('JSON')
        st.json({
            'foo': 'bar',
            'baz': 'boz',
            'stuff': [
                'stuff 1',
                'stuff 2',
                'stuff 3',
                'stuff 5',
            ],
        })

title = "提示和进度"
with st.expander(title, expanded):
    expanded = False
    st.header(title, divider='rainbow')

    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader('效果')
        if st.button('气球'):
            st.balloons()
        if st.button('下雪'):
            st.snow()
    with col2:
        st.subheader('提示')
        st.error('错误提示', icon="🚨")
        st.warning('warning 提示', icon="⚠️")
        st.info('info 提示', icon="ℹ️")
        st.success('成功!', icon="✅")
    with col3:
        st.subheader('异常')
        e = RuntimeError('This is an exception of type RuntimeError')
        st.exception(e)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader('进度条')
        my_bar = st.progress(100)


        def start():
            my_bar.progress(0)
            time.sleep(1)
            for percent_complete in range(100):
                time.sleep(0.01)
                my_bar.progress(percent_complete + 1)


        if st.button('重新开始'):
            start()
    with col2:
        st.subheader('进度圈')
        with st.spinner('Wait for it...'):
            time.sleep(1)
        st.success('Done!')

    with col3:
        st.subheader('提示')
        if st.button('提示'):
            st.toast('耶!', icon='🎉')
            time.sleep(0.3)
            st.toast('耶!', icon='🎉')
            time.sleep(0.3)
            st.toast('耶!', icon='🎉')
            time.sleep(0.3)
            st.toast('耶!', icon='🎉')

title = "布局"
with st.expander(title, expanded):
    expanded = False
    st.header(title, divider='rainbow')

    st.sidebar.header('个性设置')
    user_name = st.sidebar.text_input('你的昵称')
    user_emoji = st.sidebar.selectbox('当前的心情', ['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])
    user_food = st.sidebar.selectbox('你今天的目标是什么?',
                                     ['', '学会 Streamlit', '构建一个人工智能应用'])

    st.subheader('个人信息分栏展示')
    col1, col2, col3 = st.columns(3)
    with col1:
        if user_name != '':
            st.write(f'👋 欢迎 {user_name}!')
        else:
            st.write('请输入你的 **昵称**!')
    with col2:
        if user_emoji != '':
            st.write(f' 我现在的心情 {user_emoji}')
        else:
            st.write('请选择你的心情')

    with col3:
        if user_food != '':
            st.write(f'我今天的目标是 **{user_food}**')
        else:
            st.write('请选择你的目标')

    st.subheader('自定义宽度列')
    col1, col2, col3 = st.columns([2, 3, 5])
    with col1:
        if user_name != '':
            st.write(f'👋 欢迎 {user_name}!')
        else:
            st.write('请输入你的 **昵称**!')

    with col2:
        if user_emoji != '':
            st.write(f' 我现在的心情 {user_emoji}')
        else:
            st.write('请选择你的心情')

    with col3:
        if user_food != '':
            st.write(f'我今天的目标是 **{user_food}**')
        else:
            st.write('请选择你的目标')

    st.subheader('Tab 布局')
    tab1, tab2, tab3 = st.tabs(["兴趣爱好", "工作经历", "作品连接"])
    with tab1:
        st.header(":rainbow[我的兴趣爱好。。。]")

    with tab2:
        st.header(":rainbow[我的工作经历。。。]")

    with tab3:
        st.header(":rainbow[我的作品连接。。。]")

title = "表单"
with st.expander(title, expanded):
    expanded = False
    st.header(title, divider='rainbow')

    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader('按钮')
        if st.button('付款', type='primary'):
            st.write('付款成功!')
        else:
            st.write('请付款')
    with col2:
        st.subheader('下载按钮')


        @st.cache_resource
        def convert_df(df):
            return df.to_csv().encode('utf-8')


        chart_data = pd.DataFrame(
            np.random.randn(20, 3),
            columns=['a', 'b', 'c'])
        csv = convert_df(chart_data)

        st.download_button(
            label="导出 Excel",
            data=csv,
            file_name='年度报表.csv',
            mime='text/csv',
        )
    with col3:
        st.subheader('复选框')
        agree = st.checkbox('自动登录')

        if agree:
            st.write('我们下次将为您自动登录')

    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader('开关')
        on = st.toggle('启用GPT4')
        if on:
            st.write('已经为您启动 GPT4')
    with col2:
        st.subheader('单选')
        llm = st.radio(
            "请选择你要使用的大语言模型",
            [":rainbow[ChatGPT]", "Claude 2", "Bard"],
            captions=["来自 OpenAI", "来自 Anthropic", "来自 Google"])

        if llm == ':rainbow[ChatGPT]':
            st.write('你选择了 ChatGPT')
        else:
            st.write("你选择了其他")
    with col3:
        st.subheader('下拉框')
        option = st.selectbox(
            '选择您的付费方式',
            ('支付宝', '微信', '银行卡'))

        st.write('你选择了:', option)

    st.subheader('多选下拉')
    options = st.multiselect(
        '请选择你要启用的工具',
        ['天气预报', '项目管理', '编程导师', '文章助手'],
        ['项目管理', '编程导师'])

    st.write('你选择了下面工具:', options)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader('文本输入')
        title = st.text_input('请输入你的问题', '如何一夜暴富')
        st.write('你的问题是：', title)
    with col2:
        st.subheader('数字输入')
        number = st.number_input('请输入金额', value=99, step=1)
        st.write('当前金额是 ', number)
    with col3:
        st.subheader('颜色')
        color = st.color_picker('选择你的主题颜色', '#8824e2')
        st.write('当前主题颜色：', color)

    st.subheader('文本输入')
    txt = st.text_area('Text to analyze', '''    arr = np.random.normal(1, 1, size=100)
    fig, ax = plt.subplots()
    ax.hist(arr, bins=20)
    st.pyplot(fig)
    st.subheader('使用 altair')
    c = alt.Chart(chart_data).mark_circle().encode(
        x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
    st.altair_chart(c, use_container_width=True)''')

    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader('日期')
        d = st.date_input("请选择你的生日", datetime.date(2000, 1, 1))
        st.write('你的生日是:', d)
    with col2:
        st.subheader('日期范围')
        today = datetime.datetime.now()
        next_year = today.year + 1
        jan_1 = datetime.date(next_year, 1, 1)
        dec_31 = datetime.date(next_year, 12, 31)

        d = st.date_input(
            "明年的假期旅行时间：",
            (jan_1, datetime.date(next_year, 1, 7)),
            jan_1,
            dec_31,
            format="MM.DD.YYYY",
        )
        st.write(d)
    with col3:
        st.subheader('时间')
        t = st.time_input('明天几点起床', datetime.time(8, 45))
        st.write('我会在明天', t, '叫你起床')

    col1, col2 = st.columns(2)
    with col1:
        from io import StringIO

        uploaded_file = st.file_uploader("选择文件")
        if uploaded_file is not None:
            # To read file as bytes:
            bytes_data = uploaded_file.getvalue()
            st.write(bytes_data)

            # To convert to a string based IO:
            stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
            st.write(stringio)

            # To read file as string:
            string_data = stringio.read()
            st.write(string_data)

            # Can be used wherever a "file-like" object is accepted:
            dataframe = pd.read_csv(uploaded_file)
            st.write(dataframe)
    with col2:
        uploaded_files = st.file_uploader("选择所有的 CSV 文件", accept_multiple_files=True)
        for uploaded_file in uploaded_files:
            bytes_data = uploaded_file.read()
            st.write("filename:", uploaded_file.name)
            st.write(bytes_data)

    st.subheader('表单')
    with st.form('myform'):
        st.text_input('Name')
        st.text_input('Password')
        submitted = st.form_submit_button('登录')

title = "图表"
with st.expander(title, expanded):
    expanded = False
    st.header(title, divider='rainbow')

    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])

    st.subheader('线')
    col1, col2 = st.columns(2)
    st.line_chart(chart_data)

    st.subheader('区域')
    st.area_chart(chart_data)
    st.subheader('柱')
    st.bar_chart(chart_data)

    st.subheader('使用 matplotlib')
    import matplotlib.pyplot as plt

    arr = np.random.normal(1, 1, size=100)
    fig, ax = plt.subplots()
    ax.hist(arr, bins=20)
    st.pyplot(fig)

    st.subheader('使用 altair')
    c = alt.Chart(chart_data).mark_circle().encode(
        x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
    st.altair_chart(c, use_container_width=True)

    st.subheader('使用 vega lite')
    st.vega_lite_chart(chart_data, {
        'mark': {'type': 'circle', 'tooltip': True},
        'encoding': {
            'x': {'field': 'a', 'type': 'quantitative'},
            'y': {'field': 'b', 'type': 'quantitative'},
            'size': {'field': 'c', 'type': 'quantitative'},
            'color': {'field': 'c', 'type': 'quantitative'},
        },
    })

    st.subheader('使用 plotly')
    import plotly.figure_factory as ff

    # Add histogram data
    x1 = np.random.randn(200) - 2
    x2 = np.random.randn(200)
    x3 = np.random.randn(200) + 2
    # Group data together
    hist_data = [x1, x2, x3]
    group_labels = ['Group 1', 'Group 2', 'Group 3']
    # Create distplot with custom bin_size
    fig = ff.create_distplot(
        hist_data, group_labels, bin_size=[.1, .25, .5])
    # Plot!
    st.plotly_chart(fig, use_container_width=True)

    st.subheader('使用 pydeck')
    import pydeck as pdk

    chart_data = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
        columns=['lat', 'lon'])
    st.pydeck_chart(pdk.Deck(
        map_style=None,
        initial_view_state=pdk.ViewState(
            latitude=37.76,
            longitude=-122.4,
            zoom=11,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                'HexagonLayer',
                data=chart_data,
                get_position='[lon, lat]',
                radius=200,
                elevation_scale=4,
                elevation_range=[0, 1000],
                pickable=True,
                extruded=True,
            ),
            pdk.Layer(
                'ScatterplotLayer',
                data=chart_data,
                get_position='[lon, lat]',
                get_color='[200, 30, 0, 160]',
                get_radius=200,
            ),
        ],
    ))

    st.subheader('地图')
    df = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
        columns=['lat', 'lon'])

    st.map(df)

title = "滑条组件接收用户的输入"
with st.expander(title, expanded):
    expanded = False
    st.header(title, divider='rainbow')

    from datetime import time, datetime

    st.subheader('默认')
    age = st.slider('你多大了?', 0, 130, 25)
    st.write("我今年", age, '岁')

    st.subheader('范围')
    values = st.slider(
        '请选择你可以接受的价格范围',
        0.0, 100.0, (25.0, 75.0))
    st.write('我可以接受的价格是:', values)

    st.subheader('时间范围')
    appointment = st.slider(
        "请选择你的摸鱼时间:",
        value=(time(11, 30), time(12, 45)))
    st.write("你可以在下面时间摸鱼:", appointment)

    st.subheader('日期时间')
    start_time = st.slider(
        "选择你的项目开始时间?",
        value=datetime(2023, 9, 1, 9, 30),
        format="MM/DD/YY - hh:mm")
    st.write("开始时间:", start_time)

title = "万能写方法（write）"
with st.expander(title, expanded):
    expanded = False
    st.header(title, divider='rainbow')

    st.subheader('字符串')
    st.write('你好, *老王!* :sunglasses:')

    st.subheader('数字')
    st.write(1234)

    st.subheader('表格')
    df = pd.DataFrame({
        '排名': [1, 2, 3, 4],
        '速度': [10, 20, 30, 40]
    })
    st.write(df)

    st.subheader('文本+表格')
    st.write('这是一个数据表格:', df, '上面是一个数据表格.')

    st.subheader('可视化图表')
    df2 = pd.DataFrame(
        np.random.randn(200, 3),
        columns=['a', 'b', 'c'])
    c = alt.Chart(df2).mark_circle().encode(
        x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
    st.write(c)

title = "按钮示例"
with st.expander(title, expanded):
    expanded = False
    st.header(title)
    if st.button('问个好'):
        st.write('你好，大爷')
    else:
        st.write('啥也不是')

title = "Hello World"
with st.expander(title, expanded):
    st.write('你好世界!')
    st.write('来自未来的某某某!')
