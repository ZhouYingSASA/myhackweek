<template>
    <div id="screen_bg">
        <Nav></Nav>
    </div>
</template>

<script>
import Nav from './Nav.vue'

export default {
    components: {
        Nav
    },
    name: 'Header',
    data() {
        return {}
    },
    mounted() {}
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
#screen_bg {
    background: url(../../static/images/456.jpg);
    background-size: cover;
    position: absolute;
    width: 100%;
    height: 620px;
    z-index: -1;
}
</style>
