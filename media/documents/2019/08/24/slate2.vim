" Vim color file - slate2
" Generated by http://bytefluent.com/vivify 2017-04-01
set background=dark
if version > 580
	hi clear
	if exists("syntax_on")
		syntax reset
	endif
endif

set t_Co=256
let g:colors_name = "slate2"

"hi TabLineSel -- no settings --
"hi CTagsMember -- no settings --
"hi CTagsGlobalConstant -- no settings --
hi Normal guifg=#d0d0d0 guibg=#1b1b1b guisp=#1b1b1b gui=NONE ctermfg=252 ctermbg=234 cterm=NONE
"hi CTagsImport -- no settings --
"hi CTagsGlobalVariable -- no settings --
"hi SpellRare -- no settings --
"hi EnumerationValue -- no settings --
"hi Float -- no settings --
"hi CursorLine -- no settings --
"hi Union -- no settings --
"hi TabLineFill -- no settings --
"hi CursorColumn -- no settings --
"hi EnumerationName -- no settings --
"hi SpellCap -- no settings --
"hi SpellLocal -- no settings --
"hi DefinedName -- no settings --
"hi MatchParen -- no settings --
"hi LocalVariable -- no settings --
"hi SpellBad -- no settings --
"hi CTagsClass -- no settings --
"hi TabLine -- no settings --
"hi clear -- no settings --
"hi semicolon -- no settings --
"hi vimhigroup -- no settings --
hi IncSearch guifg=#000000 guibg=#e7e7e7 guisp=#e7e7e7 gui=bold ctermfg=NONE ctermbg=254 cterm=bold
hi WildMenu guifg=#000000 guibg=#a0a0a0 guisp=#a0a0a0 gui=bold ctermfg=NONE ctermbg=247 cterm=bold
hi SignColumn guifg=#d0d0d0 guibg=#3d3d3d guisp=#3d3d3d gui=NONE ctermfg=252 ctermbg=237 cterm=NONE
hi SpecialComment guifg=#e0c07e guibg=#1b1b1b guisp=#1b1b1b gui=NONE ctermfg=180 ctermbg=234 cterm=NONE
hi Typedef guifg=#f09479 guibg=#1b1b1b guisp=#1b1b1b gui=NONE ctermfg=216 ctermbg=234 cterm=NONE
hi Title guifg=#e7e7e7 guibg=#1b1b1b guisp=#1b1b1b gui=bold ctermfg=254 ctermbg=234 cterm=bold
hi Folded guifg=#d0d0d0 guibg=#525252 guisp=#525252 gui=NONE ctermfg=252 ctermbg=239 cterm=NONE
hi PreCondit guifg=#d7a0d7 guibg=#1b1b1b guisp=#1b1b1b gui=NONE ctermfg=182 ctermbg=234 cterm=NONE
hi Include guifg=#d7a0d7 guibg=#1b1b1b guisp=#1b1b1b gui=NONE ctermfg=182 ctermbg=234 cterm=NONE
hi StatusLineNC guifg=#000000 guibg=#878787 guisp=#878787 gui=bold ctermfg=NONE ctermbg=102 cterm=bold
hi NonText guifg=#878787 guibg=#1b1b1b guisp=#1b1b1b gui=bold ctermfg=102 ctermbg=234 cterm=bold
hi DiffText guifg=#d0d0d0 guibg=#00008b guisp=#00008b gui=bold ctermfg=252 ctermbg=18 cterm=bold
hi ErrorMsg guifg=#ffffff guibg=#ee2c2c guisp=#ee2c2c gui=bold ctermfg=15 ctermbg=13 cterm=bold
hi Ignore guifg=#373737 guibg=#1b1b1b guisp=#1b1b1b gui=NONE ctermfg=237 ctermbg=234 cterm=NONE
hi Debug guifg=#e0c07e guibg=#1b1b1b guisp=#1b1b1b gui=NONE ctermfg=180 ctermbg=234 cterm=NONE
hi PMenuSbar guifg=NONE guibg=#24292e guisp=#24292e gui=NONE ctermfg=NONE ctermbg=236 cterm=NONE
hi Identifier guifg=#7ee0ce guibg=#1b1b1b guisp=#1b1b1b gui=NONE ctermfg=116 ctermbg=234 cterm=NONE
hi SpecialChar guifg=#e0c07e guibg=#1b1b1b guisp=#1b1b1b gui=NONE ctermfg=180 ctermbg=234 cterm=NONE
hi Conditional guifg=#f09479 guibg=#1b1b1b guisp=#1b1b1b gui=NONE ctermfg=216 ctermbg=234 cterm=NONE
hi StorageClass guifg=#f09479 guibg=#1b1b1b guisp=#1b1b1b gui=NONE ctermfg=216 ctermbg=234 cterm=NONE
hi Todo guifg=#bbbb87 guibg=#1b1b1b guisp=#1b1b1b gui=bold,underline ctermfg=144 ctermbg=234 cterm=bold,underline
hi Special guifg=#e0c07e guibg=#1b1b1b guisp=#1b1b1b gui=NONE ctermfg=180 ctermbg=234 cterm=NONE
hi LineNr guifg=#a7a7a7 guibg=#292929 guisp=#292929 gui=NONE ctermfg=248 ctermbg=235 cterm=NONE
hi StatusLine guifg=#000000 guibg=#d0d0d0 guisp=#d0d0d0 gui=bold ctermfg=NONE ctermbg=252 cterm=bold
hi Label guifg=#f09479 guibg=#1b1b1b guisp=#1b1b1b gui=NONE ctermfg=216 ctermbg=234 cterm=NONE
hi PMenuSel guifg=#000000 guibg=#9fb6cd guisp=#9fb6cd gui=NONE ctermfg=NONE ctermbg=146 cterm=NONE
hi Search guifg=#000000 guibg=#bbbb87 guisp=#bbbb87 gui=bold ctermfg=NONE ctermbg=144 cterm=bold
hi Delimiter guifg=#e0c07e guibg=#1b1b1b guisp=#1b1b1b gui=NONE ctermfg=180 ctermbg=234 cterm=NONE
hi Statement guifg=#7ec0ee guibg=#1b1b1b guisp=#1b1b1b gui=NONE ctermfg=117 ctermbg=234 cterm=NONE
hi Comment guifg=#bbbb87 guibg=#1b1b1b guisp=#1b1b1b gui=NONE ctermfg=144 ctermbg=234 cterm=NONE
hi Character guifg=#8fe779 guibg=#1b1b1b guisp=#1b1b1b gui=NONE ctermfg=156 ctermbg=234 cterm=NONE
hi Number guifg=#8fe779 guibg=#1b1b1b guisp=#1b1b1b gui=NONE ctermfg=156 ctermbg=234 cterm=NONE
hi Boolean guifg=#7ec0ee guibg=#1b1b1b guisp=#1b1b1b gui=NONE ctermfg=117 ctermbg=234 cterm=NONE
hi Operator guifg=#f09479 guibg=#1b1b1b guisp=#1b1b1b gui=NONE ctermfg=216 ctermbg=234 cterm=NONE
hi Question guifg=#e0c07e guibg=#1b1b1b guisp=#1b1b1b gui=bold ctermfg=180 ctermbg=234 cterm=bold
hi WarningMsg guifg=#ee2c2c guibg=#1b1b1b guisp=#1b1b1b gui=bold ctermfg=13 ctermbg=234 cterm=bold
hi VisualNOS guifg=#ababab guibg=#1b1b1b guisp=#1b1b1b gui=bold,underline ctermfg=248 ctermbg=234 cterm=bold,underline
hi DiffDelete guifg=#d0d0d0 guibg=#8b0000 guisp=#8b0000 gui=NONE ctermfg=252 ctermbg=88 cterm=NONE
hi ModeMsg guifg=#d0d0d0 guibg=#1b1b1b guisp=#1b1b1b gui=bold ctermfg=252 ctermbg=234 cterm=bold
hi Define guifg=#d7a0d7 guibg=#1b1b1b guisp=#1b1b1b gui=NONE ctermfg=182 ctermbg=234 cterm=NONE
hi Function guifg=#7ee0ce guibg=#1b1b1b guisp=#1b1b1b gui=NONE ctermfg=116 ctermbg=234 cterm=NONE
hi FoldColumn guifg=#d0d0d0 guibg=#3d3d3d guisp=#3d3d3d gui=NONE ctermfg=252 ctermbg=237 cterm=NONE
hi PreProc guifg=#d7a0d7 guibg=#1b1b1b guisp=#1b1b1b gui=NONE ctermfg=182 ctermbg=234 cterm=NONE
hi Visual guifg=#000000 guibg=#ababab guisp=#ababab gui=bold ctermfg=NONE ctermbg=248 cterm=bold
hi MoreMsg guifg=#d0d097 guibg=#1b1b1b guisp=#1b1b1b gui=bold ctermfg=187 ctermbg=234 cterm=bold
hi VertSplit guifg=#000000 guibg=#878787 guisp=#878787 gui=bold ctermfg=NONE ctermbg=102 cterm=bold
hi Exception guifg=#f09479 guibg=#1b1b1b guisp=#1b1b1b gui=NONE ctermfg=216 ctermbg=234 cterm=NONE
hi Keyword guifg=#f09479 guibg=#1b1b1b guisp=#1b1b1b gui=NONE ctermfg=216 ctermbg=234 cterm=NONE
hi Type guifg=#f09479 guibg=#1b1b1b guisp=#1b1b1b gui=NONE ctermfg=216 ctermbg=234 cterm=NONE
hi DiffChange guifg=#d0d0d0 guibg=#00008b guisp=#00008b gui=NONE ctermfg=252 ctermbg=18 cterm=NONE
hi Cursor guifg=#000000 guibg=#e7e7e7 guisp=#e7e7e7 gui=bold ctermfg=NONE ctermbg=254 cterm=bold
hi Error guifg=#ee2c2c guibg=#1b1b1b guisp=#1b1b1b gui=NONE ctermfg=13 ctermbg=234 cterm=NONE
hi PMenu guifg=#000000 guibg=#6c7b8b guisp=#6c7b8b gui=NONE ctermfg=NONE ctermbg=60 cterm=NONE
hi SpecialKey guifg=#a28b5b guibg=#1b1b1b guisp=#1b1b1b gui=NONE ctermfg=137 ctermbg=234 cterm=NONE
hi Constant guifg=#8fe779 guibg=#1b1b1b guisp=#1b1b1b gui=NONE ctermfg=156 ctermbg=234 cterm=NONE
hi Tag guifg=#e0c07e guibg=#1b1b1b guisp=#1b1b1b gui=NONE ctermfg=180 ctermbg=234 cterm=NONE
hi String guifg=#8fe779 guibg=#1b1b1b guisp=#1b1b1b gui=NONE ctermfg=156 ctermbg=234 cterm=NONE
hi PMenuThumb guifg=NONE guibg=#a7a7a7 guisp=#a7a7a7 gui=NONE ctermfg=NONE ctermbg=248 cterm=NONE
hi Repeat guifg=#f09479 guibg=#1b1b1b guisp=#1b1b1b gui=NONE ctermfg=216 ctermbg=234 cterm=NONE
hi Directory guifg=#1e90ff guibg=#1b1b1b guisp=#1b1b1b gui=NONE ctermfg=33 ctermbg=234 cterm=NONE
hi Structure guifg=#f09479 guibg=#1b1b1b guisp=#1b1b1b gui=NONE ctermfg=216 ctermbg=234 cterm=NONE
hi Macro guifg=#d7a0d7 guibg=#1b1b1b guisp=#1b1b1b gui=NONE ctermfg=182 ctermbg=234 cterm=NONE
hi Underlined guifg=#1e90ff guibg=#1b1b1b guisp=#1b1b1b gui=underline ctermfg=33 ctermbg=234 cterm=underline
hi DiffAdd guifg=#d0d0d0 guibg=#008b00 guisp=#008b00 gui=NONE ctermfg=252 ctermbg=28 cterm=NONE
hi cursorim guifg=#ffffff guibg=#000000 guisp=#000000 gui=NONE ctermfg=15 ctermbg=NONE cterm=NONE
hi underline guifg=#afafff guibg=NONE guisp=NONE gui=NONE ctermfg=147 ctermbg=NONE cterm=NONE
hi lcursor guifg=#1b1b1b guibg=#d0d0d0 guisp=#d0d0d0 gui=bold ctermfg=234 ctermbg=252 cterm=bold
hi user1 guifg=#000000 guibg=#84E12E guisp=#84E12E gui=bold ctermfg=NONE ctermbg=76 cterm=bold
hi condtional guifg=#ff0000 guibg=#000000 guisp=#000000 gui=NONE ctermfg=196 ctermbg=NONE cterm=NONE
hi subtitle guifg=#000000 guibg=#66bbbb guisp=#66bbbb gui=bold,underline ctermfg=NONE ctermbg=73 cterm=bold,underline
hi htmlitalic guifg=#d0d0d0 guibg=#1b1b1b guisp=#1b1b1b gui=italic ctermfg=252 ctermbg=234 cterm=NONE
hi htmlboldunderlineitalic guifg=#d0d0d0 guibg=#1b1b1b guisp=#1b1b1b gui=bold,italic,underline ctermfg=252 ctermbg=234 cterm=bold,underline
hi htmlbolditalic guifg=#d0d0d0 guibg=#1b1b1b guisp=#1b1b1b gui=bold,italic ctermfg=252 ctermbg=234 cterm=bold
hi htmlunderlineitalic guifg=#d0d0d0 guibg=#1b1b1b guisp=#1b1b1b gui=italic,underline ctermfg=252 ctermbg=234 cterm=underline
hi htmlbold guifg=#d0d0d0 guibg=#1b1b1b guisp=#1b1b1b gui=bold ctermfg=252 ctermbg=234 cterm=bold
hi htmlboldunderline guifg=#d0d0d0 guibg=#1b1b1b guisp=#1b1b1b gui=bold,underline ctermfg=252 ctermbg=234 cterm=bold,underline
hi htmlunderline guifg=#d0d0d0 guibg=#1b1b1b guisp=#1b1b1b gui=underline ctermfg=252 ctermbg=234 cterm=underline
hi spellerrors guifg=#9C0D0D guibg=NONE guisp=NONE gui=NONE ctermfg=124 ctermbg=NONE cterm=NONE
hi charachter guifg=#644A9B guibg=NONE guisp=NONE gui=NONE ctermfg=97 ctermbg=NONE cterm=NONE
hi done guifg=#CCEEFF guibg=#bebebe guisp=#bebebe gui=NONE ctermfg=195 ctermbg=7 cterm=NONE
hi perlpod guifg=#B86A18 guibg=NONE guisp=NONE gui=NONE ctermfg=130 ctermbg=NONE cterm=NONE
hi autohigroup guifg=NONE guibg=#ffff00 guisp=#ffff00 gui=NONE ctermfg=NONE ctermbg=11 cterm=NONE
hi rubyconstant guifg=#00ffff guibg=NONE guisp=NONE gui=NONE ctermfg=14 ctermbg=NONE cterm=NONE
hi rubypseudovariable guifg=#005fff guibg=NONE guisp=NONE gui=NONE ctermfg=27 ctermbg=NONE cterm=NONE
hi rubystringdelimiter guifg=#005fff guibg=NONE guisp=NONE gui=NONE ctermfg=27 ctermbg=NONE cterm=NONE
hi rubysymbol guifg=#005fff guibg=NONE guisp=NONE gui=NONE ctermfg=27 ctermbg=NONE cterm=NONE
hi rubyinterpolation guifg=#5fd787 guibg=NONE guisp=NONE gui=NONE ctermfg=78 ctermbg=NONE cterm=NONE
hi tags guifg=#ffa500 guibg=NONE guisp=NONE gui=NONE ctermfg=214 ctermbg=NONE cterm=NONE
hi type guifg=#afaf5f guibg=NONE guisp=NONE gui=NONE ctermfg=143 ctermbg=NONE cterm=NONE
hi taglisttagname guifg=#005fd7 guibg=NONE guisp=NONE gui=bold ctermfg=26 ctermbg=NONE cterm=bold
hi typedef guifg=#66D9EF guibg=NONE guisp=NONE gui=NONE ctermfg=81 ctermbg=NONE cterm=NONE
hi yamltab guifg=NONE guibg=#FF0000 guisp=#FF0000 gui=NONE ctermfg=NONE ctermbg=196 cterm=NONE
hi yamlbasekey guifg=NONE guibg=NONE guisp=NONE gui=bold,underline ctermfg=NONE ctermbg=NONE cterm=bold,underline
hi phpdocblock guifg=#94E1E4 guibg=#050505 guisp=#050505 gui=bold,italic,underline ctermfg=116 ctermbg=232 cterm=bold,underline
hi icursor guifg=#ffffff guibg=#000000 guisp=#000000 gui=NONE ctermfg=15 ctermbg=NONE cterm=NONE
hi char guifg=#008000 guibg=#ffffff guisp=#ffffff gui=NONE ctermfg=2 ctermbg=15 cterm=NONE
