{%- extends 'full.tpl' -%}

{% block input_group -%}
<div class="input_hidden">
{{ super() }}
</div>
{% endblock input_group %}

{%- block header -%}
{{ super() }}

<script src=//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>

<nav class="navbar navbar-inverse navbar-fixed-top">
  <div class="container">
    <div class="navbar-header">
      <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <a class="navbar-brand" href="/">GitzFL</a>
    </div>
    <div id="navbar" class="collapse navbar-collapse">
      <ul class="nav navbar-nav">
        <li class="active"><a href="/">Home</a></li>
        <li><a href="/adhoc?art=About">About</a></li>
        <li><a href="/contact">Contact</a></li>
        <li><a href="/adhoc?art=Welcome">Ad Hoc Analyses</a></li>
        <li><a href="/3d?start=1&end=8">3rd Down Analysis</a></li>

      </ul>
    </div><!--/.nav-collapse -->
  </div>
</nav>

<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-69796661-1', 'auto');
  ga('send', 'pageview');

</script>

<style type="text/css">
//div.output_wrapper {
//  margin-top: 0px;
    max-width:20000px;
//}
.input_hidden {
  display: none;
//  margin-top: 5px;
}
//div.output_area{
//  max-height:1000px;
//  max-width:20000px;
//  overflow:auto;}
</style>

{%- endblock header -%}
