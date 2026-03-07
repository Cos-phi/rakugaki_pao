#!/usr/bin/perl
use strict;
use warnings;

use CGI;
use CGI::Carp qw(fatalsToBrowser warningsToBrowser);
use GD;
use MIME::Base64;

my $q = CGI->new;

my $palette = $q->param('palette') // '';

# テスト用（ブラウザ直アクセス時）
$palette ||= 'NjZK8u7m-.6mn.sSN.fGae7B_nb7q1Mj08Mbw-w8PD';

# ----------------------------
# palette を分解
# ----------------------------

my ($sec1,$sec2,$sec3) = split /-/, $palette;

my @two   = decode_section($sec1);
my @seven = decode_section($sec2);
my @one   = decode_section($sec3);

# 背景色（最初の2色の2色目）
my $bg = $two[1] // [240,240,240];

# 正方形の色
my @colors = (@seven,@one);

# ----------------------------
# 画像生成
# ----------------------------

my $img_size = 630;

my $img = GD::Image->new($img_size,$img_size);

my $bgc = $img->colorAllocate(@$bg);

# 正方形色
my @gdcolors;
for my $c (@colors){
    push @gdcolors, $img->colorAllocate(@$c);
}

# ----------------------------
# レイアウト
# ----------------------------

my $cols = 4;
my $rows = 2;

my $square = 110;
my $gap    = 30;

my $grid_w = $cols*$square + ($cols-1)*$gap;
my $grid_h = $rows*$square + ($rows-1)*$gap;

my $start_x = int(($img_size-$grid_w)/2);
my $start_y = int(($img_size-$grid_h)/2);

for my $i (0..$#gdcolors){

    last if $i >= 8;

    my $row = int($i/$cols);
    my $col = $i%$cols;

    my $x1 = $start_x + $col*($square+$gap);
    my $y1 = $start_y + $row*($square+$gap);

    $img->filledRectangle(
        $x1,
        $y1,
        $x1+$square,
        $y1+$square,
        $gdcolors[$i]
    );
}

# ----------------------------
# 出力
# ----------------------------

print "Content-Type: image/png\n\n";
print $img->png;

# ----------------------------
# Base64セクションデコード
# ----------------------------

sub decode_section {

    my $part = shift // '';
    return () unless $part;

    # URL-safe → Base64
    $part =~ s/\./+/g;
    $part =~ s/_/\//g;

    # padding復元
    while(length($part)%4){
        $part .= '=';
    }

    my $bin;
    eval {
        $bin = decode_base64($part);
    };
    return () unless defined $bin;

    my @colors;

    for(my $i=0; $i+2 < length($bin); $i+=3){

        my ($r,$g,$b) = unpack("CCC", substr($bin,$i,3));

        push @colors, [$r,$g,$b];
    }

    return @colors;
}
