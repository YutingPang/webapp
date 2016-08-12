set nocompatible              " required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'gmarik/Vundle.vim'

" Add all your plugins here (note older versions of Vundle used Bundle instead of Plugin)

Plugin 'jnurmine/Zenburn'
Plugin 'altercation/vim-colors-solarized'
Plugin 'tmhedberg/SimpylFold'
Plugin 'vim-scripts/indentpython.vim'
Plugin 'scrooloose/syntastic'
Plugin 'tpope/vim-fugitive'

" All of your Plugins must be added before the following line

call vundle#end()            " required

filetype plugin indent on    " required

set foldmethod=indent
set foldlevel=99

" Pyhton3 setting
au BufNewFile,BufRead *.py
    \ set tabstop=4
"    \ set softtabstop=4
    \ set shiftwidth=4
    \ set textwidth=79
    \ set expandtab
"    \ set autoindent
    \ set fileformat=unix

" full stack setting
au BufNewFile,BufRead *.js, *.html, *.css
    \ set tabstop=2
    \ set softtabstop=2
    \ set shiftwidth=2

set number
let g:solarized_termcolors=256
set t_Co=256 
set background=dark
set encoding=utf-8
colorscheme solarized
set splitbelow
set splitright

set tabstop=4

let g:SimpylFold_docstring_preview=1

" Virtualenv Support
python3 << EOF
import os
import sys
if 'VIRTUAL_ENV' in os.environ:
	project_base_dir = os.environ['VIRTUAL_ENV']
	activate_this = os.path.join(project_base_dir, 'bin/activate_this.py')
	execfile(activate_this, dict(__file__=activate_this))
EOF

" syntastic with pathogen
execute pathogen#infect()

" scrooloose?syntastic setting
set statusline+=%#warningmsg#
set statusline+=%{SyntasticStatuslineFlag()}
set statusline+=%*

let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list = 1
let g:syntastic_check_on_open = 1
let g:syntastic_check_on_wq = 0

" Make code look pretty
let python_highlight_all=1
syntax on

" color scheme based on VIM mode
if has('gui_running')
	set background=dark
	colorscheme solarized
else
	colorscheme zenburn
endif

" Solarized also ships with a dark and light theme. To make switching between
" them very easy (by pressing F5) add
call togglebg#map("<F5>")

" switch syntastic to python3 version
let g:syntastic_python_python_exec = 'python3'

" set F9 to run button
nnoremap <buffer> <F12> :exec '!python3' shellescape(@%, 1)<cr>

" set F8 to NERDTree
nnoremap <F8> :NERDTree <cr>
