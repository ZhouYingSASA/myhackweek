<template>
    <div id="app">
        <router-view />
        <Header></Header>
        <p>a</p>
        <p>a</p>
        <p>a</p>
        <p>a</p>
        <p>a</p>
        <p>a</p>
        <p>a</p>
        <p>a</p>
        <p>a</p>
        <p>a</p>
        <p>a</p>
        <p>a</p>
        <p>a</p>
        <p>a</p>
        <p>a</p>
        <p>a</p>
        <p>a</p>
        <p>a</p>
        <p>a</p>
        <p>a</p>
        <p>a</p>
        <p>a</p>
        <p>a</p>
        <p>a</p>
        <p>a</p>
        <p>a</p>
        <p>a</p>
        <p>a</p>
        <p>a</p>
        <p>a</p>
        <p>a</p>
        <p>a</p>
        <p>a</p>
        <p>a</p>
        <p>a</p>
        <p>a</p>
        <p>a</p>
        <p>a</p>
        <p>a</p>
        <p>a</p>
        <p>a</p>
        <p>a</p>
        <p>a</p>
        <p>a</p>
        <p>a</p>
        <p>a</p>
        <p>a</p>
        <p>a</p>
        <p>a</p>
        <p>a</p>
        <p>a</p>
        <p>a</p>
        <p>a</p>
        <p>a</p>
        <p>a</p>
        <p>a</p>
        <p>a</p>
        <p>a</p>

        <div id="back-to-top" class="red" data-scroll="body" style="top:-900px;color:red;">回到顶部 </div>
        <canvas id="evanyou" width="1920" height="934"></canvas>
    </div>
</template>
<script>
import { background } from 'assets/js/background.js'
import { scroll } from 'assets/js/scroll.js'
import Header from './components/Header.vue'

export default {
    components: {
        Header
    },
    name: 'App',
    mounted() {
        background('evanyou')
        scroll()
    }
}
</script>

<style type="text/css">
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
#app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 0;
}
#evanyou {
    position: fixed;
    width: 100%;
    height: 100%;
    left: 0;
    top: 0;
}

</style>
