dof_output = {'dof': {'value': 19.0908, 'last_updated': '2019-05-20T00:00:00'}}

dof_input = """



<html>
    <head>
        <meta name="robots" content="index, nofollow">
        <script type="text/javascript">var djConfig = {isDebug:false,parseWidgets:false,searchIds:["CALENDARIOINICIAL","CALENDARIOFINAL"]};</script>
        <script type="text/javascript" language="JavaScript" src="js/dojo-0.3.1-ajax-bm/dojo.js"></script>
        <script type="text/javascript">dojo.require("dojo.widget.MyDropdownDatePicker");</script>
        <script language="JavaScript" src="js/tipCamValidar.js" type="text/javascript"></script>
        <link type="text/css" rel="stylesheet" href="css/borders.css"/>
        <link type="text/css" rel="stylesheet" href="css/TiposCambios.css"/>
        <title>SIE - Mercado cambiario</title>
    </head>
    <body>
        <form name="tipCambMIActionForm" method="post" action="/tipcamb/tipCamIHAction.do" target="_blank">
            <input type="hidden" name="idioma" value="sp">
            <table width="80%" border="0" align="center">
                <tr>
                    <td class="titulo" align="center">
            Tipo de cambio para solventar obligaciones denominadas en d&oacute;lares de los EE.UU.A.,
                        <br>pagaderas en la Rep&uacute;blica Mexicana
            
                        <sup>1/</sup>
                    </td>
                </tr>
                <tr>
                    <td height="6">
          </td>
                </tr>
                <tr>
                    <td>
                        <table width="100%" border="0" cellspacing="0" class="renglonPar">
                            <tr>
                                <td>
                                    <table border="0" cellspacing="0" align="left">
                                        <tr>
                                            <td class="fechasFormatoSalida">
                                                <div align="center">Fecha Inicial</div>
                                            </td>
                                            <td>
                                                <div align="center"></div>
                                            </td>
                                            <td>
                                                <div align="center"></div>
                                            </td>
                                            <td class="fechasFormatoSalida">
                                                <div align="center">Fecha Final</div>
                                            </td>
                                            <td>
                                                <div align="center"></div>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td id="fechaInicial">
                                                <div align="center">
                                                    <input type="text" name="fechaInicial" size="13" value="dd/mm/aaaa" class="renglonNon">
                                                </div>
                                            </td>
                                            <td width="18">
                                                <div align="center">
                                                    <span
                          id="CALENDARIOINICIAL"
                          dojoType="MyDropdownDatePicker"
                          widgetId="INI_cal"
                          idioma="es"
                          dateFormat="%d/%m/%Y"
                          date="01/01/2006"
                          datemin="01/01/1990"
                          datemax="20/05/2019"
                          fechasInhabiles="true"
                          campoFecha="fechaInicial"
                          prefijosSeries="none">
                          </span>
                                                </div>
                                            </td>
                                            <td width="20">
                                                <div align="center">-</div>
                                            </td>
                                            <td id="fechaFinal">
                                                <div align="center">
                                                    <input type="text" name="fechaFinal" size="13" value="dd/mm/aaaa" class="renglonNon">
                                                </div>
                                            </td>
                                            <td width="18">
                                                <div align="center">
                                                    <span
                          id="CALENDARIOFINAL"
                          dojoType="MyDropdownDatePicker"
                          widgetId="FIN_cal"
                          idioma="es"
                          dateFormat="%d/%m/%Y"
                          date=""
                          datemin="01/01/1990" datemax="20/05/2019"
                          fechasInhabiles="true"
                          campoFecha="fechaFinal"
                          prefijosSeries="none">
                          </span>
                                                </div>
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                                <td align="right">
                                    <table border="0" cellspacing="0">
                                        <tr>
                                            <td class="fechasFormatoSalida">
                                                <div align="center">Formato
                        </div>
                                            </td>
                                            <td>&nbsp;</td>
                                        </tr>
                                        <tr>
                                            <td>
                                                <div align="center">
                                                    <select name="salida" class="renglonNon">
                                                        <option value="HTML" selected="selected" class="renglonNon">HTML</option>
                                                        <option value="XLS" class="renglonNon">XLS</option>
                                                    </select>
                                                </div>
                                            </td>
                                            <td>
                                                <input type="submit" value="Consultar series" onclick="return  esMenorIgual(document.tipCambMIActionForm.fechaInicial.value,document.tipCambMIActionForm.fechaFinal.value,'sp')
        && dentroDeRango(document.tipCambMIActionForm.fechaInicial.value,document.tipCambMIActionForm.fechaFinal.value,'01/01/1990','01/01/2050','sp')" class="botonesSIE">
                      
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
                <tr>
                    <td height="6"></td>
                </tr>
                <tr>
                    <td>
                        <table border="0" cellpadding="0" cellspacing="0" width="100%">
                            <tr>
                                <td>
                                    <table border="0" cellpadding="0" cellspacing="0" align="center">
                                        <tr>
                                            <td class="b4"></td>
                                            <td class="b5">
                                                <table border="0" width="100%" cellspacing="0">
                                                    <tr>
                                                        <td height="8"></td>
                                                    </tr>
                                                    <tr class="renglonTituloColumnas" align="center">
                                                        <td align="left">
                              Fecha
                            </td>
                                                        <td align="right" width="111">
                              FIX
                              
                                                            <sup>2/</sup>
                                                        </td>
                                                        <td align="right" width="111">
                              Publicaci&oacute;n DOF
                              
                                                            <sup>3/</sup>
                                                        </td>
                                                        <td align="right" width="111">
                              Para pagos
                              
                                                            <sup>4/</sup>
                                                        </td>
                                                        <!--td><input type="checkbox" name="seriesSeleccionadas" value="FIX">
                            </td-->
                          
                                                    </tr>
                                                    <tr class="renglonNon" align="center">
                                                        <td style="padding-top:5px;padding-bottom:5px;" align="left">
                                20/05/2019
                              </td>
                                                        <td align="right">
                                19.0908
                              </td>
                                                        <td align="right">
                                19.1454
                              </td>
                                                        <td align="right">
                                19.0710
                              </td>
                                                        <!--td>
                                &nbsp;
                              </td-->
                            
                                                    </tr>
                                                    <tr class="renglonPar" align="center">
                                                        <td style="padding-top:5px;padding-bottom:5px;" align="left">
                                19/05/2019
                              </td>
                                                        <td align="right">
                                N/E
                              </td>
                                                        <td align="right">
                                N/E
                              </td>
                                                        <td align="right">
                                19.0710
                              </td>
                                                        <!--td>
                                &nbsp;
                              </td-->
                            
                                                    </tr>
                                                    <tr class="renglonNon" align="center">
                                                        <td style="padding-top:5px;padding-bottom:5px;" align="left">
                                18/05/2019
                              </td>
                                                        <td align="right">
                                N/E
                              </td>
                                                        <td align="right">
                                N/E
                              </td>
                                                        <td align="right">
                                19.0710
                              </td>
                                                        <!--td>
                                &nbsp;
                              </td-->
                            
                                                    </tr>
                                                    <tr class="renglonPar" align="center">
                                                        <td style="padding-top:5px;padding-bottom:5px;" align="left">
                                17/05/2019
                              </td>
                                                        <td align="right">
                                19.1454
                              </td>
                                                        <td align="right">
                                19.0710
                              </td>
                                                        <td align="right">
                                19.1236
                              </td>
                                                        <!--td>
                                &nbsp;
                              </td-->
                            
                                                    </tr>
                                                    <tr class="renglonNon" align="center">
                                                        <td style="padding-top:5px;padding-bottom:5px;" align="left">
                                16/05/2019
                              </td>
                                                        <td align="right">
                                19.0710
                              </td>
                                                        <td align="right">
                                19.1236
                              </td>
                                                        <td align="right">
                                19.1427
                              </td>
                                                        <!--td>
                                &nbsp;
                              </td-->
                            
                                                    </tr>
                                                    <tr class="renglonPar" align="center">
                                                        <td style="padding-top:5px;padding-bottom:5px;" align="left">
                                15/05/2019
                              </td>
                                                        <td align="right">
                                19.1236
                              </td>
                                                        <td align="right">
                                19.1427
                              </td>
                                                        <td align="right">
                                19.1928
                              </td>
                                                        <!--td>
                                &nbsp;
                              </td-->
                            
                                                    </tr>
                                                    <tr class="renglonNon" align="center">
                                                        <td style="padding-top:5px;padding-bottom:5px;" align="left">
                                14/05/2019
                              </td>
                                                        <td align="right">
                                19.1427
                              </td>
                                                        <td align="right">
                                19.1928
                              </td>
                                                        <td align="right">
                                19.1374
                              </td>
                                                        <!--td>
                                &nbsp;
                              </td-->
                            
                                                    </tr>
                                                </table>
                                            </td>
                                            <td class="b6"></td>
                                        </tr>
                                        <tr>
                                            <td class="b7"></td>
                                            <td class="b8"></td>
                                            <td class="b9"></td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                            <!--tr><td height="6"></td></tr-->
                            <tr>
                                <td>
                                    <table width="100%" align="center">
                                        <tr>
                                            <td class="notasNotas" align="justify">
                                                <b>1/</b> Para mayor informaci&oacute;n sobre este tipo de cambio consulte:
                                                <a target="_blank" href="http://www.banxico.org.mx/disposiciones/normativa/circular-3-2012/%7B60333E30-FC8B-94D3-E1D0-4AF8E3C75E90%7D.pdf ">El T&iacute;tulo Tercero, Cap&iacute;tulo V de la Circular 3/2012 del Banco de M&eacute;xico</a>.
                                            </td>
                                        </tr>
                                        <tr>
                                            <td class="notasNotas" align="justify">
                                                <b>2/</b> El tipo de cambio FIX es determinado por el Banco de M&eacute;xico los d&iacute;as h&aacute;biles bancarios con base en un promedio de las cotizaciones del mercado de cambios al mayoreo para operaciones liquidables el segundo d&iacute;a h&aacute;bil bancario siguiente. Dichas cotizaciones se obtienen de plataformas de transacci&oacute;n cambiaria y otros medios electr&oacute;nicos con representatividad en el mercado de cambios. El Banco de M&eacute;xico da a conocer el FIX a partir de las 12:00 horas de todos los d&iacute;as h&aacute;biles bancarios.
                                            </td>
                                        </tr>
                                        <tr>
                                            <td class="notasNotas" align="justify">
                                                <b>3/</b> El tipo de cambio FIX se publica por el Banco de M&eacute;xico en el Diario Oficial de la Federaci&oacute;n el d&iacute;a h&aacute;bil bancario inmediato siguiente a su determinaci&oacute;n.
                                            </td>
                                        </tr>
                                        <tr>
                                            <td class="notasNotas" align="justify">
                                                <b>4/</b> El tipo de cambio que se debe de utilizar el d&iacute;a de hoy para calcular el equivalente en pesos del monto de las obligaciones de pago denominadas en d&oacute;lares de los EE.UU.A. para ser cumplidas en la Rep&uacute;blica Mexicana, debe de ser el publicado por el Banco de M&eacute;xico en el Diario Oficial de la Federaci&oacute;n el d&iacute;a h&aacute;bil bancario inmediato anterior.
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
            </table>
        </form>
    </body>
</html>"""
