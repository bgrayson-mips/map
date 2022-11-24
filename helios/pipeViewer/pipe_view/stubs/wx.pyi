from __future__ import annotations
from typing import Callable, Iterator, List, Optional, Tuple, Union, overload

class Object: ...

class Trackable: ...

class EvtHandler(Object, Trackable):
    def Bind(self,
             event: int,
             handler: Callable,
             source: Optional[Object] = None,
             id: int = ID_ANY,
             id2: int = ID_ANY) -> None: ...

class EventFilter: ...
class AppConsole(EvtHandler, EventFilter): ...

class App(AppConsole):
    def __init__(self,
                 redirect: bool = False,
                 filename: Optional[str] = None,
                 useBestVisual: bool = False,
                 clearSigInt: bool = True) -> None: ...
    def MainLoop(self) -> None: ...

def NewId() -> int: ...

BOTH: int
HORIZONTAL: int
VERTICAL: int
CENTRE: int
ALIGN_CENTER: int
ALIGN_CENTER_HORIZONTAL: int
ALIGN_CENTER_VERTICAL: int
ALIGN_BOTTOM: int
ALIGN_LEFT: int
ALIGN_RIGHT: int
ALIGN_TOP: int
BOTTOM: int
LEFT: int
RIGHT: int
TOP: int
ALL: int
EXPAND: int
ID_ANY: int
ID_CANCEL: int
ID_OK: int
ID_FIND: int
ID_EXIT: int
ID_DELETE: int
ID_SAVE: int
ID_BACKWARD: int
DEFAULT_DIALOG_STYLE: int
MAXIMIZE_BOX: int
BORDER_NONE: int
BORDER_SIMPLE: int
BORDER_SUNKEN: int
RESIZE_BORDER: int
SUNKEN_BORDER: int
CAPTION: int
CLOSE_BOX: int
CLIP_CHILDREN: int
STAY_ON_TOP: int
SYSTEM_MENU: int
TAB_TRAVERSAL: int

OK: int
CANCEL: int

EVT_BUTTON: int
EVT_SPINCTRL: int
EVT_CLOSE: int
EVT_MENU: int
EVT_TEXT: int
EVT_TEXT_ENTER: int
EVT_LIST_ITEM_ACTIVATED: int
EVT_LIST_ITEM_RIGHT_CLICK: int
EVT_KEY_UP: int
EVT_KEY_DOWN: int
EVT_LEFT_DOWN: int
EVT_CHECKBOX: int
EVT_ENTER_WINDOW: int
EVT_SET_FOCUS: int
EVT_TIMER: int

KeyCode = int
WXK_UP: KeyCode
WXK_DOWN: KeyCode
WXK_RIGHT: KeyCode
WXK_LEFT: KeyCode
WXK_PAGEUP: KeyCode
WXK_PAGEDOWN: KeyCode
WXK_HOME: KeyCode
WXK_END: KeyCode
WXK_SHIFT: KeyCode
WXK_CONTROL: KeyCode
WXK_ESCAPE: KeyCode
WXK_RETURN: KeyCode
WXK_ENTER: KeyCode

MOD_CONTROL: int

TIMER_CONTINUOUS: int

class Timer(EvtHandler):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, owner: EvtHandler, id: int = -1) -> None: ...
    def Start(self, milliseconds: int = -1, oneShot: int = TIMER_CONTINUOUS) -> bool: ...
    def Stop(self) -> None: ...

class Size:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, width: int, height: int) -> None: ...
    def __getitem__(self, idx: int) -> int: ...
    def __iter__(self) -> Iterator[int]: ...

SizeUnion = Union[Tuple[int, int], Size]

class Event:
    def GetId(self) -> int: ...
    def Skip(self, skip: bool = True) -> None: ...
    def GetEventObject(self) -> Object: ...

class PaintEvent(Event): ...

class CommandEvent(Event):
    def GetString(self) -> str: ...

class NotifyEvent(CommandEvent): ...

class MenuEvent(Event): ...

class FocusEvent(Event): ...

class TimerEvent(Event): ...

class KeyboardState:
    def AltDown(self) -> bool: ...
    def ControlDown(self) -> bool: ...
    def ShiftDown(self) -> bool: ...
    def GetModifiers(self) -> int: ...

class KeyEvent(Event, KeyboardState):
    def GetKeyCode(self) -> int: ...

class MouseState(KeyboardState):
    def GetPosition(self) -> Point: ...
    def LeftIsDown(self) -> bool: ...

class MouseEvent(Event, MouseState):
    def GetWheelDelta(self) -> int: ...
    def GetWheelRotation(self) -> int: ...

ALPHA_OPAQUE: int

class Colour:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, red: int, green: int, blue: int, alpha: int = ALPHA_OPAQUE) -> None: ...
    @overload
    def __init__(self, colRGB: int) -> None: ...
    @overload
    def __init__(self, colour: Colour) -> None: ...

BLACK: Colour
WHITE: Colour
RED: Colour

ColourUnion = Union[Tuple[int, int, int], List[int], str, Colour]

ImageResizeQuality = int
IMAGE_QUALITY_NORMAL: ImageResizeQuality
IMAGE_QUALITY_HIGH: ImageResizeQuality

class Image:
    def Scale(self, width: int, height: int, quality: ImageResizeQuality = IMAGE_QUALITY_NORMAL) -> Image: ...

StockCursor = int
CURSOR_WAIT: StockCursor
CURSOR_SIZING: StockCursor
HOURGLASS_CURSOR: StockCursor


class Cursor:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,
                 cursorName: str,
                 type: BitmapType = BITMAP_TYPE_ANY,
                 hotSpotX: int = 0,
                 hotSpotY: int = 0) -> None: ...
    @overload
    def __init__(self, cursorId: StockCursor) -> None: ...
    @overload
    def __init__(self, image: Image) -> None: ...
    @overload
    def __init__(self, cursor: Cursor) -> None: ...

class RealPoint: ...

class Point:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, x: int, y: int) -> None: ...
    @overload
    def __init__(self, pt: RealPoint) -> None: ...
    def __getitem__(self, idx: int) -> int: ...
    def __iter__(self) -> Iterator[int]: ...

PointUnion = Union[Tuple[int, int], Point]

class ToolTip(Object): ...

SIZE_AUTO: int
SIZE_USE_EXISTING: int

class Window(EvtHandler):
    def SetMinSize(self, size: SizeUnion) -> None: ...
    def GetId(self) -> int: ...
    def GetTextExtent(self, string: str) -> Size: ...
    def SetSizer(self, sizer: Sizer, deleteOld: bool = True) -> None: ...
    def Hide(self) -> bool: ...
    def Destroy(self) -> None: ...
    def GetSize(self) -> Size: ...
    def GetBackgroundColour(self) -> Colour: ...
    def SetBackgroundColour(self, colour: ColourUnion) -> bool: ...
    def SetForegroundColour(self, colour: ColourUnion) -> bool: ...
    def SetAutoLayout(self, autoLayout: bool) -> None: ...
    def Enable(self, enable: bool = True) -> None: ...
    def SetFont(self, font: Font) -> None: ...
    def GetFont(self) -> Font: ...
    def GetClientSize(self) -> Size: ...
    def Layout(self) -> bool: ...
    def Fit(self) -> None: ...
    def GetCursor(self) -> Cursor: ...
    @overload
    def ScreenToClient(self, x: int, y: int) -> Tuple[int, int]: ...
    @overload
    def ScreenToClient(self, pt: Point) -> Point: ...
    @overload
    def PopupMenu(self, menu: Menu, pos: Point = DefaultPosition) -> bool: ...
    @overload
    def PopupMenu(self, menu: Menu, x: int, y: int) -> bool: ...
    def Show(self, show: bool = True) -> bool: ...
    def Raise(elf) -> None: ...
    def SetFocus(self) -> None: ...
    @overload
    def SetToolTip(self, tipString: str) -> None: ...
    @overload
    def SetToolTip(self, tip: ToolTip) -> None: ...
    def Close(self, force: bool = False) -> bool: ...
    def GetBestSize(self) -> Size: ...
    def GetRect(self) -> Rect: ...
    def SetRect(self, rect: RectUnion) -> None: ...
    def Disable(self) -> bool: ...
    def DestroyLater(self) -> None: ...
    def Update(self) -> None: ...
    def SetPosition(self, pt: PointUnion) -> None: ...
    @overload
    def SetClientSize(self, width: int, height: int) -> None: ...
    @overload
    def SetClientSize(self, size: SizeUnion) -> None: ...
    @overload
    def SetClientSize(self, rect: RectUnion) -> None: ...
    @overload
    def SetSize(self, x: int, y: int, width: int, height: int, sizeFlags: int = SIZE_AUTO) -> None: ...
    @overload
    def SetSize(self, size: SizeUnion) -> None: ...
    @overload
    def SetSize(self, rect: RectUnion) -> None: ...
    @overload
    def SetSize(self, width: int, height: int) -> None: ...
    def GetParent(self) -> Window: ...
    @overload
    def ClientToScreen(self, x: int, y: int) -> Tuple[int, int]: ...
    @overload
    def ClientToScreen(self, pt: PointUnion) -> Point: ...
    def RefreshRect(self, rect: RectUnion, eraseBackground: bool = True) -> None: ...
    def CaptureMouse(self) -> None: ...
    def HasCapture(self) -> bool: ...
    def ReleaseMouse(self) -> None: ...
    def SetCursor(self, cursor: Cursor) -> bool: ...
    def SetSizerAndFit(self, sizer: Sizer, deleteOld: bool = True) -> None: ...
    @overload
    def Move(self, x: int, y: int, flags: int = SIZE_USE_EXISTING) -> None: ...
    @overload
    def Move(self, pt: PointUnion, flags: int = SIZE_USE_EXISTING) -> None: ...

class Scrolled:
    @overload
    def CalcScrolledPosition(self, x: int, y: int) -> Point: ...
    @overload
    def CalcScrolledPosition(self, pt: PointUnion) -> Point: ...

class ScrolledWindow(Scrolled, Window): ...

class SizerFlags: ...

class PyUserData: ...

class SizerItem(Object): ...

class Rect:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, x: int, y: int, width: int, height: int) -> None: ...
    @overload
    def __init__(self, pos: PointUnion, size: SizeUnion) -> None: ...
    @overload
    def __init__(self, size: SizeUnion) -> None: ...
    @overload
    def __init__(self, topLeft: PointUnion, bottomRight: PointUnion) -> None: ...
    def GetTopLeft(self) -> Point: ...
    def SetPosition(self, pos: Point) -> None: ...
    @overload
    def Inflate(self, dx: int, dy: int) -> Rect: ...
    @overload
    def Inflate(self, diff: Size) -> Rect: ...
    @overload
    def Inflate(self, diff: int) -> Rect: ...

RectUnion = Union[Rect, Tuple[int, int, int, int]]

BitmapType = int
BITMAP_TYPE_ANY: BitmapType
BITMAP_SCREEN_DEPTH: int

class GDIObject(Object): ...

class Bitmap(GDIObject):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, bitmap: Bitmap) -> None: ...
    @overload
    def __init__(self, bits: bytes, width: int, height: int, depth: int) -> None: ...
    @overload
    def __init__(self, width: int, height: int, depth: int = BITMAP_SCREEN_DEPTH) -> None: ...
    @overload
    def __init__(self, sz: SizeUnion, depth: int = BITMAP_SCREEN_DEPTH) -> None: ...
    @overload
    def __init__(self, width: int, height: int, dc: DC) -> None: ...
    @overload
    def __init__(self, name: str, type: BitmapType = BITMAP_TYPE_ANY) -> None: ...
    @overload
    def __init__(self, img: Image, depth: int = BITMAP_SCREEN_DEPTH) -> None: ...
    @overload
    def __init__(self, img: Image, dc: DC) -> None: ...
    @overload
    def __init__(self, listOfBytes: list[bytes]) -> None: ...
    def GetWidth(self) -> int: ...
    def GetHeight(self) -> int: ...
    def IsOk(self) -> bool: ...

BrushStyle = int
BRUSHSTYLE_SOLID: BrushStyle
SOLID: BrushStyle
TRANSPARENT: BrushStyle

class Brush(GDIObject):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, colour: ColourUnion, style: BrushStyle = BRUSHSTYLE_SOLID) -> None: ...
    @overload
    def __init__(self, stippleBitmap: Bitmap) -> None: ...
    @overload
    def __init__(self, brush: Brush) -> None: ...
    def GetColour(self) -> Colour: ...

PenStyle = int
PENSTYLE_SOLID: PenStyle

class PenInfo: ...

class Pen(GDIObject):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, info: PenInfo) -> None: ...
    @overload
    def __init__(self, colour: ColourUnion, width: int = 1, style: PenStyle = PENSTYLE_SOLID) -> None: ...
    @overload
    def __init__(self, pen: Pen) -> None: ...

DefaultCoord: int

DefaultPosition: Point

DefaultSize: Size

class Sizer(Object):
    @overload
    def Add(self, window: Window, flags: SizerFlags) -> None: ...
    @overload
    def Add(self, window: Window, proportion: int = 0, flag: int = 0, border: int = 0, userData: Optional[PyUserData] = None) -> None: ...
    @overload
    def Add(self, sizer: Sizer, flags: SizerFlags) -> None: ...
    @overload
    def Add(self, sizer: Sizer, proportion: int = 0, flag: int = 0, border: int = 0, userData: Optional[PyUserData] = None) -> None: ...
    @overload
    def Add(self, width: int, height: int, proportion: int = 0, flag: int = 0, border: int = 0, userData: Optional[PyUserData] = None) -> None: ...
    @overload
    def Add(self, width: int, height: int, flags: SizerFlags) -> None: ...
    @overload
    def Add(self, item: SizerItem) -> None: ...
    @overload
    def Add(self,
            size: SizeUnion,
            proportion: int = 0,
            flag: int = 0,
            border: int = 0,
            userData: Optional[PyUserData] = None) -> None: ...
    @overload
    def Add(self, size: SizeUnion, flags: SizerFlags) -> None: ...
    def SetSizeHints(self, window: Window) -> None: ...
    def Fit(self, window: Window) -> Size: ...
    @overload
    def Hide(self, window: Window, recursive: bool = False) -> bool: ...
    @overload
    def Hide(self, sizer: Sizer, recursive: bool = False) -> bool: ...
    @overload
    def Hide(self, index: int) -> bool: ...
    @overload
    def Show(self, window: Window, show: bool = True, recursive: bool = False) -> bool: ...
    @overload
    def Show(self, sizer: Sizer, show: bool = True, recursive: bool = False) -> bool: ...
    @overload
    def Show(self, index: int, show: bool = True) -> bool: ...
    @overload
    def Detach(self, window: Window) -> bool: ...
    @overload
    def Detach(self, sizer: Sizer) -> bool: ...
    @overload
    def Detach(self, index: int) -> bool: ...
    @overload
    def Insert(self, index: int, window: Window, flags: SizerFlags) -> SizerItem: ...
    @overload
    def Insert(self,
               index: int,
               window: Window,
               proportion: int = 0,
               flag: int = 0,
               border: int = 0,
               userData: Optional[PyUserData] = None) -> SizerItem: ...
    @overload
    def Insert(self, index: int, sizer: Sizer, flags: SizerFlags) -> SizerItem: ...
    @overload
    def Insert(self,
               index: int,
               sizer: Sizer,
               proportion: int = 0,
               flag: int = 0,
               border: int = 0,
               userData: Optional[PyUserData] = None) -> SizerItem: ...
    @overload
    def Insert(self,
               index: int,
               width: int,
               height: int,
               proportion: int = 0,
               flag: int = 0,
               border: int = 0,
               userData: Optional[PyUserData] = None) -> SizerItem: ...
    @overload
    def Insert(self,
               index: int,
               width: int,
               height: int,
               flags: SizerFlags) -> SizerItem: ...
    @overload
    def Insert(self,
               index: int,
               item: SizerItem) -> SizerItem: ...
    @overload
    def Insert(self,
               index: int,
               size: Size,
               proportion: int = 0,
               flag: int = 0,
               border: int = 0,
               userData: Optional[PyUserData] = None) -> SizerItem: ...
    @overload
    def Insert(self,
               index: int,
               size: Size,
               flags: SizerFlags) -> SizerItem: ...

class BoxSizer(Sizer):
    def __init__(self, orient: int = HORIZONTAL) -> None: ...

class StaticBoxSizer(Sizer):
    @overload
    def __init__(self,
                 box: StaticBox,
                 orient: int = HORIZONTAL) -> None: ...
    @overload
    def __init__(self,
                 orient: int,
                 parent: Window,
                 label: str = '') -> None: ...

class GridSizer(Sizer):
    ...

class FlexGridSizer(GridSizer):
    @overload
    def __init__(self, cols: int, vgap: int, hgap: int) -> None: ...
    @overload
    def __init__(self, cols: int, gap: SizeUnion = Size(0, 0)) -> None: ...
    @overload
    def __init__(self, rows: int, cols: int, vgap: int, hgap: int) -> None: ...
    @overload
    def __init__(self, rows: int, cols: int, gap: SizeUnion = Size(0, 0)) -> None: ...

class NonOwnedWindow(Window): ...

class PopupWindow(NonOwnedWindow):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, parent: Window, flags: int = BORDER_NONE) -> None: ...

class TopLevelWindow(NonOwnedWindow): ...

PanelNameStr: str

class Panel(Window):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,
                 parent: Window,
                 id: int = ID_ANY,
                 pos: PointUnion = DefaultPosition,
                 size: SizeUnion = DefaultSize,
                 style: int = TAB_TRAVERSAL,
                 name: str = PanelNameStr) -> None: ...

class MenuItem(Object):
    def Enable(self, enable: bool = True) -> None: ...

ItemKind = int
ITEM_NORMAL: ItemKind

class Menu(EvtHandler):
    @overload
    def Append(self, id: int, item: str = '', helpString: str = '', kind: ItemKind = ITEM_NORMAL) -> MenuItem: ...
    @overload
    def Append(self, menuItem: MenuItem) -> MenuItem: ...
    def AppendSeparator(self) -> MenuItem: ...

class MenuBar(Window):
    def Append(self, menu: Menu, title: str) -> None: ...

StatusBarNameStr: str
STB_DEFAULT_STYLE: int

class StatusBar(Control): ...

FrameNameStr: str

class Frame(TopLevelWindow):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,
                 parent: Window,
                 id: int = ID_ANY,
                 title: str = '',
                 pos: PointUnion = DefaultPosition,
                 size: SizeUnion = DefaultSize,
                 style: int = DEFAULT_DIALOG_STYLE,
                 name: str = FrameNameStr) -> None: ...
    def SetMenuBar(self, menuBar: MenuBar) -> None: ...
    def CreateStatusBar(self, number: int = 1, style: int = STB_DEFAULT_STYLE, id: int = 0, name: str = StatusBarNameStr) -> None: ...
    def GetStatusBar(self) -> StatusBar: ...
    def SetStatusText(self, text: str, number: int = 0) -> None: ...

DialogNameStr: str

class Dialog(TopLevelWindow):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,
                 parent: Optional[Window],
                 id: int = ID_ANY,
                 title: str = '',
                 pos: PointUnion = DefaultPosition,
                 size: SizeUnion = DefaultSize,
                 style: int = DEFAULT_DIALOG_STYLE,
                 name: str = DialogNameStr) -> None: ...
    def CreateButtonSizer(self, flags: int) -> Sizer: ...
    def GetReturnCode(self) -> int: ...
    def EndModal(self, retCode: int) -> None: ...
    def ShowModal(self) -> int: ...
    def Centre(self, direction: int = BOTH) -> None: ...

FileSelectorPromptStr: str
FileSelectorDefaultWildcardStr: str
FileDialogNameStr: str

FD_DEFAULT_STYLE: int
FD_OPEN: int
FD_CHANGE_DIR: int

class FileDialog(Dialog):
    def __init__(self,
                 parent: Window,
                 message: str = FileSelectorPromptStr,
                 defaultDir: str = '',
                 defaultFile: str = '',
                 wildcard: str = FileSelectorDefaultWildcardStr,
                 style: int = FD_DEFAULT_STYLE,
                 pos: PointUnion = DefaultPosition,
                 size: SizeUnion = DefaultSize,
                 name: str = FileDialogNameStr) -> None: ...
    def ShowModal(self) -> int: ...
    def GetPath(self) -> str: ...
    def GetFilename(self) -> str: ...

class GenericProgressDialog(Dialog): ...

PD_APP_MODAL: int
PD_AUTO_HIDE: int
PD_CAN_ABORT: int
PD_REMAINING_TIME: int

class ProgressDialog(GenericProgressDialog):
    def __init__(self,
                 title: str,
                 message: str,
                 maximum: int = 100,
                 parent: Optional[Window] = None,
                 style: int = PD_APP_MODAL | PD_AUTO_HIDE) -> None: ...
    def Update(self, value: int, newmsg: str = '') -> Tuple[bool, bool]: ...  # type: ignore[override]

class Control(Window):
    @overload
    def GetSizeFromTextSize(self, xlen: int, ylen: int = -1) -> Size: ...
    @overload
    def GetSizeFromTextSize(self, tsize: SizeUnion) -> Size: ...
    def SetLabel(self, label: str) -> None: ...

StaticTextNameStr: str

class StaticText(Control):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,
                 parent: Window,
                 id: int = ID_ANY,
                 label: str = '',
                 pos: PointUnion = DefaultPosition,
                 size: SizeUnion = DefaultSize,
                 style: int = 0,
                 name: str = StaticTextNameStr) -> None: ...
    def Wrap(self, width: int) -> None: ...

class SpinEvent(NotifyEvent): ...

class SpinCtrl(Control):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,
                 parent: Window,
                 id: int = ID_ANY,
                 value: str = '',
                 pos: PointUnion = DefaultPosition,
                 size: SizeUnion = DefaultSize,
                 style: int = 0,
                 min: int = 0,
                 max: int = 100,
                 initial: int = 0,
                 name: str = 'wxSpinCtrl') -> None: ...
    def GetValue(self) -> int: ...
    def SetRange(self, minVal: int, maxVal: int) -> None: ...

class Validator(EvtHandler): ...

DefaultValidator: Validator

ClientData = int

class ItemContainerImmutable:
    def SetStringSelection(self, string: str) -> bool: ...

class ItemContainer(ItemContainerImmutable):
    @overload
    def Append(self, item: str) -> None: ...
    @overload
    def Append(self, item: str, clientData: ClientData) -> None: ...
    @overload
    def Append(self, items: List[str]) -> None: ...
    def AppendItems(self, items: List[str]) -> None: ...
    def Clear(self) -> None: ...

CB_DROPDOWN: int
CB_READONLY: int
TE_PROCESS_ENTER: int

ComboBoxNameStr: str

class ComboBox(Control, ItemContainer, TextEntry):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,
                 parent: Window,
                 id: int = ID_ANY,
                 value: str = '',
                 pos: PointUnion = DefaultPosition,
                 size: SizeUnion = DefaultSize,
                 choices: List[str] = [],
                 style: int = 0,
                 validator: Validator = DefaultValidator,
                 name: str = ComboBoxNameStr) -> None: ...
    def GetValue(self) -> str: ...
    def SetValue(self, text: str) -> None: ...
    @overload
    def SetSelection(self, from_: int, to_: int) -> None: ...
    @overload
    def SetSelection(self, n: int) -> None: ...
    def GetSelection(self) -> int: ...

class TextEntry:
    def GetValue(self) -> str: ...
    def SetValue(self, value: str) -> None: ...
    def SetEditable(self, editable: bool) -> None: ...
    def Clear(self) -> None: ...

TextCtrlNameStr: str

class TextCtrl(Control, TextEntry):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,
                 parent: Window,
                 id: int = ID_ANY,
                 value: str = '',
                 pos: PointUnion = DefaultPosition,
                 size: SizeUnion = DefaultSize,
                 style: int = 0,
                 validator: Validator = DefaultValidator,
                 name: str = TextCtrlNameStr) -> None: ...

class AnyButton(Control): ...

ButtonNameStr: str

class Button(AnyButton):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,
                 parent: Window,
                 id: int = ID_ANY,
                 label: str = '',
                 pos: PointUnion = DefaultPosition,
                 size: SizeUnion = DefaultSize,
                 style: int = 0,
                 validator: Validator = DefaultValidator,
                 name: str = ButtonNameStr) -> None: ...

StaticBoxNameStr: str

class StaticBox(Control):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,
                 parent: Window,
                 id: int = ID_ANY,
                 label: str = '',
                 pos: PointUnion = DefaultPosition,
                 size: SizeUnion = DefaultSize,
                 style: int = 0,
                 name: str = StaticBoxNameStr) -> None: ...

ListCtrlNameStr: str
LC_ICON: int
LC_REPORT: int
LC_SORT_ASCENDING: int

LIST_FORMAT_LEFT: int
LIST_AUTOSIZE: int

class ListItem(Object): ...

class ListEvent(NotifyEvent):
    def GetIndex(self) -> int: ...

class ListCtrl(Control):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,
                 parent: Window,
                 id: int = ID_ANY,
                 pos: PointUnion = DefaultPosition,
                 size: SizeUnion = DefaultSize,
                 style: int = LC_ICON,
                 validator: Validator = DefaultValidator,
                 name: str = ListCtrlNameStr) -> None: ...
    def ClearAll(self) -> None: ...
    @overload
    def InsertColumn(self, col: int, info: ListItem) -> int: ...
    @overload
    def InsertColumn(self, col: int, heading: str, format: int = LIST_FORMAT_LEFT, width: int = LIST_AUTOSIZE) -> int: ...
    def SetColumnWidth(self, col: int, width: int) -> bool: ...
    def SetItem(self, index: int, column: int, label: str, imageId: int = -1) -> bool: ...
    def SetItemBackgroundColour(self, item: int, col: ColourUnion) -> None: ...
    @overload
    def InsertItem(self, info: ListItem) -> int: ...
    @overload
    def InsertItem(self, index: int, label: str) -> int: ...
    @overload
    def InsertItem(self, index: int, imageIndex: int) -> int: ...
    @overload
    def InsertItem(self, index: int, label: str, imageIndex: int) -> int: ...
    def DeleteItem(self, item: int) -> bool: ...

class BitmapBundle: ...

NullBitmap: BitmapBundle

StaticBitmapNameStr: str

class StaticBitmap(Control):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,
                 parent: Window,
                 id: int = ID_ANY,
                 bitmap: Union[Bitmap, BitmapBundle] = NullBitmap,
                 pos: PointUnion = DefaultPosition,
                 size: SizeUnion = DefaultSize,
                 style: int = 0,
                 name: str = StaticBitmapNameStr) -> None: ...

CheckBoxNameStr: str

class CheckBox(Control):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,
                 parent: Window,
                 id: int = ID_ANY,
                 label: str = '',
                 pos: Point = DefaultPosition,
                 size: Size = DefaultSize,
                 style: int = 0,
                 validator: Validator = DefaultValidator,
                 name: str = CheckBoxNameStr) -> None: ...
    def SetValue(self, state: bool) -> None: ...
    def GetValue(self) -> bool: ...

StaticLineNameStr: str

class StaticLine(Control):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,
                 parent: Window,
                 id: int = ID_ANY,
                 pos: Point = DefaultPosition,
                 size: Size = DefaultSize,
                 style: int = 0,
                 name: str = StaticLineNameStr) -> None: ...

RasterOperationMode = int
COPY: RasterOperationMode

class DC(Object):
    def GetTextExtent(self, st: str) -> Size: ...
    def SetPen(self, pen: Pen) -> None: ...
    def SetBrush(self, brush: Brush) -> None: ...
    def SetBackground(self, brush: Brush) -> None: ...
    def SetBackgroundMode(self, mode: int) -> None: ...
    @overload
    def DrawBitmap(self, bitmap: Bitmap, x: int, y: int, useMask: bool = False) -> None: ...
    @overload
    def DrawBitmap(self, bmp: Bitmap, pt: PointUnion, useMask: bool = False) -> None: ...
    @overload
    def DrawLine(self, x1: int, y1: int, x2: int, y2: int) -> None: ...
    @overload
    def DrawLine(self, pt1: PointUnion, pt2: PointUnion) -> None: ...
    @overload
    def DrawRectangle(self, x: int, y: int, width: int, height: int) -> None: ...
    @overload
    def DrawRectangle(self, pt: PointUnion, sz: SizeUnion) -> None: ...
    @overload
    def DrawRectangle(self, rect: Rect) -> None: ...
    @overload
    def DrawText(self, text: str, x: int, y: int) -> None: ...
    @overload
    def DrawText(self, text: str, pt: PointUnion) -> None: ...
    def DrawTextList(self,
                     textList: List[str],
                     coords: List[PointUnion],
                     foregrounds: Optional[Union[ColourUnion, List[ColourUnion]]] = None,
                     backgrounds: Optional[Union[ColourUnion, List[ColourUnion]]] = None) -> None: ...
    @overload
    def SetClippingRegion(self, x: int, y: int, width: int, height: int) -> None: ...
    @overload
    def SetClippingRegion(self, pt: PointUnion, sz: SizeUnion) -> None: ...
    @overload
    def SetClippingRegion(self, rect: Rect) -> None: ...
    def DestroyClippingRegion(self) -> None: ...
    def GetFont(self) -> Font: ...
    def SetFont(self, font: Font) -> None: ...
    def SetLogicalScale(self, x: float, y: float) -> None: ...
    def GetSize(self) -> Size: ...
    def Clear(self) -> None: ...
    def Blit(self,
             xdest: int,
             ydest: int,
             width: int,
             height: int,
             source: DC,
             xsrc: int,
             ysrc: int,
             logicalFunc: RasterOperationMode = COPY,
             useMask: bool = False,
             xsrcMask: int = DefaultCoord,
             ysrcMask: int = DefaultCoord) -> bool: ...
    def StretchBlit(self,
                    xdest: int,
                    ydest: int,
                    dstWidth: int,
                    dstHeight: int,
                    source: DC,
                    xsrc: int,
                    ysrc: int,
                    srcWidth: int,
                    srcHeight: int,
                    logicalFunc: RasterOperationMode = COPY,
                    useMask: bool = False,
                    xsrcMask: int = DefaultCoord,
                    ysrcMask: int = DefaultCoord) -> bool: ...

class MemoryDC(DC):
    def SelectObject(self, bitmap: Bitmap) -> None: ...

class WindowDC(DC): ...

class PrinterDC(DC): ...

class GraphicsObject(Object): ...

class GraphicsContext(GraphicsObject): ...

class GCDC(DC):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, windowDC: WindowDC) -> None: ...
    @overload
    def __init__(self, memoryDC: MemoryDC) -> None: ...
    @overload
    def __init__(self, printerDC: PrinterDC) -> None: ...
    @overload
    def __init__(self, context: GraphicsContext) -> None: ...

FontFamily = int
FONTFAMILY_MODERN: FontFamily

FontStyle = int
NORMAL: FontStyle

FontWeight = int
FONTWEIGHT_BOLD: FontWeight
BOLD: FontWeight

FontEncoding = int
FONTENCODING_DEFAULT: FontEncoding

class FontInfo: ...

class NativeFontInfo: ...

class Font(GDIObject):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, font: Font) -> None: ...
    @overload
    def __init__(self, fontInfo: FontInfo) -> None: ...
    @overload
    def __init__(self,
                 pointSize: int,
                 family: FontFamily,
                 style: FontStyle,
                 weight: FontWeight,
                 underline: bool = False,
                 faceName: str = '',
                 encoding: FontEncoding = FONTENCODING_DEFAULT) -> None: ...
    @overload
    def __init__(self,
                 pixelSize: SizeUnion,
                 family: FontFamily,
                 style: FontStyle,
                 weight: FontWeight,
                 underline: bool = False,
                 faceName: str = '',
                 encoding: FontEncoding = FONTENCODING_DEFAULT) -> None: ...
    @overload
    def __init__(self, nativeInfoString: str) -> None: ...
    @overload
    def __init__(self, nativeInfo: NativeFontInfo) -> None: ...
    def SetWeight(self, weight: FontWeight) -> None: ...

class FontEnumerator:
    @staticmethod
    def IsValidFacename(facename: str) -> bool: ...

ArtID = int
ART_DELETE: ArtID
ART_FILE_SAVE: ArtID
ART_GO_BACK: ArtID
ART_WARNING: ArtID

ArtClient = int
ART_MESSAGE_BOX: ArtClient

class ArtProvider(Object):
    @staticmethod
    def GetBitmap(id: ArtID, client: ArtClient, size: SizeUnion = DefaultSize) -> Bitmap: ...

class DataObject: ...
class DataObjectSimple(DataObject): ...
class TextDataObject(DataObjectSimple):
    def SetText(self, strText: str) -> None: ...

class Clipboard(Object):
    def Open(self) -> bool: ...
    def SetData(self, data: DataObject) -> bool: ...
    def IsOpened(self) -> bool: ...
    def Close(self) -> None: ...

TheClipboard: Clipboard

def GetDisplayPPI() -> Size: ...
def GetMousePosition() -> Point: ...
def SetCursor(cursor: Cursor) -> None: ...
def BeginBusyCursor(cursor: Union[StockCursor, Cursor] = HOURGLASS_CURSOR) -> None: ...
def IsBusy() -> bool: ...
def EndBusyCursor() -> None: ...
def SafeYield(win: Optional[Window] = None, onlyIfNeeded: bool = False) -> bool: ...
def ImageFromBitmap(bitmap: Bitmap) -> Image: ...
def BitmapFromImage(image: Image) -> Bitmap: ...
def PostEvent(dest: EvtHandler, event: Event) -> None: ...

MessaageBoxCaptionStr: str
def MessageBox(message: str,
               caption: str = MessaageBoxCaptionStr,
               style: int = OK | CENTRE,
               parent: Optional[Window] = None,
               x: int = DefaultCoord,
               y: int = DefaultCoord) -> int: ...
