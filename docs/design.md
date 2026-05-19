# >> Fire Emblem Fates Revelation Archipelago Design

## >> Core goal

Create an Archipelago world for Fire Emblem Fates Revelation.

The player completes Fates checks such as chapters, chests, shops, recruitments, and My Castle upgrades. These checks can contain items for other Archipelago players. Other players can find Fates items, which are then sent back to the Fates client.

## >> Route?

- Revelation

## >> Goal

- Clear Final Chaper (Revelation)
- After goal completion, use Archipelago's built-in release behaviour to release remaining checks/items

## >> Randomization

- Units randomized
- Starting weapons randomized
- Fork ignis randomiser? likely handles patch generation

## >> Checks

Planned check categories:

- Chapter completions
- Chest checks
- Shop slot checks
- Recruitment checks
- Child unit checks
- My Castle building/shop upgrade checks
- Optional special class checks later

## >> Chest rules

Opening a chest sends the check immediately.

On chapter clear:

- unopened chests containing remote/out-world items are auto-checked
- unopened chests containing local Fates progression items are auto-checked
- unopened chests containing local Fates useful/filler/trap items are skipped/lost

Chest access must be guaranteed when chest checks are enabled.

Planned safety:

- MC gets Locktouch or equivalent access
- limited Chest Keys remain available as backup

## >> Shop rules

Shops contain AP voucher/check slots.

Buying a shop voucher sends the matching AP location check.

Shop upgrades unlock more AP shop checks.

## >> Master Seal safety

Limited Master Seals should be guaranteed locally.

Extra Master Seals may still appear in the AP item pool.

## >> Recruitment rules

Recruitment checks should probably be based on recruitment slots rather than exact randomized unit identity.

Male Kana and Female Kana count as one shared check:

- Recruitment - Kana

## >> DeathLink

Outgoing DeathLink:

- any deployed player-controlled unit defeat sends DeathLink
- no separate DeathLink on game over
- DeathLink-caused unit defeats do not send another DeathLink

Incoming DeathLink:

- if a player unit is currently in combat, defeat that combat unit
- otherwise, defeat a random living deployed player unit
- if no valid unit exists, queue the DeathLink until the next map

## >> Expected mode

- Lunatic/Casual