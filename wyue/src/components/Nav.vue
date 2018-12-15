<template>
    <nav class="navbar navbar-expand-md fixed-top">
        <ul class="navbar-nav mr-auto nav-pills nav-fill">
            <li class="nav-item" style="width:127px">
                <a class="nav-link tab navbar-brand" href="#"><img src="../../static/images/home.png" style="width:23px;margin: 0 6px 2px 0;">WYue<span class="sr-only">(current)</span></a>
            </li>
            <li class="nav-item">
                <a class="nav-link tab" href="#"><img src="../../static/images/picture.png" style="width:20px;margin: 0 6px 0 0;">图片</a>
            </li>
            <li class="nav-item">
                <a class="nav-link tab" href="#"><img src="../../static/images/rocket.png" style="width:30px;margin: 0 2px 0 0;">归档</a>
            </li>
            <li class="nav-item">
                <a class="nav-link tab" href="#"><img src="../../static/images/donut.png" style="width:24px;margin: 0 5px 0 0;">留言</a>
            </li>
        </ul>
        <ul class="navbar-nav nav flex-column nav-pills nav-fill hover-about">
            <li class="nav-item">
                <a class="nav-link tab" href="#"><img src="../../static/images/chick.png" style="width:24px;margin: 0 6px 0 0;">链接</a>
            </li>
            <li class="nav-item">
                <a class="nav-link Active" href="https://www.baidu.com/">Activeee</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="#">Linkeeeee</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="https://www.baidu.com/">Linkeeeee</a>
            </li>
            <li class="nav-item">
                <a class="nav-link disabled" href="https://www.baidu.com/">Disabled</a>
            </li>
        </ul>
    </nav>
</template>

<script>
export default {
    name: 'Nav',
    data() {
        return {}
    },
    mounted() {
        if ($(window).width() > 800) {
            //如果窗体的宽度大于800
            var navBar = $('nav')
            //获取navBar对象
            $(window).scroll(function() {
                if (
                    $(window).scrollTop() > 700
                ) {
                    navBar.slideUp(150);
                } else {
                    navBar.slideDown(200);
                }
            })
        }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
#screen_bg {
    background: url(/static/images/header.jpg);
    background-size: cover;
    position: absolute;
    width: 100%;
    height: 100%;
    z-index: -1;
}
#back-to-top {
    position: fixed;
    right: 50px;
    z-index: 9;
    width: 70px;
    height: 900px;
    background: url('/static/images/scroll.png');
    transition: 0.5s;
    cursor: pointer;
}
h1,
h2 {
    font-weight: normal;
}

nav {
    max-width: 100%;
    opacity: 0.8;
    background-color: hsla(5, 92%, 76%, 0.8);
    color: #fff;
    height: 40px;
    z-index: 10;
    ul {
        max-width: 80%;
        display: flex;
        list-style-type: none;
        padding: 0;
        flex-direction: row;
        .nav-item {
            padding: 0;
            margin: 0;
            width: 80px;
            &:hover {
                background-color: hsla(5, 92%, 76%, 0.8);
                font-weight: 700;
            }
            .navbar-brand {
                margin-right: 0;
            }
        }
        li {
            display: inline-block;
            margin: 0 10px;
            a {
                color: #fff;
                .navbar-nav {
                    margin-right: 0;
                }
                .navbar-brand {
                    margin: 2px 0 0 0;
                }
                .tab {
                    position: relative;
                    &:hover {
                        font-weight: 700;
                    }
                }
            }
        }
    }
}

.hover-about {
    background-color: hsla(5, 92%, 76%, 0.8);
    height: 40px;
    position: fixed;
    right: 0;
    top: 0px;
    color: #000;
    transition: height 1s;
    &:hover {
        height: 200px;
    }
}
</style>