set nu
map <F5> <Esc>:w<CR>:!clear;python % <CR>

set ts=4
set expandtab
set autoindent

set title
set hlsearch


autocmd BufWritePre *.py :%s/\s\+$//e

execute pathogen#infect()

set statusline+=%#warningmsg#
set statusline+=%{SyntasticStatuslineFlag()}
set statusline+=%*

""color scheme
colorscheme gruvbox
let g:gruvbox_italic=1
set termguicolors
set bg=dark
let g:gruvbox_contrast_dark='soft'
"colorscheme desert

" Syntastic
let g:syntastic_check_on_open = 0
let g:syntastic_check_on_wq = 0
let g:syntastic_mode_map = {'mode':'passive'}
nnoremap <F10> :SyntasticCheck<CR> :SyntasticToggleMode<CR> :w<CR>

" configure expanding of tabs for various file types
au BufRead,BufNewFile *.py set expandtab
au BufRead,BufNewFile *.c set noexpandtab
au BufRead,BufNewFile *.h set noexpandtab
au BufRead,BufNewFile Makefile* set noexpandtab

" indent Line
let g:indentLine_char_list = ['|', '¦', '┊','┆', '┊']

" --------------------------------------------------------------------------------
" configure editor with tabs and nice stuff...
" --------------------------------------------------------------------------------
set expandtab           " enter spaces when tab is pressed
set textwidth=120       " break lines when line length increases
set tabstop=4           " use 4 spaces to represent tab
set softtabstop=4
set shiftwidth=4        " number of spaces to use for auto indent
set autoindent          " copy indent from current line when starting a new line

" make backspaces more powerfull
set backspace=indent,eol,start

set ruler                           " show line and column number
syntax on               " syntax highlighting
set showcmd             " show (partial) command in status line
